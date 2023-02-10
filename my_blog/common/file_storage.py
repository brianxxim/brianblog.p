from django.conf import settings
from django.core.files.storage import Storage

from .utils.upload_qiniu import upload_data


class FileStorage(Storage):
    """
    自定义django文件存储类
    """
    def __init__(self, qiniu_base_url=None):
        self.base_url = qiniu_base_url or settings.QINIU_BASE_URL

    def _open(self, name, mode='rb'):
        """
        :param name: 要打开的文件的名字
        :param mode: 打开文件方式
        :return: None
        """
        # 打开文件时使用的，此时不需要 但文档说明必须写，所以pass
        pass

    def _save(self, name, content):
        """
        :param name: django生成的文件名
        :param content: 保存的文件对象
        :return string 保存到数据库的文件名
        """
        return upload_data(content.read())

    def url(self, name):
        """
        读取文件路径
        :param name: 数据库中保存的文件路径后缀
        :return: 文件完整路径
        """
        return self.base_url + name

    def exists(self, name):
        """
        文件是否已存在
        :param name:
        :return:
        """
        return False


def get_filename(filename, request):
    """
    自定义ckeditor上传文件名(已废弃)
    :param filename:
    :param request:
    :return:
    """
    return filename.upper()

