from cache.alone import ArticleTag, ArticleInfo, ArticleDetail, CategoryInfo, TagInfo, SlideshowInfo, AuthorInfo
from cache.wholes import AllLink, AllNotice, AllCategory, AllTag
from cache.statistics import ArticleCreateTime, ArticleCommentCount, ArticleReadCount
#
#
# class CacheListBase(object):
#     """
#     清除缓存基类
#     """
#     CACHES = ()
#
#     # def __init__(self):
#     #     self.cms = {}
#     #     for cache in self.caches:
#     #         self.cms[cache] = cache.model
#     # 多个子类共用这个实例, 这是不合法的
#     # def __new__(cls, *args, **kwargs):
#     #     """ 创建对象时执行; 需要返回一个对象 """
#     #
#     #     if not hasattr(cls, "_instance"):
#     #         # 创建实例
#     #         obj = super().__new__(cls, *args, **kwargs)
#     #         # 初始化属性
#     #         obj.caches = {cache: cache.model for cache in cls.CACHES}
#     #
#     #         # 保存单例(将实例保存为类属性, 每次创建时返回这个属性)
#     #         cls._instance = obj
#     #
#     #     return cls._instance
#
#
# class AloneCache(CacheListBase):
#     """
#     需要清除的独立缓存
#     """
#     CACHES = (ArticleTag, ArticleInfo, ArticleDetail, CategoryInfo, TagInfo, SlideshowInfo, AuthorInfo)
#
#
# class LastingCache(CacheListBase):
#     """
#     需要清除的持久缓存
#     """
#     LASTING_CACHES = (AllLink, AllNotice, AllCategory, AllTag)
#
#
# class StatisticsCache(CacheListBase):
#     """
#     需要清除的统计缓存
#     """
#     CACHES = (ArticleReadCount, ArticleCommentCount, ArticleCreateTime)


# 独立缓存

ALONE_CACHES = (ArticleTag, ArticleInfo, ArticleDetail, CategoryInfo, TagInfo, SlideshowInfo, AuthorInfo)
# 整体缓存
LASTING_CACHES = (AllLink, AllNotice, AllCategory, AllTag)
# 统计缓存
STATISTIC_CACHES = (ArticleReadCount, ArticleCommentCount, ArticleCreateTime)


def clear_alone_cache(sender, instance, **kwargs):
    """
    清除独立缓存(cache)
    :param sender: 发送信号的模型类
    :param instance: 发送信号的模型实例
    :return:
    """
    # if sender in ac.models:
    #     index = ac.models.index(sender)
    #     ac.caches[index](instance.pk).clear()
    for cache in ALONE_CACHES:
        if cache.model == sender:
            cache(instance.pk).clear()


def clear_lasting_cache(sender, instance, **kwargs):
    """
    清除持久缓存(caches)
    :param sender: 发送信号的模型类
    :param instance: 发送信号的模型实例
    :return:
    """
    for cache in LASTING_CACHES:
        if cache.model == sender:
            cache.clear()
    # for cache, model in LastingCache().caches:
    #     if model == sender:
    #         cache.clear()


def clear_statistics_cache(sender, instance, **kwargs):
    """
    清除统计缓存中的一条数据
    :param sender: 发送信号的模型类
    :param instance: 发送信号的模型实例
    :return:
    """
    for cache in STATISTIC_CACHES:
        if cache.model == sender:
            cache.clear(instance.pk)
    #
    # for cache, model in StatisticsCache().caches:
    #     if model == sender:
    #         cache.clear(instance.pk)


# class ClearCaches(object):
#     """
#     清除缓存工具
#     已废弃 --> assert callable(receiver), "Signal receivers must be callable."
#     """
#     # 需要清除的独立缓存
#     ALONE_CACHES = (ArticleTag, ArticleInfo, ArticleDetail, CategoryInfo, TagInfo, SlideshowInfo, AuthorInfo)
#
#     # 需要清除的持久缓存
#     LASTING_CACHES = (AllLink, AllNotice, AllCategory, AllTag)
#
#     # 需要清除的统计缓存
#     STATISTICS_CACHES = (ArticleReadCount, ArticleCommentCount, ArticleCreateTime)
#
#     def __init__(self):
#         self.alone_caches = [cls.model for cls in self.ALONE_CACHES]
#         self.lasting_caches = [cls.model for cls in self.LASTING_CACHES]
#         self.statistics_cache = [cls.model for cls in self.STATISTICS_CACHES]
#
#     def clear_alone_cache(self, sender, instance, **kwargs):
#         """
#         清除独立缓存(cache)
#         :param sender: 发送信号的模型类
#         :param instance: 发送信号的模型实例
#         :return:
#         """
#         if sender in self.alone_caches:
#
#             index = self.alone_caches[sender]
#             self.ALONE_CACHES[index](instance.pk).clear()
#
#     def clear_lasting_cache(self, sender, instance, **kwargs):
#         """
#         清除持久缓存(caches)
#         :param sender: 发送信号的模型类
#         :param instance: 发送信号的模型实例
#         :return:
#         """
#         if sender in self.lasting_caches:
#
#             index = self.alone_caches[sender]
#             self.LASTING_CACHES[index]().clear()
#
#     def clear_statistics_cache(self, sender, instance, **kwargs):
#         """
#         清除统计缓存中的一条数据
#         :param sender: 发送信号的模型类
#         :param instance: 发送信号的模型实例
#         :return:
#         """
#
#         if sender in self.statistics_cache:
#
#             index = self.alone_caches[sender]
#             self.STATISTICS_CACHES[index].clear(number=instance.pk)
#
#     def connect_signals(self, func, no_save=True, no_delete=True, sender=None):
#         """
#         connect post_save and post_delete signal
#         """
#         kwargs = {'receiver': func}
#
#         if sender:
#             kwargs['sender'] = sender
#
#         if no_delete:
#             post_delete.connect(**kwargs)
#
#         if not no_save:
#             post_save.connect(**kwargs)
#
#     def register(self):
#         self.connect_signals(self.alone_caches)
#         self.connect_signals(self.lasting_caches)
#         self.connect_signals(self.statistics_cache, no_save=False)
