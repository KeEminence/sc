#coding=utf8

import urllib.request
import io
import sys
import re


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def getcontent(url):
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

    data=urllib.request.urlopen(url).read().decode('gb2312')
    print(data)

url='https://weibo.com/zhangzimu?is_hot=1#_rnd1581427836766'
getcontent(url)

