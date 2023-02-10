import os
import re
from re import search


def kill_process(keyword,):
    """停止django程序(python manage.py runserver)"""
    cmd = "ps -aux | grep \"{}\"".format(keyword)
    # 执行命令
    ps_result = os.popen(cmd)

    while True:
        # 获取一行结果
        line_result = ps_result.readline()

        # 没有结果或结果是ps命令
        if not line_result or re.search("\sgrep\s", line_result):
            break

        # 匹配是否是manage.py
        s = search("\d+.*{}".format(keyword), line_result)
        if s is None:
            continue

        # 拿到pid
        s = search("^\d+", s.group())
        if s is None:
            continue

        # 杀死
        os.system("kill -9 {}".format(s.group()))


if __name__ == '__main__':
    manage_py_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "manage.py")
    process_keyword = "{} runserver".format(manage_py_path)
    kill_process(process_keyword)
