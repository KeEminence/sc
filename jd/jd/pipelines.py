# -*- coding: utf-8 -*-
import urllib.request

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JdPipeline(object):
    def process_item(self, item, spider):
        # return item
        for i in range(0,len(item['pic'])):
            thispic=item['pic'][i]
            picname=thispic.split('/')[-1]
            localpath="E:/sc/jd/jd/pic/"+picname
            urllib.request.urlretrieve(item['pic'][i],filename=localpath)
        return item