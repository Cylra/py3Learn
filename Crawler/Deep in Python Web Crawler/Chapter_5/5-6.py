#! /usr/bin/python3

import urllib.request
import urllib.parse

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LL3Mj"
postdata = urllib.parse.urlencode({
    "username": "weisuen",
    "password": "aA123456"
}).encode("utf-8")
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
               like Gecko) Chrome/61.0.3163.100 Safari/537.36")
data = urllib.request.urlopen(req).read()

with open("1.html", "wb") as f:
    f.write(data)

url2 = "http://bbs.chinaunix.net/"
req2 = urllib.request.Request(url2, postdata)
req2.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
               like Gecko) Chrome/61.0.3163.100 Safari/537.36")
data2 = urllib.request.urlopen(req2).read()

with open("2.html", "wb") as f:
    f.write(data2)