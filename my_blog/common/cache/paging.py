from django.core.cache import caches
from django.core.paginator import Paginator

from cache.constants import PagerCacheTTL
from .constants import PAGER_PAGE_NUMBER

# """
# (废弃, 通过保存分页器达到效果)
# redis list
# 总数据：T                 --> [id1, id2, id3]
# 每页数据长度：N
# 总页数：T/N
# 当前页数：p
# 每页页数据：LRANGE key p*(n-1) p*n
# """


class Pager(object):
    """
    缓存分页器
    """
    PAG_KEY = 'page:{}:data'
    __COUNT_KEY = 'page:{}:count'
    TTL = PagerCacheTTL
    cache = caches['caches']

    def __init__(self, key, pk_queryset):
        self.pag_key = self.PAG_KEY.format(key)
        self.count_key = self.__COUNT_KEY.format(key)

        paginator = self.cache.get(self.pag_key)
        total_count = self.cache.get(self.count_key)

        if not paginator:
            # 没有缓存时, 查询并保存查询集
            pks = [pk['article_id'] for pk in pk_queryset]
            # 总数据长度
            total_count = len(pks)
            # 分页器
            paginator = Paginator(pks, PAGER_PAGE_NUMBER)

            # 保存缓存
            self.cache.set(self.pag_key, paginator, self.TTL.get_ttl())
            self.cache.set(self.count_key, total_count, self.TTL.get_ttl())

        self.total_count = total_count
        self.paginator = paginator

    @classmethod
    def clear(cls, key):
        """
        清除缓存
        :return:
        """
        cls.cache.delete(cls.PAG_KEY.format(key))
        cls.cache.delete(cls.__COUNT_KEY.format(key))

    def page(self, current_page=None):
        """
        paginator同名方法
        :param current_page:
        :return:
        """
        return self.paginator.page(current_page)

    @property
    def num_pages(self):
        return self.paginator.num_pages


# @classmethod
#     def get(cls, key, pks):
#         cache = caches['caches']
#         paginator = cache.get(cls.KEY.format(key))
#         total_count = cache.get(cls.COUNT_KEY.format(key))
#
#         if not paginator:
#
#             # 总数据长度
#             total_count = pks.count()
#             # 分页器
#             paginator = Paginator(pks, PAGER_PAGE_NUMBER)
#
#             # 保存到缓存
#             cache.set(cls.KEY.format(key), paginator)
#             cache.set(cls.COUNT_KEY.format(key), total_count)
#
#         return paginator, total_count

