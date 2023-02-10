import logging

from jieba.analyse import ChineseAnalyzer
from whoosh import fields
from whoosh.qparser import MultifieldParser

from cache.alone import ArticleInfo, ArticleDetail
from . import init_ix, get_ix

INDEX_NAME = 'article_index'
# 自定义分析器
analyzer = ChineseAnalyzer()

logger = logging.getLogger()


class ArticleSchema(fields.SchemaClass):
    """
    文章索引类
    只提供搜索返回的article_id
    """
    article_id = fields.ID(unique=True, stored=True)
    title = fields.TEXT(stored=False, analyzer=analyzer)
    content = fields.TEXT(stored=False, analyzer=analyzer)
    digest = fields.TEXT(stored=False, analyzer=analyzer)


def __add_document(writer, queryset, update=False):
    """
    添加索引文档
    :return:
    """
    for query in queryset:
        pk = query['article_id']
        content = ArticleDetail().get(pk)

        if update:
            # 更新/新增
            writer.update_document(article_id=str(pk), title=query['title'], content=content, digest=query['digest'])
            continue

        writer.add_document(article_id=str(pk), title=query['title'], content=content, digest=query['digest'])

    writer.commit()


def reset(pk=None):
    """
    重置文章索引数据
    :return:
    """
    update = False

    if pk:
        # 更新单个
        assert pk,  ValueError('pk is None')
        query = ArticleInfo().get(pk)
        assert query, ValueError('queryset is Null')

        queryset = [query]
        try:
            writer = get_ix(indexname=INDEX_NAME).writer()
            update = True
        except Exception as e:
            logger.error((e, 'No search index created'))
            # 更新全部
            queryset = ArticleInfo.get_all()
            writer = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()

    else:
        # 更新全部
        queryset = ArticleInfo.get_all()
        writer = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()

    __add_document(writer, queryset, update=update)

    return writer


def remove(pk):
    """
    删除索引文档
    :return:
    """

    writer = get_ix(indexname=INDEX_NAME)

    writer.delete_by_term('article_id', str(pk))


def search(text, pagenum=1, pagelen=10):
    """
    搜索文章数据
    :param pagenum: 当前页数
    :param pagelen: 每页的数量长度
    :return: list() 文章数据
    """
    try:
        ix = get_ix(INDEX_NAME)
    except Exception as e:
        ix = reset()
        logger.warning(e, "No search index created")

    with ix.searcher() as searcher:

        query = MultifieldParser(["title", 'content', 'digest'], ix.schema).parse(text)
        # todo不能获取总页数，当前页数大于总页数时，获取的是当前页数 可以手机设置一个假的总页数
        results = searcher.search_page(query, pagenum=int(pagenum), pagelen=int(pagelen))

        return [result['article_id'] for result in results]


# 设计索引更新时期
#  当article update -> 信号机制更新索引 ok
#            delete -> 不删除, 显示文章不存在 ok
#  是否需要定时更新索引 -> aps定时 ok
#  手动更新索引 -> 自定义manage.py 命令 ok


# """
# whoosh.fields.ID
#     ID只能为一个单元值，不能分割为若干个词，常用于文件路径、URL、日期、分类、文章作者；
# whoosh.fields.IDLIST
#     为包含由空格和/或标点分隔的ID的字段
#     stored -- 此字段的值是否与文档一起存储。
#     unique -- 此字段的值对于每个文档是否唯一。
#     expression -- 用于提取标记的正则表达式对象。默认表达式将中断CRS、LFS、制表符、空格、逗号和分号上的标记。
# whoosh.fields.STORED
#     为要存储但不是索引的字段配置的字段类型
# whoosh.fields.KEYWORD
#     为包含空格分隔或逗号分隔的关键字（如标记）数据的字段配置的字段类型
#     stored -- 此字段的值是否与文档一起存储。
#     commas -- 是否为逗号分隔字段。如果该值为假（默认值），则将其视为一个空格分隔的字段。
#     scorable -- 此字段是否可记分
# whoosh.fields.TEXT
#     为文本字段（例如文章正文）配置的字段类型
#     stored -- 此字段的值是否与文档一起存储。
#     analyzer -- 分析器
# whoosh.fields.DATETIME
#     用于为日期时间对象编制索引的特殊字段类型
#     此字段基于python的datetime模块
#     stored -- 此字段的值是否与文档一起存储。
#     unique -- 此字段的值对于每个文档是否唯一
# whoosh.fields.BOOLEAN
#     允许为布尔值（true和false）编制索引的特殊字段类型
#     stored -- 此字段的值是否与文档一起存储
#
# 删除
#     delete_document(docnum)方法 (docnum是索引查询结果的每条结果记录的docnum属性)
#     delete_by_term(field_name, termtext)方法 （特别适合删除ID,或KEYWORD字段）
#     delete_by_query(query)
# """