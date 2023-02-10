from django.conf import settings as django_settings

import json
from datetime import datetime
from logging import getLogger
from . import constants

import gevent.monkey
gevent.monkey.patch_all(thread=False)
import requests


logger = getLogger('django')


def __get_config():
    """
    获取新闻API配置
    :return:
    """
    api = 'https://api.jisuapi.com/news/get'
    appkeys = ["560499d1136123b6",
               "4391b24cd8c2fb30"]

    try:
        api = django_settings.NEWS_API
        appkeys = django_settings.NEWS_APPKEYS

    except Exception as e:
        logger.warning(e, 'No setting NEW_API')

    return {
        'api': api,
        'appkeys': appkeys
    }


def __request_news(config: __get_config(), channel, count=None):
    """
    请求新闻数据
    :param channel: 请求频道
    :param count: 请求条数
    :return: list news
    """
    news_list = list()
    content = None

    for appkey in config.get('appkeys'):
        response = requests.post(config['api'], verify=False, data={
            "channel": channel,
            "num": count,
            "appkey": appkey
        })

        if response.status_code != 200:
            raise Exception('New API appkey invalid! appkey: {}, status_code: {}'.format(appkey, response.status_code))

        content = json.loads(response.content.decode())
        break

    # for appkey in config.get('appkeys'):
    #     try:
    #         response = requests.post(config['api'], verify=False, data={
    #             "channel": channel,
    #             "num": count,
    #             "appkey": appkey
    #         })
    #
    #         if response.status_code != 200:
    #             raise Exception('New API appkey invalid! appkey: {}, status_code: {}'.format(appkey, response.status_code))
    #
    #         content = json.loads(response.content.decode())
    #         break
    #     except Exception as e:
    #         logger.error(e, 'Request news api error')

    if content['status'] == '104':
        return news_list

    for news in content['result']['list']:
        news_list.append({
            'title': news['title'],  # 标题
            # 'time': news['time'],  # 发表时间
            'channel': channel,  # 新闻所属分类
            'src': news['src'],  # 新闻机构名称
            'url': news['url']  # 新闻链接
        })

    return news_list


def get_news(channels=None, count=None) -> list:
    """
    获取新闻数据
    :param channels: 新闻频道列表
    :param count: 每个频道获取条数
    :return: channels, news_list
    """

    channels = channels or constants.NEWS_CHANNELS
    count = count or constants.GET_NEWS_COUNT
    config = __get_config()

    for channel in channels:
        news_list = __request_news(config, channel, count)
        yield channel, news_list


class News:
    """
    缓存存储单例(已废弃)
    要求:
        只存在一个对象
        同一天内, 仅get_news一次
    """

    def __new__(cls, *args, **kwargs):
        # 只创建一次对象, 并获取初始化数据
        if not hasattr(cls, "_instance"):
            # 创建对象
            obj = super().__new__(cls, *args, **kwargs)
            obj._news = None
            # 将对象赋值给类属性_instance
            cls._instance = obj
        return cls._instance

    def get_news(self):
        # 非同一天重新获取数据
        if not hasattr(self, '_day') or self._day != datetime.now().day:
            self._day = datetime.now().day
            self._news = get_news()
        return self._news


if __name__ == '__main__':
    ret = get_news()
    print(ret)