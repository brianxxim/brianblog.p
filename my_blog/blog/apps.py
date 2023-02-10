from logging import getLogger

from django.apps import AppConfig

from . import constants

logger = getLogger('django')


class BlogConfig(AppConfig):
    name = 'my_blog.blog'

    def ready(self):
        """
        此方法用于django初始化后初始化自己的数据
        """
        # 注册信号接收器
        # from . import signals
        from . import signal

        # 开启定时任务
        from schedulers import scheduler
        scheduler.start()

        # 初始化表数据
        from django.db import DatabaseError
        from django.contrib.auth.models import Group

        try:
            for group in constants.INIT_USER_GROUPS:
                if not Group.objects.filter(name=group):
                    Group.objects.create(name=group)
        except DatabaseError as e:
            logger.error(e)
