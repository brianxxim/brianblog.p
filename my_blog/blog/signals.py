# #### 已废弃 ######

# from django.db.models.signals import post_delete, post_save
#
# from cache.alone import ArticleTag, ArticleInfo, ArticleDetail, CategoryInfo, TagInfo, SlideshowInfo, AuthorInfo
# from cache.lasting import AllLink, AllNotice, AllCategory, AllTag, AllRecommendArticle
# from cache.statistics import ArticleCreateTime, ArticleCommentCount, ArticleReadCount
#
#
# def alone_cache_clear(sender, instance, **kwargs):
#     """
#     清除独立缓存(cache)
#     :param sender: 发送信号的模型类
#     :param instance: 发送信号的模型实例
#     :return:
#     """
#     cache_class = (ArticleTag, ArticleInfo, ArticleDetail, CategoryInfo, TagInfo, SlideshowInfo, AuthorInfo)
#
#     pk = instance.pk
#
#     for cls in cache_class:
#         if sender == cls.model:
#             cls(pk).clear()
#
#
# def lasting_caches_clear(sender, instance, **kwargs):
#     """
#     清除持久缓存(caches)
#     :param sender: 发送信号的模型类
#     :param instance: 发送信号的模型实例
#     :return:
#     """
#     cache_class = (AllLink, AllNotice, AllCategory, AllTag, AllRecommendArticle)
#
#     for cls in cache_class:
#         if sender == cls.model:
#             cls().clear()
#
#
# def statistics_cache_clear(sender, instance, **kwargs):
#     """
#     清除统计缓存中的一条数据
#     :param sender: 发送信号的模型类
#     :param instance: 发送信号的模型实例
#     :return:
#     """
#     cache_class = (ArticleReadCount, ArticleCommentCount, ArticleCreateTime)
#     pk = instance.pk
#
#     for cls in cache_class:
#         if cls.model == sender:
#             cls.clear(number=pk)
#
#
# def connect_signals(func, save=True):
#     """
#     connect post_save and post_delete signal
#     """
#     post_delete.connect(func)
#
#     if not save:
#         return
#
#     post_save.connect(func)
#
#
# connect_signals(alone_cache_clear)
# connect_signals(lasting_caches_clear)
# connect_signals(statistics_cache_clear, save=False)
#
