# from whoosh.index import create_in
# from whoosh.fields import *
#
# # 构建索引
# schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
# ix = create_in("indexdir", schema)
# writer = ix.writer()
# writer.add_document(title=u"First document", path=u"/a",content=u"This is the first document we've added!")
# writer.add_document(title=u"Second document", path=u"/b", content=u"The second one is even more interesting!")
# writer.commit()
#
# # 搜索
# from whoosh.qparser import QueryParser
# with ix.searcher() as searcher:
#     query = QueryParser("content", ix.schema).parse("first")
#     results = searcher.search(query)
#     print(results[0])


def a(**kwargs):
    try:
            raise Exception('aaa')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    a()
