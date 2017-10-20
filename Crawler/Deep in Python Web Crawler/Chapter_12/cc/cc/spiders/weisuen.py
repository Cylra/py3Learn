# -*- coding: utf-8 -*-
import scrapy
from cc.items import CcItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/c/nd/2017-10-19/doc-ifymzqpq2219041.shtml', \
                  'http://slide.mil.news.sina.com.cn/h/slide_8_198_57340.html#p=1', \
                  'http://slide.news.sina.com.cn/s/slide_1_2841_103185.html']
    
    #定义了新属性urls2
    urls2 = ('http://www.jd.com', 'http://sina.com.cn', 'http://yum.iqianyue.com')
    #重写了start_requests()方法,不从start_urls读取网址
    def start_requests(self):
        #将起始网址设置为从新属性urls2中读取
        for url in self.urls2:
            #调用默认的make_requests_from_url()方法生成具体请求并通过yield返回
            yield self.make_requests_from_url(url)
            
    #命令行传网址参数
    def __init__(self, myurl=None, *args, **kwargs):
        super(WeisuenSpider, self).__init__(*args, **kwargs)
        print("要爬取的网址为: %s" %myurl)
        self.start_urls = ['%s' %myurl]

    def parse(self, response):
        item = CcItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print(item['urlname'])