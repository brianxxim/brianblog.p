from haystack import indexes

from .models.articles import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """
    文章索引模型类(已废弃)
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """
        返回需要建立索引的模型类
        """
        return Article

    def index_queryset(self, using=None):
        """
        返回要建立索引的数据查询集
        """
        # 不允许values()
        # return self.get_model().objects.values('article_id', 'title', 'digest', 'content', 'category', 'author', 'tag').filter(is_delete=False)
        return self.get_model().objects.filter(is_delete=False)

# 模型类对应ES中的Types表？
# 模型类的每个字段对应于ES中Types表的Filed？
# document=Truer, haystack会把这个字段当成主要搜索字段
# use_template=True, 说明需要在templates/search/indexes/应用名/模型名_text.txt中设置搜索时索引的数据库模型对象
# 生成初始索引 python manage.py rebuild_index