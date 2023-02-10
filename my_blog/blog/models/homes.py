from django.db import models

from common.models import BaseModel


class Link(BaseModel):
    link_id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=20, verbose_name='名称')
    title = models.CharField(max_length=255, verbose_name='标题')
    url = models.URLField(blank=True, null=True, verbose_name='链接')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        managed = False
        db_table = 'home_link'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Slideshow(BaseModel):
    slideshow_id = models.AutoField(primary_key=True, verbose_name='ID')
    image = models.ImageField(verbose_name='图片')
    title = models.CharField(unique=True, max_length=64, blank=True, null=True, verbose_name='标题')
    brief = models.CharField(max_length=255, null=True, verbose_name='简介')
    url = models.CharField(max_length=2048, blank=True, null=True, verbose_name='链接')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        managed = False
        db_table = 'home_slideshow'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title if self.title is not None else '请输入标题'


class Notice(BaseModel):
    notice_id = models.AutoField(primary_key=True, verbose_name='ID')
    content = models.CharField(max_length=255, verbose_name='内容')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        managed = False
        db_table = 'home_notice'
        verbose_name = '流动消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
