from django.core.management.base import BaseCommand

from whoosh_search.article import reset


class Command(BaseCommand):
    """
    重置whoosh索引文档命令
    """
    help = "reset whoosh index document"

    # def add_arguments(self, parser):
    #     """
    #     对传入的参数进行处理
    #     :param parser: 保存参数的解析器
    #     :return:
    #     """
    #
    #     # python manage.py reset_whoosh reset
    #     # parser.add_argument(
    #     #     dest='reset',  # 参数名字
    #     #     type=str,   # 参数类型
    #     #     help='reset whoosh index document',  # 帮助信息
    #     # )

    def handle(self, *args, **options):
        """
        核心业务逻辑
        :param args:
        :param options:
        :return:
        """
        reset()
        self.stdout.write('reset whoosh index document complete!')
