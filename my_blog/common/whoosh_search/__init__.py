import os

from whoosh.index import open_dir

# 索引数据存放的根目录
# DATA_BASE_DIR = os.path.join(os.path.dirname(__file__))
DATA_BASE_DIR = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), 'data')


def init_ix(schema, indexname, dirname=None):
    """
    初始化索引
    :param dirname: 索引存放目录
    :param schema: 索引模型对象
    :param indexname: 索引名
    :return: FileIndex.writer
    """
    data_path = os.path.join(DATA_BASE_DIR, dirname) if dirname else DATA_BASE_DIR
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    from whoosh.index import create_in
    ix = create_in(data_path, schema, indexname=indexname)

    return ix


def get_ix(indexname: str, dirname=None):
    """
    打开
    :param indexname: 索引名
    :param dirname: 索引存放路径
    :return:
    """
    data_path = os.path.join(DATA_BASE_DIR, dirname) if dirname else DATA_BASE_DIR

    ix = open_dir(data_path, indexname=indexname)
    return ix
