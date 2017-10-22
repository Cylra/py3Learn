# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request

class QtpjtPipeline(object):
    def process_item(self, item, spider):
        #一个图片列表页中有多张图片,通过循环依次存储到本地
        for j in range(0, len(item['picurl'])):
            thispic = item['picurl'][j]
            trueurl = thispic + '_1024.jpg'
            #需要提前建立pic文件夹
            localpath = "./pic/" + item['picname'][j] + '.jpg'
            #将图片保存在本地
            urllib.request.urlretrieve(trueurl, filename = localpath)
        return item