#! /usr/bin/python3
import urllib.request
import urllib.parse

url = "http://yum.iqianyue.com/mypost/"
#将数据使用urlencode编码后,使用encode()设置为utf-8
postdata = urllib.parse.urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode("utf-8")

req = urllib.request.Request(url, postdata)
req.add_header("User-Agent",  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
           Chrome/61.0.3163.100 Safari/537.36")
data = urllib.request.urlopen(req).read()

with open("6.html", "wb") as f:
    f.write(data)