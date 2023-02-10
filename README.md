**Demo演示**: [brianblog.bsia](https://brianblog.asia)

# 部署说明

**部署环境** 

* Ubuntu20.04TLS

* MySQL 8.*

* Redis 7.*

* Python3.8

  

**命令**

* 更新索引: python manage.py reset_whoosh
* 启动redis: redis-server /etc/redis/redis.conf
* 启动supervisord: supervisord -c /etc/supervisord.conf



**第三方API**

* 新闻api: https://www.jisuapi.com/my/
* 评论api: https://changyan.kuaizhan.com/v3/changyan/overview


# 缓存

## 一级缓存 -> 本地内存

缓存内容

* 视图
  * 首页
  * 关于
  * 归档
  * 链接
  * 留言
* 全局上下文

## 二级缓存 --> Redis

缓存内容

* 0号库 持久/统计存储  caches
* 0号库 单独缓存 cache
* 1号库 news

缓存系统

* 持久缓存

  | key                  | 类型   | py类型       | 说明                   | 存储字段                  |
  | -------------------- | ------ | ------------ | ---------------------- | ------------------------- |
  | home: link:all       | string | list(dict()) | 友情链接               | link_id, name, title, url |
  | home:notice:all      | string | list(dict()) | 滚动消息               | notice_id, content        |
  | art:category:all     | string | list()       | 所有分类               | [cid1, cid2...]           |
  | art:tag:all          | string | list()       | 所有标签               | [tid1, tid2...]           |
  | art:recommend:all  X | string |              | 所有推荐X              | [article_id, ..]          |
  | home:news:all        | set    |              | 新闻(随机获取指定个数) |                           |
  
* 单独缓存

  | key                    | 类型   | py类型 | 说明     | 存储字段                                                 |      |
  | ---------------------- | ------ | ------ | -------- | -------------------------------------------------------- | ---- |
  | home:slideshow:{sid}   | string | dict   | 轮播图   | slideshow_id, title, image, url, biref                   |      |
  | art:category:{cid}     | string | dict   | 分类信息 | category_id, name                                        |      |
  | art:tag:{tid}          | string | dict   | 标签信息 | tag_id, name                                             |      |
  | art:{aid}:tags         | string | list   | 文章标签 | [tag1, tag2]                                             |      |
  | art:art/:{art_id}:info | string | dict   | 文章信息 | article_id, title, cover, digest, category_id, author_id |      |
  | art:{art_id}:detail    | string | string | 文章内容 | content                                                  |      |
  | author:{uid}           | string |        | 作者     | id, username                                             |      |

* 统计

  | key                | 类型 | 说明         | 举例                  |
  | ------------------ | ---- | ------------ | --------------------- |
  | count: art:read    | zset | 阅读量       | [art_id, count]       |
  | count: art:comment | zset | 评论量       | [art_id, count]       |
  | art:create:time    | zset | 文章创建时间 | [art_id, create_time] |

* 分页
* 其它 ....未完持续

**缓存更新**

* 通过djagno signals 从数据库更新

* aps定时更新

* 新闻-> API更新



## 其它缓存

**搜索**

1. 文章更新 -> 更新单个索引
2. 文章创建 -> 更新单个索引
3. 文章删除 -> 不更新索引

文章删除时不更新索引，使用aps定时更新全部索引

重置索引 `python manage.py reset_whoosh`



**分页**

使用缓存保存分页器。分页器只保存文章ID。文章删除时不删除分页，只等待分页缓存过期

1. 文章更新 -> 不删除缓存
2. 文章删除 -> 不删除缓存
3. 标签/分类 更新 -> 不删除缓存
4. 标签/分类 删除 -> 删除缓存

**评论**

评论功能对接畅言云评

https://changyan.kuaizhan.com/v3/changyan/overview

* aps定时从畅言云评更新评论数
