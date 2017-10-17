#! /usr/bin/python3

import urllib.request
import urllib.error
import re
import os

def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist" class=.+<div class="page clearfix">'
    rseult1 = re.compile(pat1).findall(html1)
    rseult1 = rseult1[0]
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.*?\.jpg)">'
    imagelist = re.compile(pat2).findall(rseult1)

    cur = os.getcwd()
    if os.path.exists(str(page)):
        return
    os.mkdir(str(page))
    os.chdir(str(page))

    x = 1
    for imageurl in imagelist:
        imagename = str(x) + ".jpg"
        imageurl = "http://" + imageurl

        try:
            urllib.request.urlretrieve(imageurl, filename = imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1

    os.chdir(cur)

cur = os.getcwd()
if not os.path.exists("jd"):
    os.mkdir("jd")
os.chdir("jd")

for i in range(1, 41):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    craw(url, i)

os.chdir(cur)