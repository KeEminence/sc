# -*- coding:utf-8 -*-

import scrapy
from firstpro.items import FirstproItem

class testSpider(scrapy.Spider):
    name='test'
    allowed_domains=['sina.com.cn']
    start_urls=[
        'https://ent.sina.com.cn/star/',
        'http://slide.ent.sina.com.cn/star/slide_4_704_333594.html?cre=picpc&mod=picg&loc=2&r=0&rfunc=63&tj=none#p=1',
        'https://sports.sina.com.cn/basketball/nba/2020-02-13/doc-iimxyqvz2519544.shtml',
    ]

    def __init__(self,myurl,*args,**kwargs):
        super(testSpider,self).__init__(*args,**kwargs)
        print('要爬取的网址为：%s'%myurl)
        self.start_urls=['%s'%myurl]

    def parse(self,response):
        item=FirstproItem()
        item['urlname']=response.xpath('/html/head/title/text()')
        print(item['urlname'])

# http://blog.sina.com.cn/rss/1615888477.xml

