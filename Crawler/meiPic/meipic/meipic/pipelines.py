# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib.request

class MeipicPipeline(object):
    root = "/home/long/桌面/CC/py3Learn/Crawler/Deep in Python Web Crawler/meipic/meipic/"
    def process_item(self, item, spider):
        os.chdir(self.root)
        if not os.path.exists("pic"):
            os.mkdir("pic")
        os.chdir("pic")

        folder = item['title'][0]
        folder = folder.replace('/', ' ')
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for j in range(1, int(item['amount']) + 1):
            name = str(j) + ".jpg"
            url = item['link'] + name
            urllib.request.urlretrieve(url, filename=name)

        os.chdir(self.root)
        return item
