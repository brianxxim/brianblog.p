from datetime import datetime

from django_redis import get_redis_connection
from django.db.models import Model
from redis.client import Redis
from redis.exceptions import RedisError

from . import logger
from .constants import ArticleReadCountTTL, ArticleCommentCountTTL, CacheTTLBase, ArticleCreateTimeTTL
from my_blog.blog.models.articles import Article


class StatisticsCacheBase(CacheTTLBase, object):
    """
    文章阅读量缓存
    """
    conn: Redis = get_redis_connection('caches')
    key = ''
    model: Model

    @classmethod
    def db_query(cls, instance_id=''):
        """
        从数据库中查询中需要的数据
        :return:
        """
        raise NotImplementedError('function db_query is Not implemented')

    @classmethod
    def incr(cls, number, amount=1):
        """
        增加或减数统计数据
        :return:
        """
        try:
            cls.conn.zincrby(cls.key, amount, number)
        except RedisError as e:
            logger.error(e, 'incr Statistics failed. key: {} number: {}'.format(cls.key, number))

    @classmethod
    def get(cls, number):
        """
        获取缓存
        :param number: 需要获取的pk
        :return: score
        """

        try:
            score = cls.conn.zscore(cls.key, number)
        except RedisError as e:
            logger.warning(e)
            score = None

        if score == b'-1':
            return

        if not score:
            # 向数据库查询
            queryset = cls.db_query(number)

            if queryset:
                score = [v for v in queryset[0].values()][1]

                try:
                    cls.conn.zincrby(cls.key, score, number)
                except RedisError as e:
                    logger.warning(e, 'save cache fail key: {}, number: {}'.format(cls.key, number))

        return int(score) if score else 0

    @classmethod
    def get_top(cls, count, score=False):
        """
        获取最热数据
        :param count: 获取条数
        :param score: 是否获取分数
        :return: list[str] [data_id: score, ...]
        """
        pks = []

        for n in range(2):
            try:
                ret = cls.conn.zrandmember(cls.key, count, withscores=score)
            except RedisError as e:
                logger.error(e, 'get rank fail key: {}'.format(cls.key))
                ret = None

            if ret:
                if not score:
                    pks = [r.decode() for r in ret]
                else:
                    data = [r.decode() for r in ret]
                    for i in range(0, len(data), 2):
                        pks.append({
                            'pk': data[i],
                            'score': data[i + 1]
                        })
                break

            # 尝试重置缓存
            cls.reset()

        return pks

    @classmethod
    def clear(cls, number=None):
        """
        清除全部或一条缓存
        :param number: 需要清除的number
        :return:
        """
        if number:
            try:
                cls.conn.zrem(cls.key, number)
            except RedisError as e:
                logger.error(e, 'delete cache fail key: {}, number: {}'.format(cls.key, number))

            return

        try:
            cls.conn.delete(cls.key)
        except RedisError as e:
            logger.error(e, 'delete cache fail key: {}'.format(cls.key))

    @classmethod
    def reset(cls):
        """
        重置缓存
        :return: {} or {pk: score, pk: score}
        """
        pl = cls.conn.pipeline()
        queryset = cls.db_query()
        if queryset:

            cache_data = {}
            for query in queryset:
                v = [v for v in query.values()]
                cache_data[v[0]] = v[1]

            try:
                pl.zadd(cls.key, cache_data)
                pl.expire(cls.key, cls.get_ttl())
                pl.execute()
            except RedisError as e:
                logger.warning(e, 'reset article reading count fail')


