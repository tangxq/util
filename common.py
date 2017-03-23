__author__ = 'txq'
"""python3下一些常用的方法或工具类整理"""

import requests
import time


def contentsize(url):
    """获取下载链接的文件大小,单位：kb"""
    r = requests.head(url, timeout=3.0)
    if r.is_redirect:
        r = requests.head(url=r.headers['Location'], timeout=3.0)
    size = round(r.headers['Content-Length'] / 1024, 2)
    return size


def retry_request(url, times=3):
    """设置请求重试次数,如果请求http code!=200"""
    i = 0
    while times >= 0:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
            # break
        times -= 1
        print('重试第%d次' % i)
        i += 1

