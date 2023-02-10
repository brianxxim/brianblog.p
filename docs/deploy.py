#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ### 已废弃@cheng ###
import os
import re
import sys
import time


def implement_cmd(cmd):
    """
    执行命令
    :param cmd: 需要执行的命令
    :return: None表示执行成功, int表示错误
    """
    p = os.popen(cmd)
    msg = p.readlines()
    if len(msg) > 0:
        print(msg)
    return p.close()


def input_cmd(msg: str):
    """
    监听指令
    :param msg: 提示信息
    :return: 用户的输入指令
    """
    exits = ['exit', 'quit', 'exit()']
    cmd = input(msg)
    if cmd in exits:
        exit()

    return cmd


class InstallBase(object):
    """
    安装程序的基类
    """
    name = str("程序名称")
    commands = {"指令名称": "指令"}

    @classmethod
    def install(cls, is_check=True):
        """
        安装程序方法
        :param is_check: 是否一键安装, 不需要确认
        :return:
        """

        print("2s后开始安装{}".format(cls.name))
        for x in range(2):  # 美化作用
            for y in range(10):
                print('* ', end='')
                time.sleep(0.1)
            print('')

        for command in cls.commands.values():
            ret = implement_cmd(command)
            if ret and is_check:
                time.sleep(0.1)
                if input("是否需要继续？(Y/n)").lower() == 'n':
                    return
        print("{}安装完成".format(cls.name))


class InstallDocker(InstallBase):
    """
    安装docker
    """
    name = "Docker"
    commands = {
        'install': "curl -sSL https://get.daocloud.io/docker | sh",
        'start': "sudo systemctl start docker"
    }


class InstallES(InstallBase):
    """
    安装Elasticsearch
    """
    name = 'Elasticsearch'
    commands = {
        'install': "docker pull elasticsearch",
        'start': 'docker run -d --name es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e '
                 '"ES_JAVA_OPTS=-Xms512m -Xmx512m" elasticsearch:7.1.1 /bin/bash',
        'enter_container': 'docker exec -it es /bin/bash',
        'install_ik': '/usr/share/elasticsearch/bin/elasticsearch-plugin install '
                      'https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.1.1/elasticsearch'
                      '-analysis-ik-7.1.1.zip',
        'exit_container': 'exit',
        'restart': 'docker restart es',
    }


class InstallRedis(InstallBase):
    """
    安装Redis
    """
    name = "Redis"
    commands = {
        'install': 'docker pull redis:latest',
        'start': 'docker run -itd --name redis -p 6379:6379 redis',
    }


class InstallMySQL(InstallBase):
    """
    安装mysql
    """
    name = "Mysql"
    commands = {
        'install': 'docker pull mysql:latest',
        'start': "docker run -itd --name mysql -p 3306:3306 -e 'MYSQL_ROOT_PASSWORD={}' mysql",
    }

    @classmethod
    def install(cls, is_check=True):
        if not is_check:
            cls.commands['start'] = cls.commands['start'].format('123456')
        else:
            cls.commands['start'] = cls.commands['start'].format(input_cmd('({})请设置root密码: '.format(cls.name)))
        super().install(is_check)


class InstallWhole(InstallBase):
    """
    安装全部程序
    """
    name = "全部安装"
    commands = None

    @classmethod
    def install(cls, is_check=True):
        InstallDocker.install(is_check)
        InstallES.install(is_check)
        InstallRedis.install(is_check)
        InstallMySQL.install(is_check)


def main(functions):
    """
    菜单
    :return:
    """
    # 初始化
    menu = dict()

    for function in functions:
        menu[functions.index(function)] = function.name

    # 菜单
    while True:
        print("输入需要安装的程序：")
        for num, msg in menu.items():
            print("{}. {}".format(num, msg))

        input_command = input_cmd(">> ")

        # 监听命令
        for i in range(3):
            if not re.match(r'^[0-{}]$'.format(len(functions)), input_command):
                input_command = input_cmd("输入错误, 请重新输入: ")
                continue

            functions[int(input_command)].install()
            break

        time.sleep(2)


if __name__ == '__main__':
    if sys.argv.pop() != 'auto':
        functions = [InstallWhole, InstallDocker, InstallES, InstallRedis, InstallMySQL]
        main(functions)
    else:
        InstallWhole.install(is_check=False)
