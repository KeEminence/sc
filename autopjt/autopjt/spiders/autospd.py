# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


#http://category.dangdang.com/pg1-cp01.45.56.01.00.00.html

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cp01.45.56.01.00.00.html']

    def parse(self, response):
        item=AutopjtItem()
        item['name']=response.xpath("//a[@class='pic']/@title").extract()
        item['price']=response.xpath("//span[@class='search_now_price']/text()").extract()
        item['link']=response.xpath("//a[@class='pic']/@href").extract()
        item['comnum']=response.xpath("//a[@class='itemlist-review']/text()").extract()

        # print(item['price'])
        yield item  #这里回返回item值给引擎，后续可能交给pipeline处理之类的。返回值之后，继续向下执行代码，因为整个函数相当于一个生成器，引擎会继续向下执行代码。

        for i in range(1,5):
            url="http://category.dangdang.com/pg"+str(i)+"-cp01.45.56.01.00.00.html"
            # print(url)
            yield Request(url,callback=self.parse)  #此处生成返回request，并把这个request交给引擎处理（引入url队列操作等），完成操作后，继续向下执行代码，直到循环结束（此处回调应该为异步回调，不会阻塞进程）。结束后会生成4个url，它们都在队列里面，送去给下载器下载，返回response后回调parse函数，继续解析动作。scrapy引擎会屏蔽相同的url，即当发现有url重合的时候会不再继续爬取该url，但是第一个url重合并不会屏蔽，此时才触发屏蔽功能。
        # print('done')
