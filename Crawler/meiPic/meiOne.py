#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import os
import urllib.request
import urllib.error
import time

pat_title = '<h1>(.*)</h1>'
r1 = re.compile(pat_title)
pat_amount = '图片数量.*?(\d+)'
r2 = re.compile(pat_amount)
pat_picurl = 'src="(http://mtl.ttsqgs.com/images/img/\d+/)\d.jpg' #20171024 首页找不到1.jpg
r3 = re.compile(pat_picurl)

def oneGirl(url):
    req1 = requests.get(url)
    req1.encoding = 'utf-8'
    str1 = req1.text
    
    title  = r1.findall(str1)[0]
    amount = r2.findall(str1)[0]
    picurl = r3.findall(str1)[0]

    folder = title.replace('/', ' ') #替换名字中不规范的字符
    #文件夹存在,就返回
    if os.path.exists(folder):
        return

    os.mkdir(folder)
    os.chdir(folder)

    for i in range(1, int(amount) + 1):
        print("处理当前人物进度: %s/%s" %(i, amount))
        name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picurl + name, filename=name)
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                #20171023 add by cc 实际图片数量没有标示的那么多,需要处理404错误
                if 404 == int(e.code):
                    continue
            if hasattr(e, 'reason'):
                print(e.reason)
            time.sleep(30)
            urllib.request.urlretrieve(picurl + name, filename=name)
        except Exception as e:  #除了URLError,会报服务器Service Unavailable或http错误
            if hasattr(e, 'code'):
                pass
            if hasattr(e, 'reason'):
                print(e.reason)
            time.sleep(30)
            urllib.request.urlretrieve(picurl + name, filename=name)  

    urllib.request.urlcleanup()
    #返回上级目录    
    os.chdir('..')

def download(onePage):
    req1 = requests.get(onePage)
    req1.encoding = 'utf-8'
    str1 = req1.text

    pat1 = '\s<a href="(https://www.meitulu.com/item/\d+.html)'
    onePageUrls = re.compile(pat1).findall(str1)
    #print(onePageUrls)

    sum = len(onePageUrls)
    for i in range(sum):
        print('处理当前页进度: %s/%s' %(i+1, sum))
        oneGirl(onePageUrls[i])
        time.sleep(1)

if not os.path.exists('pic'):
    os.mkdir('pic')
os.chdir('pic')

basic = 'https://www.meitulu.com/t/nvshen/'
pageFolder = 'page_'
for i in range(7, 26):
    if 1 == i:
        page = basic
    else:
        page = basic + str(i) + '.html'
    print('在下载第%s页' %(i))

    folder = pageFolder + str(i)
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    download(page)

    os.chdir("..")

os.chdir("..")