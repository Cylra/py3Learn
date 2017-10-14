#! /usr/bin/python3
import urllib.request

url = "http://www.baidu.com"
file = urllib.request.urlopen(url)
data = file.read()
data_line = file.readline()

print(file.info())
print(file.getcode())
print(file.geturl())


with open("1.html", "wb") as f:
    f.write(data)

ff = urllib.request.urlretrieve("http://edu.51cto.com", filename = "2.html")
urllib.request.urlcleanup()

a = urllib.request.quote("http://www.sina.com.cn")
print(a)
print(urllib.request.unquote(a))