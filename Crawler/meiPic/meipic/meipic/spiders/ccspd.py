# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
import urllib.request
import re

from meipic.items import MeipicItem

class CcspdSpider(scrapy.Spider):
    name = 'ccspd'
    allowed_domains = ['meitulu.com']
    start_urls = ['https://www.meitulu.com/t/nvshen/']

    def parse(self, response):
        links = response.xpath('//ul[@class="img"]//li/a/@href').extract()
        sum = len(links)
        for i in range(0, sum):
            print("处理该页的%s/%s" %(i+1, sum))
            yield Request(links[i], callback = self.oneGirl)
        '''
        for i in range(2, 26):
            print("处理第%s页" %(i))
            url = "https://www.meitulu.com/t/nvshen/" + str(i) + ".html"
            yield Request(url, callback = self.parse)
        '''

    def oneGirl(self, response):
        item = MeipicItem()
        item['title']  = response.xpath('//h1/text()').extract()

        num = response.xpath('//div[@class="c_l"]/p/text()').extract()
        list1 = re.compile('.*?(\d+).*').findall(num[1])
        item['amount'] = list1[0]

        pat1 = '(http://mtl.ttsqgs.com/images/img/\d+/)\d.jpg'
        list1 = re.compile(pat1).findall(str(response.body))
        item['link'] = list1[0]
        
        yield item