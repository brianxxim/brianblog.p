from datetime import datetime

from django.conf import settings
from redis.exceptions import RedisError

from my_blog.blog.models import articles
from my_blog.blog.models.homes import Slideshow
from my_blog.blog.models.users import User
from . import CacheBase, constants, logger
from .statistics import ArticleCreateTime, ArticleReadCount, ArticleCommentCount


class SlideshowInfo(constants.SlideshowInfoTTL, CacheBase):
    """
    所有轮播图缓存
    """
    key = 'home:slideshow:{}'
    model = Slideshow

    def db_query(self):
        """
        重置缓存
        此方法需要从数据库中查询并处理成需要的数据
        :return: 需要的数据
        """
        query = self.model.objects.values('slideshow_id', 'title', 'image', 'url', 'brief').filter(is_delete=False, slideshow_id=self.instance_id).first()

        if query is not None:
            query['image'] = settings.QINIU_BASE_URL + query['image']

        return query


class CategoryInfo(constants.CategoryInfoTTL, CacheBase):
    """
    文章类别信息缓存
    """
    key = 'art:category:{}'
    model = articles.Category

    def db_query(self):
        """
        需要保存的查询集
        """
        return self.model.objects.values('category_id', 'name').filter(is_delete=False, category_id=self.instance_id).first()


class TagInfo(constants.TagInfoTTL, CacheBase):
    """
    文章标签信息缓存
    """
    key = 'art:tag:{}'
    model = articles.Tag

    def db_query(self):
        return self.model.objects.values('tag_id', 'name').filter(is_delete=False, tag_id=self.instance_id).first()


class ArticleTag(constants.ArticleTagTTL, CacheBase):
    """
    文章标签缓存
    """

    key = 'art:{}:tags'
    model = articles.ArtArticleTag

    def db_query(self):
        """
        从数据库中查询需要的数据
        :return: cache_data
        """
        queryset = self.model.objects.values('tag_id').filter(article_id=self.instance_id)

        if queryset:
            return [query['tag_id'] for query in queryset]

    def get(self, pk=None):
        cache = super(ArticleTag, self).get(pk)
        if cache is None:
            return []

        return cache


class ArticleInfo(constants.ArticleInfoTTL, CacheBase):
    """
    文章基本信息缓存
    """
    key = 'art:{}:info'
    model = articles.Article

    def db_query(self):
        """
        重置缓存
        此方法需要从数据库中查询并处理成需要的数据
        :return: 需要的数据
        """
        query = self.model.objects.values('article_id', 'title', 'cover', 'digest', 'category_id', 'author_id') \
            .filter(is_delete=False, article_id=self.instance_id).first()

        if query is not None:
            query['cover'] = settings.QINIU_BASE_URL + query['cover']

        return query

    @classmethod
    def _get_relation_data(cls, cache, pk=None):
        """
        获取关联数据
        :param cache: 缓存数据
        :param pk: 请求获取的id
        :return: 添加关联后的缓存数据
        """
        if not cache:
            return {'article_id': pk}

        pk = cache['article_id']

        timestamp = ArticleCreateTime.get(pk)
        cache['create_time'] = datetime.fromtimestamp(timestamp)
        cache['category'] = CategoryInfo(cache['category_id']).get()
        cache['author'] = AuthorInfo(cache['author_id']).get()

        cache['comment_count'] = ArticleCommentCount.get(pk)
        cache['read_count'] = ArticleReadCount.get(pk)

        return cache

    @classmethod
    def mget_by_relation(cls, pks: list):
        """
        批量获取文章基本信息和关联数据
        """
        caches = cls.mget(pks)
        new_caches = []

        # for cache, pk in dict(zip(caches, pks)).items(): # python不支持dict的key为list或dict类型
        for pk, cache in dict(zip(pks, caches)).items():

            try:
                new_caches.append(cls._get_relation_data(cache, pk))
            except RedisError as e:
                logger.error(e, 'get_by_relation error cache: {}'.format(cache))

        return new_caches

    def get_by_relation(self, pk):
        """
       获取文章基本信息和关联数据
        """
        if not pk:
            return

        cache = self.get(pk)

        return self._get_relation_data(cache, pk) if cache else None

    @classmethod
    def get_all(cls):
        """
        获取所有数据
        :return:
        """
        queryset = cls.model.objects.values('article_id').filter(is_delete=False)
        return cls.mget_by_relation([query['article_id'] for query in queryset])


class ArticleDetail(constants.ArticleDetailTTL, CacheBase):
    """
    文章详情内容
    """
    key = 'art:{}:detail'
    model = articles.Article

    def db_query(self):
        """
        重置缓存
        此方法需要从数据库中查询并处理成需要的数据
        :return: 需要的数据
        """
        query = self.model.objects.values('content').filter(is_delete=False, article_id=self.instance_id).first()

        if query:
            return query['content']

        return query


class AuthorInfo(constants.AuthorInfoTTL, CacheBase):
    """
    作者信息缓存
    """
    model = User
    key = 'author:{}'

    def db_query(self):
        return self.model.objects.values('id', 'username').filter(is_active=True, id=self.instance_id).first()
