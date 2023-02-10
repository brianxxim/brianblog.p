from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModel


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='名称')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        managed = False
        db_table = 'art_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(BaseModel):
    category_id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(unique=True, max_length=20, verbose_name='名称')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        # managed表示是否需要迁移数据库
        managed = False
        db_table = 'art_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    article_id = models.BigAutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=128, verbose_name='标题')
    cover = models.ImageField(default='art_default.jpg', verbose_name='封面')
    # digest = RichTextField(config_name='digest', verbose_name='摘要')
    digest = models.CharField(max_length=300, verbose_name='摘要')
    content = RichTextUploadingField(config_name='default', verbose_name='内容')
    read_count = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    comment_count = models.PositiveIntegerField(default=0, verbose_name='评论量')
    category = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True, verbose_name='分类')
    author = models.ForeignKey(get_user_model(), models.PROTECT, default=1, verbose_name='作者')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    is_delete = models.BooleanField(default=False, verbose_name='禁止')

    class Meta:
        managed = False
        db_table = 'art_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Recommend(models.Model):
    recommend_id = models.AutoField(primary_key=True, verbose_name='ID')
    article = models.ForeignKey(Article, models.CASCADE, verbose_name='推荐文章')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        managed = False
        db_table = 'art_recommend'
        verbose_name = '推荐文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class ArtArticleTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, models.DO_NOTHING)
    tag = models.ForeignKey(Tag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'art_article_tag'


