from django.db import models


class BaseModel(models.Model):
    """
    ORM模型基类
    """
    create_time = models.DateTimeField(auto_now_add=True, null=False, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=False, verbose_name='更新时间')

    class Meta:
        abstract = True
        # managed = False
