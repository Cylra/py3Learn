# -*- coding: utf-8 -*-
import scrapy
from ccautopjt.items import CcautopjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html']

    def parse(self, response):
        item = CcautopjtItem()
        item['name']  = response.xpath("//a[@class='pic']/@title").extract()
        item['price'] = response.xpath("//span[@class='price_n']/text()").extract()
        item['link']  = response.xpath("//a[@class='pic']/@href").extract()
        item['comnum']= response.xpath("//a[@name='itemlist-review']/text()").extract()
        #提取完后返回item
        yield item
        #通过循环爬取45页的数据
        for i in range(1,46):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4002203.html"
            #通过yield返回Request,并指定要爬取的网址和回调函数
            #实现自动爬取
            yield Request(url, callback = self.parse)