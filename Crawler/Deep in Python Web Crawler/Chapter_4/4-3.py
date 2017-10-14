#! /usr/bin/python3
import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent" , "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
           Chrome/61.0.3163.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

with open("3.html", "wb") as f:
    f.write(data)