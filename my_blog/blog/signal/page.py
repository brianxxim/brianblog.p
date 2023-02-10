from cache.paging import Pager


def clear_page_cache(sender, instance, **kwargs):
    """
    清除分页缓存
    :param sender: 模型
    :param instance: 实例
    :param kwargs:
    :return:
    """

    # 当标签、分类被删除时  删除缓存
    # 当删除art时  不删除缓存  ->如果用户进入detail页面，显示”文章已删除“
    key = instance.pk
    Pager.clear(key)
