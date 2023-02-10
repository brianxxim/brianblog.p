from my_blog.blog.models.articles import Category, Tag
from my_blog.blog.models.homes import Link, Notice
from . import constants
from . import CachesBase


class AllLink(constants.AllLinkTTL, CachesBase):
    """
    所有友情链接
    """
    key = 'home:link:all'
    model = Link
    ttl = constants.AllLinkTTL

    @classmethod
    def save_dataset(cls):
        """
        Get the link cached ata query set
        :return:
        """
        return cls.model.objects.values('link_id', 'name', 'title', 'url').filter(is_delete=False).all()


class AllNotice(constants.AllNotice, CachesBase):
    """
    所有滚动消息缓存
    """
    model = Notice
    key = 'home:notice:all'

    @classmethod
    def save_dataset(cls):
        """
        Get the notice cache data query set
        :return: query set
        """
        return cls.model.objects.values('notice_id', 'content').filter(is_delete=False)


class AllCategory(constants.AllCategoryTTL, CachesBase):
    """
    所有分类ID
    """
    model = Category
    key = 'art:category:all'

    @classmethod
    def save_dataset(cls):
        queryset = cls.model.objects.values('category_id').filter(is_delete=False).all()
        return [query['category_id'] for query in queryset]


class AllTag(constants.AllTagTTL, CachesBase):
    """
    所有标签ID
    """
    model = Tag
    key = 'art:tag:all'

    @classmethod
    def save_dataset(cls):
        queryset = cls.model.objects.values('tag_id').filter(is_delete=False).all()

        return [query['tag_id'] for query in queryset]


# class AllRecommendArticle(constants.AllRecommendArticleTTL, CachesBase):
#     """
#     推荐文章缓存(已废弃)
#     """
#     key = 'art:recommend:all'
#     model = Recommend
#
#     @classmethod
#     def save_dataset(cls):
#         queryset = cls.model.objects.values('article_id').filter(is_delete=False).all()
#         dataset = [query['article_id'] for query in queryset]
#
#         return dataset
