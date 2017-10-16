#! /usr/bin/python3

import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LL3Mj"
postdata = urllib.parse.urlencode({
    "username": "weisuen",
    "password": "aA123456"
}).encode("utf-8")
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
               like Gecko) Chrome/61.0.3163.100 Safari/537.36")
#创建CookieJar对象
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()

with open("3.html", "wb") as f:
    f.write(data)

url2 = "http://bbs.chinaunix.net/"
data2 = urllib.request.urlopen(url2).read()

with open("4.html", "wb") as f:
    f.write(data2)