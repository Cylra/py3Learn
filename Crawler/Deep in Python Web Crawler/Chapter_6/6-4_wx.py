#! /usr/bin/python3

import urllib.request
import re

key = '呵呵'
key_code = urllib.request.quote(key)
url = "http://weixin.sogou.com/weixin?type=2&s_from=input&query="
req = urllib.request.Request(url + key_code)
data = urllib.request.urlopen(req).read()
pat1 = '<ul class="news-list">.*</ul>'
str1 = re.compile(pat1).findall(str(data))

pat2 = 'a target="_blank" href="(http://mp.weixin.qq.com/[^ "]*)'
linkList = re.compile(pat2).findall(str1[0])
linkList = list(set(linkList))

i = 101
for url in linkList:
    url = url.replace("&amp;", "&")
    oneWeb = urllib.request.urlopen(url).read()
    with open(str(i) + ".html", "wb") as f:
        f.write(oneWeb)
    i += 1