# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ccxml.items import CcxmlItem

class CcxmlspiderSpider(XMLFeedSpider):
    name = 'ccxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    
    #将开始迭代的节点设置为第一个节点rss
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        i = CcxmlItem()
        #利用XPath表达式将信息提取出来,存储到对应的item中
        i['title'] = selector.xpath('/rss/channel/item/title/text()').extract()
        i['link']  = selector.xpath('/rss/channel/item/link/text()').extract()
        i['author']= selector.xpath('/rss/channel/item/author/text()').extract()
        
        for j in range(len(i['title'])):
            print("第%s篇文章" %(j+1))
            print("标题是:")
            print(i['title'][j])
            print("对应链接是:")
            print(i['link'][j])
            print("对应作者是:")
            print(i['author'][j])
            print("----------------------------")

        return i