class ArticleReadCount(StatisticsCacheBase, ArticleReadCountTTL):
    """
    文章阅读量缓存
    """
    key = 'count:art:read'
    model = Article

    @classmethod
    def db_query(cls, instance_id=None):
        """
        获取缓存
        :return:
        """
        queryset = cls.model.objects.values('article_id', 'read_count').filter(is_delete=False)
        if instance_id:
            queryset = queryset.filter(article_id=instance_id)

        return queryset

    #
    # @classmethod
    # def get(cls, instance_id):
    #     """
    #     获取缓存
    #     :return:
    #     """
    #
    #     try:
    #         score = cls.conn.zscore(cls.key, instance_id)
    #     except RedisError as e:
    #         logger.warning(e)
    #         score = None
    #
    #     if not score:
    #         # 向数据库查询
    #         ret = cls.reset(instance_id)
    #         if ret:
    #             return ret[0]
    #
    #     elif score != b'-1':
    #         return {cls.model.__name__.lower() + '_id': instance_id, 'count': score}
    #
    # # @classmethod
    # # def update(cls, instance_id):
    # #     """
    # #     保存缓存
    # #     :return: {id: count, id: count, ...}
    # #     """
    # #     conn: Redis = get_redis_connection(cls.cache_db)
    # #
    # #     # 查数据
    # #     queryset = cls.db_query(instance_id)
    # #     if not queryset:
    # #         try:
    # #             conn.zadd(cls.key, {instance_id: -1})
    # #             return None
    # #         except RedisError as e:
    # #             logger.warning(e)
    # #
    # #     else:
    # #         try:
    # #             save_data = {}  # {id: count, id2: count2, ...}
    # #             for data in queryset:
    # #                 l = [v for v in data.values()]
    # #                 save_data[l[0]] = l[1]
    # #
    # #             conn.zadd(cls.key, save_data)
    # #         except RedisError as e:
    # #             logger.warning(e, 'save article reading count fail. article_id: {}'.format(instance_id))
    # #
    # #         return [query for query in queryset]
    #
    # @classmethod
    # def reset(cls, instance_id=None):
    #     """
    #     重置缓存
    #     :instance_id: 文章id; 若为空表示重置全部缓存
    #     :return:
    #     """
    #     pl = cls.conn.pipeline()
    #     queryset = cls.db_query(instance_id)
    #
    #     # 重置单个缓存
    #     if instance_id:
    #         if not queryset:
    #             try:
    #                 pl.zadd(cls.key, {instance_id: -1})
    #                 pl.expire(cls.key, cls.get_ttl())
    #                 pl.execute()
    #             except RedisError as e:
    #                 logger.warning(e)
    #
    #     # 重置多个缓存
    #     else:
    #         try:
    #             cls.conn.delete(cls.key)
    #         except RedisError as e:
    #             logger.error(e)
    #
    #     # 保存缓存
    #     if queryset:
    #         save_data = {}  # {id: count, id2: count2, ...}
    #         for cache in queryset:
    #             l = [v for v in cache.values()]
    #             save_data[l[0]] = l[1]
    #
    #         try:
    #             pl.zadd(cls.key, save_data)
    #             pl.expire(cls.key, cls.get_ttl())
    #             pl.execute()
    #         except RedisError as e:
    #             logger.warning(e, 'reset article reading count fail')
    #
    #     return [query for query in queryset]


class ArticleCommentCount(StatisticsCacheBase, ArticleCommentCountTTL):
    """
    文章评论量缓存
    """
    key = 'count:art:comment'
    model = Article

    @classmethod
    def db_query(cls, instance_id=''):
        queryset = cls.model.objects.values('article_id', 'comment_count').filter(is_delete=False)
        if instance_id:
            queryset = queryset.filter(article_id=instance_id)

        return queryset


class ArticleCreateTime(StatisticsCacheBase, ArticleCreateTimeTTL):
    key = 'art:create:time'
    model = Article

    @classmethod
    def db_query(cls, instance_id=''):
        new_queryset = []

        queryset = cls.model.objects.values('article_id', 'create_time').filter(is_delete=False)

        if instance_id:
            queryset = queryset.filter(article_id=instance_id)

        for query in queryset:
            query['create_time'] = datetime.timestamp(query['create_time'])

            new_queryset.append(query)

        return new_queryset
