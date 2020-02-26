# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
from scrapy.http import Request
import json
import re


class AutojdSpider(scrapy.Spider):
    name = 'autojd'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&wq=%E5%A5%B3%E5%AD%A9%E8%B6%85%E7%9F%AD%E8%A3%A4&pvid=c1352e6c483c424ab70e5802fb43d07f']

    def parse(self, response):
        item=JdItem() 
        item['link']=response.xpath("//div[@class='p-name p-name-type-2']/a/@href").extract()
        # print(item['link'])
        for url in item['link']:
            yield Request('https://'+url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'},callback=self.parselink)

        for i in range(1,2):
            url1='https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%A5%B3%E5%AD%A9%E8%B6%85%E7%9F%AD%E8%A3%A4&page='+str(i)+'&s=61&click=0'
            yield Request(url1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'},callback=self.parse)    

    def parselink(self,response):
        urlmo1=re.compile(r'desc: \'(\S+)\'')
        item1=JdItem() 
        item1['scr']=response.xpath("/html/head/script[@charset='gbk']").extract()[0]
        b=urlmo1.findall(str(item1['scr']))
        yield Request('https://'+b[0],headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'},callback=self.parsePic)    

    def parsePic(self,response):
        item2=JdItem() 
        # print(response.body)
        urlmo2=re.compile(r'data-lazyload=\\\\"(\S+)\\\\"')
        item2['pic']=urlmo2.findall(str(response.body))
        yield item2
        # print(c)

