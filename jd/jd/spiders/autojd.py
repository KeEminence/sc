# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
from scrapy.http import Request
import json


class AutojdSpider(scrapy.Spider):
    name = 'autojd'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E5%A5%B3%E7%AB%A5%E7%83%AD%E8%A3%A4&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page=1&s=1&click=0']
    #https://search.jd.com/Search?keyword=%E5%A5%B3%E7%AB%A5%E7%83%AD%E8%A3%A4&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page=1&s=1&click=0

    def parse(self, response):
        item=JdItem() 
        item['link']=response.xpath("//div[@class='p-name p-name-type-2']/a/@href").extract()
        # print(item['link'])
        #    for url in item['link']:
        #        yield Request(url,callback=self.parsePic)
        yield Request(item['link'][0],callback=self.parsePic)    

    def parsePic(self,response):
        item1=JdItem() 
        item1['scr']=response.xpath("/html/head/script[@charset='gbk']").extract()
        print(item1['scr'])