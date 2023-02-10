from random import randrange

# 尝试获取新闻次数
TRY_GET_NEWS_COUNT = 3

# 持久缓存TTLBase
DEFAULT_LASTING_TTL = 60 * 60 * 1

# 单独缓存TTLBase
DEFAULT_ALONE_TTL = 60 * 10

# 统计缓存TTLBase
DEFAULT_STATISTICS_TTL = 60 * 60 * 24

# 分页器每页显示条数
PAGER_PAGE_NUMBER = 7


class CacheTTLBase(object):
    """
    缓存TTL基类
    """
    TTL = 10
    MAX_DELTA = 10 * 60

    @classmethod
    def get_ttl(cls):
        return cls.TTL + randrange(0, cls.MAX_DELTA)


class AllLinkTTL(CacheTTLBase):
    """
    所有友情链接缓存TTL
    """
    TTL = DEFAULT_LASTING_TTL


class AllNotice(CacheTTLBase):
    """
    所有滚动消息缓存TTL
    """
    TTL = DEFAULT_LASTING_TTL


class AllCategoryTTL(CacheTTLBase):
    """
    所有文章类别缓存
    """
    TTL = DEFAULT_LASTING_TTL


class AllTagTTL(CacheTTLBase):
    """
    所有文章标签缓存TTL
    """
    TTL = DEFAULT_LASTING_TTL


class AllRecommendArticleTTL(CacheTTLBase):
    """
    所有推荐文章缓存TTL
    """
    TTL = DEFAULT_LASTING_TTL


class SlideshowInfoTTL(CacheTTLBase):
    """
    所有轮播图缓存TTL
    """
    TTL = DEFAULT_LASTING_TTL


class CategoryInfoTTL(CacheTTLBase):
    """
    文章类别信息缓存TTL
    """
    TTL = DEFAULT_ALONE_TTL


class TagInfoTTL(CacheTTLBase):
    """
    文章标签缓存TTL
    """
    TTL = DEFAULT_ALONE_TTL


class ArticleTagTTL(CacheTTLBase):
    """
    文章标签缓存TTL
    """
    TTL = DEFAULT_ALONE_TTL


class ArticleInfoTTL(CacheTTLBase):
    """
    文章信息缓存TTL
    """
    TTL = DEFAULT_ALONE_TTL


class ArticleDetailTTL(CacheTTLBase):
    TTL = DEFAULT_ALONE_TTL


class AuthorInfoTTL(CacheTTLBase):
    """
    作者信息缓存TTL
    """
    TTL = DEFAULT_ALONE_TTL


class ArticleReadCountTTL(CacheTTLBase):
    """
    文章阅读量缓存TTL
    """
    TTL = DEFAULT_STATISTICS_TTL


class ArticleCommentCountTTL(CacheTTLBase):
    """
    文章评论量缓存TTL
    """
    TTL = DEFAULT_STATISTICS_TTL


class ArticleCreateTimeTTL(CacheTTLBase):
    """
    最新文章
    """
    TTL = DEFAULT_STATISTICS_TTL


class NewsCacheTTL(CacheTTLBase):
    """
    新闻缓存TTL
    """
    TTL = DEFAULT_LASTING_TTL


class PagerCacheTTL(CacheTTLBase):
    """
    分页器缓存TTL
    """
    TTL = 60 * 60 * 12

