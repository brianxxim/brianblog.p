import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class UsernameMobileModelBackend(ModelBackend):
    """自定义登陆认证"""

    def authenticate(self, request, password=None, **kwargs):
        """
        认证登陆凭证。允许使用email或username登陆
        :param kwargs: 用户名或者邮箱
        :return: user
        """
        account = kwargs.get('username')
        user_query = get_user_model().objects.filter(is_active=True)

        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", account):
            # 邮箱登陆
            user = user_query.filter(email=account).first()
        else:
            # 用户名登陆
            user = user_query.filter(username=account).first()

        if user:
            # 认证密码
            if user.check_password(password):
                return user
