# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from cccwpjt.items import CccwpjtItem

class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = CccwpjtItem()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        return i
