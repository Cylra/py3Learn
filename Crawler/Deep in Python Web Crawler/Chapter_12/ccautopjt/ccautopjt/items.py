# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcautopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name  = scrapy.Field()
    price = scrapy.Field()
    link  = scrapy.Field()
    #商品评论数
    comnum= scrapy.Field()