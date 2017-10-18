#! /usr/bin/python3

import urllib.request
import http.cookiejar

url = "http://news.163.com/"
#以字典的形式设置headers
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", \
           "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0", \
           "Connection": "keep-alive", \
           "referer": "http://www.163.com/"}
#设置cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http': "127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
#添加请求头部信息
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
#将opener安装为全局
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()

with open("1.html", "wb") as f:
    f.write(data)