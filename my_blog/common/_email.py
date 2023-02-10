import datetime
from logging import getLogger
from smtplib import SMTPException

from django.template.loader import get_template
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail

from encryption import generate_jwt
# 找不到父级包
#   common作为导包路径，common内的文件就是根路径包, 它没有父包
# from . import constants

logger = getLogger('django')


def send_activation_email(user, ip):
    """
    发送激活用户链接
    :return:
    """
    web_name = settings.BOSS.WEB_NAME
    domain_name = settings.BOSS.DOMAIN_NAME
    now_date = datetime.datetime.today()

    # 生成链接
    expire = now_date + datetime.timedelta(hours=settings.USER_ACTIVATION_EXPIRE_SECONDS)
    token = generate_jwt({'id': user.id, 'email': user.email}, expire)
    url = 'http://{}{}?token={}'.format(domain_name, reverse('blog:activation'), token)

    # 渲染邮件内容
    message = get_template('email/register.html').render({
        'web_name': web_name,
        'domain_name': domain_name,
        'now_date': now_date,
        'ip': ip,
        'url': url,
    })

    # 发送
    try:
        send_mail(subject=web_name,
                  message='',
                  html_message=message,
                  recipient_list=[user.email],
                  from_email=None,
                  fail_silently=False,
                  )
    except SMTPException as e:
        logger.warning(e, '注册发送邮件失败! 用户: {}-{}, ip: {}'.format(user.id, user.username, ip))
        return False

    return True


def send_repasswd_email(user, ip):
    """
    发送找回密码链接
    :return:
    """
    web_name = settings.BOSS.WEB_NAME
    domain_name = settings.BOSS.DOMAIN_NAME
    now_date = datetime.datetime.today()

    # 生成链接
    expire = now_date + datetime.timedelta(hours=settings.USER_REPASSWD_EXPIRE_SECONDS)
    token = generate_jwt({'id': user.id, 'email': user.email}, expire)
    url = 'http://{}{}?token={}'.format(domain_name, reverse('blog:repasswd'), token)

    # 发送
    try:
        send_mail(subject=web_name,
                  message=f'请通过以下链接登陆您的后台并修改密码\n'
                          f'{url}\n'
                          f'您的ip: {ip}',
                  recipient_list=[user.email],
                  from_email=None,
                  fail_silently=False,
                  )
    except SMTPException as e:
        logger.warning(e, '找回密码发送邮件失败! 用户: {}-{}, ip: {}'.format(user.id, user.username, ip))
        return False

    return True
