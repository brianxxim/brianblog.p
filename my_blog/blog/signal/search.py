from whoosh_search.article import remove, reset


def update_search_index(sender, instance, **kwargs):
    """
    更新搜索索引
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    reset(pk=instance.pk)


def delete_search_index(sender, instance, **kwargs):
    """
    删除搜索索引(已停用)
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    remove(instance.pk)
