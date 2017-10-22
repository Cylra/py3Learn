# -*- coding: utf-8 -*-
import scrapy
from qtpjt.items import QtpjtItem
from scrapy.http import Request
import re

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0.html']

    def parse(self, response):
        item = QtpjtItem()
        #http://pic.qiantucdn.com/58pic/26/60/72/82G58PICmgP.jpg!qtwebp290
        paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
        item['picurl'] = re.compile(paturl).findall(str(response.body))
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item['picname'] = re.compile(patlocal).findall(str(response.body))
        yield item

        for i in range(2,3):
            #构造出下一页图片列表页的网址
            nexturl = "http://www.58pic.com/piccate/3-0-0-" + str(i) + ".html"
            yield Request(nexturl, callback=self.parse)