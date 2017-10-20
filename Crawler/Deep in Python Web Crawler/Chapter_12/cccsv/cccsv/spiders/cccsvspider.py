# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from cccsv.items import CccsvItem

class CccsvspiderSpider(CSVFeedSpider):
    name = 'cccsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    #定义headers
    headers = ['name', 'sex', 'addr', 'email']
    #定义间隔符
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = CccsvItem()
        i['name'] = row['name']
        i['sex'] = row['sex']
        print("名字是:")
        print(i['name'])
        print("性别是:")
        print(i['sex'])
        print("-------------------------")
        return i
