import json

from django.db.models import Model
from django_redis import get_redis_connection
from redis.client import Redis
from redis.exceptions import RedisError

from .constants import CacheTTLBase
from logging import getLogger

logger = getLogger('django')


class CachesBase(CacheTTLBase, object):
    """
    整体缓存基类
    """
    conn: Redis = get_redis_connection('caches')

    key = ''
    model: Model

    @classmethod
    def save_dataset(cls):
        """
        获取需要缓存的查询集
        :return:
        """
        raise NotImplementedError('Model queryset is not set')

    @classmethod
    def all(cls):
        """
        获取缓存
        :return: dict cache
        """
        cache = list()

        try:
            ret = cls.conn.get(cls.key)
        except RedisError as e:
            logger.warning(e)
            ret = None

        if not ret:
            cache = cls.reset()

        elif ret != b'-1':
            cache = json.loads(ret)

        return cache

    @classmethod
    def reset(cls):
        """
        从数据库中重置缓存
        :return: dict cache
        """
        cache_data = None

        queryset = cls.save_dataset()

        if not queryset:
            try:
                cls.conn.setex(cls.key, cls.get_ttl(), -1)
            except RedisError as e:
                logger.warning(e)

        else:
            # 序列化; queryset -> 纯dict
            cache_data = [query for query in queryset]

            try:
                cls.conn.setex(cls.key, cls.get_ttl(), json.dumps(cache_data))
            except RedisError as e:
                logger.warning(e)

        return cache_data

    @classmethod
    def clear(cls):
        """
        清除缓存
        :return:
        """
        try:
            cls.conn.delete(cls.key)
        except RedisError as e:
            logger.warning(e)


class CacheBase(CacheTTLBase, object):
    """
    独立缓存基类
    """
    conn: Redis = get_redis_connection('cache')

    key = str()
    model: Model

    def __init__(self, pk=None):
        if pk:
            self.instance_id = pk
            self.key = self.key.format(pk)

    def __getattr__(self, item):
        raise ValueError('No definition {}'.format(item))

    def db_query(self):
        """
        获取查询集
        此方法需要从数据库中查询并处理成需要的数据
        :return: 需要的数据
        """
        raise NotImplementedError('Function db_query is not defined')

    def _update(self):
        """
        重置缓存
        :return: cache_data
        """
        queryset = self.db_query()

        if not queryset:
            try:
                self.conn.setex(self.key, self.get_ttl(), -1)
            except RedisError as e:
                logger.warning(e, 'Failed to save cache. save_data: -1; key: {}'.format(self.key))

            return

        try:
            self.conn.setex(self.key, self.get_ttl(), json.dumps(queryset))
        except RedisError as e:
            logger.warning(e, 'Failed to save cache. save_data: {}; key: {}'.format(str(queryset), self.key))

        return queryset

    def get(self, pk=None):
        """
        获取缓存
        :return: dict cache
        """
        if pk:
            self.instance_id = pk
            self.key = self.key.format(pk)

        cache = None

        # 获取缓存
        try:
            ret = self.conn.get(self.key)
        except RedisError as e:
            logger.warning(e)
            ret = None

        if not ret:
            cache = self._update()

        elif ret != b'-1':
            cache = json.loads(ret)

        return cache

    @classmethod
    def mget(cls, pks: list):
        """
        批量获取缓存
        :return: [{slideshow_id: 001, cache: {}..}..]
        """
        caches = []

        # 获取数据
        try:
            keys = [cls.key.format(pk) for pk in pks]
            ret = cls.conn.mget(keys)
        except RedisError as e:
            logger.warning(e)
            # 假数据
            ret = [None for i in range(len(pks))]

        for pk, data in dict(zip(pks, ret)).items():  # {1: None, 2: xxx}

            # no cache, try get from database
            if not data:
                data = cls._update(self=cls(pk))

            # data is empty
            elif data == b'-1':
                data = None

            if isinstance(data, bytes):
                data = json.loads(data)

            caches.append(data)

        return caches

    def clear(self):
        """
        清除缓存
        :return:
        """
        try:
            self.conn.delete(self.key)
        except RedisError as e:
            logger.warning(e)
