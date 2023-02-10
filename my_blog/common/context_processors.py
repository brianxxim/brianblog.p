from django.conf import settings

from cache.wholes import AllNotice, AllCategory
from cache.alone import CategoryInfo, ArticleInfo, TagInfo
from cache.wholes import AllLink, AllTag
from cache.statistics import ArticleReadCount
from cache.news import AllNewsCache

from . import constants


def global_variable(request):
    """
    base.html全局上下文
    """
    # BOSS
    boss = settings.BOSS

    # 流动消息
    notices = AllNotice.all()

    # 文章分类
    pks = AllCategory.all()
    categories = CategoryInfo.mget(pks)

    # 文章排行
    pk_reads = ArticleReadCount.get_top(constants.RANK_ARTICLE_SHOW_COUNT, score=True)

    pks = [pt['pk'] for pt in pk_reads]
    art_ranks = ArticleInfo.mget(pks)

    for index in range(len(art_ranks)):
        art_ranks[index]['read_count'] = pk_reads[index]['score']

    # 标签云
    pks = AllTag.all()
    tags = TagInfo.mget(pks)

    # 友情链接
    links = AllLink.all()

    # 新闻
    news = AllNewsCache.mget(constants.GET_NEWS_COUNT)
    return {
        'notices': notices,
        'categories': categories,
        'tags': tags,
        'links': links,
        'news': news,
        'art_ranks': art_ranks,
        'BOSS': boss
    }
