from django.conf import settings

from cache.statistics import ArticleReadCount, ArticleCommentCount
from cache.news import AllNewsCache
from my_blog.blog.models.articles import Article
from logging import getLogger

logger = getLogger('django')
import gevent.monkey
gevent.monkey.patch_all(thread=False)
import requests


def reset_lasting_cache():
    """
    重置统计缓存
    """
    # ArticleReadCount.reset()
    # ArticleCommentCount.reset()
    AllNewsCache.reset()


def sync_cache():
    """
    同步缓存数据到数据库
    """
    queryset = Article.objects.values('article_id').all()

    for query in queryset:

        pk = query['article_id']

        read_count = ArticleReadCount.get(pk)
        comment_count = ArticleCommentCount.get(pk)

        Article.objects.filter(article_id=pk).update(read_count=read_count, comment_count=comment_count)


def sync_comment():
    """
    从畅言云评同步评论数量
    """
    url = 'https://changyan.sohu.com/api/2/topic/count?client_id={}&topic_source_id={}'
    queryset = Article.objects.values('article_id').all()

    pk_param = ''
    for query in queryset:
        pk_param += '{},'.format(query['article_id'])

    ret = requests.get(url.format(settings.JY_APPID, pk_param))

    if ret.status_code != 200:
        logger.error('畅言云评 - 请求文章评论数据失败，状态码: {}'.format(ret.status_code))
        return

    json_data = ret.json()

    for pk, data in json_data['result'].items():

        if data['id'] == '-1':
            # 无评论数据
            continue

        comment_count = data['comments']
        Article.objects.filter(article_id=pk).update(comment_count=comment_count)
