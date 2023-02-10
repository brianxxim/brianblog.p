from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=150, verbose_name='用户名')
    # email = models.CharField(max_length=254, verbose_name='邮箱')

    # nickname = models.CharField(unique=True, default='', max_length=32, verbose_name='署名')
    # mobile = models.CharField(default='', max_length=11, verbose_name='手机号')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='手机号')

    class Meta:
        managed = True
        db_table = 'auth_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username if self.username else 'user{}'.format(self.id)

