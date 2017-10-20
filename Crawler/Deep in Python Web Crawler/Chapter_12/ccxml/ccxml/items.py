# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcxmlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #文章标题
    title = scrapy.Field()
    #链接
    link  = scrapy.Field()
    #文章作者
    author= scrapy.Field()