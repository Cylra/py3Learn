#! /usr/bin/python3
import urllib.request

keywd = "hello"
url = "http://www.baidu.com/s?wd="

req = urllib.request.Request(url + keywd)
data = urllib.request.urlopen(req).read()

with open("4.html", "wb") as f:
    f.write(data)


key = "老师"
key_code = urllib.request.quote(key)
req = urllib.request.Request(url + key_code)
data = urllib.request.urlopen(req).read()

with open("5.html", "wb") as f:
    f.write(data)