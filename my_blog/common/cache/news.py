import json

from django_redis import get_redis_connection
from redis.exceptions import RedisError

from . import constants
from . import logger
from common.utils.news import get_news


class AllNewsCache(object):
    key = 'home:news:all'
    conn = get_redis_connection('news')
    ttl = constants.NewsCacheTTL

    @classmethod
    def get(cls, count=1):
        """
        获取新闻缓存数据
        :param count: 获取条数
        :return: [{}, {}...]
        """
        # 查询缓存
        # 缓存存在 -> 返回
        # 缓存不存在 -> 更新缓存
        # 更新成功 -> 返回
        # 更新失败 -> 返回 None
        caches = []

        for i in range(constants.TRY_GET_NEWS_COUNT):
            try:
                ret = cls.conn.srandmember(cls.key, count)

                if ret:
                    for r in ret:
                        caches.append(json.loads(r))

                    break
            except RedisError as e:
                logger.warning(e)

        if not caches:
            # 更新缓存
            return cls.reset(count)

        if len(caches) < count:
            # 更新缓存
            return cls.reset(count)

        return caches

    @classmethod
    def reset(cls, count=1):
        """
        更新缓存
        :return:
        """
        caches = []

        # 新闻生成器
        news_generator = get_news()

        for channel, news_list in news_generator:
            if not news_list:
                return caches

            try:
                save_data = [json.dumps(news) for news in news_list]
                cls.conn.sadd(cls.key, *save_data)

            except RedisError as e:
                logger.error(e, 'Update news cache data fail. News channel: {}'.format(channel))

            if len(caches) < count:
                caches.extend(news_list[:count])

        # 过期
        try:
            cls.conn.expire(cls.key, cls.ttl.get_ttl())
        except RedisError as e:
            logger.warning(e, 'Failed to set the validity period of news cache')

        if not caches:
            return None

        return caches

    @classmethod
    def mget(cls, count):
        """
        获取批量新闻
        :param count:
        :return:
        """
        return cls.get(count)
