# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_data
from django.conf import settings

configs = {
    'access_key': 'Nx4WPQqzkyhFP-rm1Ww5KDQibIoRozt7OKAbgO38',
    'secret_key': '5acpxjF-w9erqZ-N2mQsxFhtENqzvQfQnUGgmfwk',
    'bucket_name': 'brianblogpro',
    'token_exists': 3600
}

try:
    configs['access_key'] = settings.QINIU_ACCESS_KEY
    configs['secret_key'] = settings.QINIU_SECRET_KEY
    configs['bucket_name'] = settings.QINIU_BUCKET_NAME
    configs['token_exists'] = settings.QINIU_TOKEN_EXISTS
except:
    pass


# 上传后保存的文件名
# key = 'my-python-logo.png'

# 构建鉴权对象
q = Auth(configs['access_key'], configs['secret_key'])


def upload_data(content, key=None):
    """
    上传二进制数据到七牛
    :param content: types 二进制内容
    :param key: string 文件名
    :return: string 文件名
    """
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(configs['bucket_name'], key, configs['token_exists'])

    ret, info = put_data(token, key, data=content)

    # assert ret['hash'] == etag_stream(content), "types content hash error"
    assert info.status_code == 200, "upload fail. response_status: {}".format(info.status_code)

    return ret['key']


def upload_file(localfile, *args, **kwargs):
    """
    上传本地文件到七牛云
    :param localfile: string 文件路径
    :return:
    """
    with open(localfile, 'rb') as f:
        return upload_data(f.read(), *args, **kwargs)


if __name__ == '__main__':
    ret = upload_file('img.png')
    print(ret)
