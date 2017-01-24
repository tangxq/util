__author__ = 'txq'
"""python3下一些常用的方法或工具类整理"""

import requests


def contentsize(url):
    """获取下载链接的文件大小,单位：kb"""
    r = requests.head(url, timeout=3.0)
    if r.is_redirect:
        r = requests.head(url=r.headers['Location'], timeout=3.0)
    size = round(r.headers['Content-Length'] / 1024, 2)
    return size
