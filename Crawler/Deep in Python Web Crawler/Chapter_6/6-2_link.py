#! /usr/bin/python3

import urllib.request
import re

def getLink(url):
    headers = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    html1 = urllib.request.urlopen(url)
    data = str(html1.read())

    #构建获取链接的正则表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    links = re.compile(pat).findall(data)
    #print(links)
    #去除重复元素
    links = list(set(links))
    return links

#要爬取的网页链接
url = "http://blog.csdn.net/"
linkList = getLink(url)
for link in linkList:
    print(link[0])