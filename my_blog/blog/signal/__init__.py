from django.db.models.signals import post_delete, post_save

from .cache import clear_alone_cache, clear_lasting_cache, clear_statistics_cache
from .page import clear_page_cache
from .search import delete_search_index, update_search_index
from my_blog.blog.models.articles import Tag, Category, Article


def connect_signals(func, no_save=False, no_delete=False, sender=None):
    """
    connect post_save and post_delete signal
    :param no_save: 如果为True, update/create时不触发
    :param no_delete: 如果为True, delete时不触发
    :param sender: 指定需要监听的模型
    """
    kwargs = {'receiver': func}

    if sender:
        kwargs['sender'] = sender

    if not no_delete:
        post_delete.connect(**kwargs)

    if not no_save:
        post_save.connect(**kwargs)


connect_signals(clear_alone_cache)
connect_signals(clear_lasting_cache)
connect_signals(clear_statistics_cache, no_save=True)
connect_signals(clear_page_cache, no_save=True, sender=Tag)
connect_signals(clear_page_cache, no_save=True, sender=Category)
connect_signals(update_search_index, no_delete=True, sender=Article)
# connect_signals(delete_search_index, no_save=True, sender=Article) 当文章删除时不删除索引


