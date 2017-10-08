import requests
from bs4 import BeautifulSoup
import os
import re


links=[]
with open("sites", "r") as f:
    for line in f.readlines():
        links.append(line.strip())

for url in links:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    folderName = soup.h1.string
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    cur = os.getcwd()
    os.chdir(folderName)

    with open("README", "w") as f:
        f.write(url)

    for link in soup.find_all('p'):
        str1 = str(link.string)
        if (str1.startswith("图片数量")):
            total = re.search(r"\d+",str1).group()
            break
    for link in soup.find_all('center'):
        if(link.img):
            basePicUrl = link.contents[0]['src']

    prefix = os.path.dirname(basePicUrl)
    file = os.path.basename(basePicUrl)
    print("共有%s张" %(total))
    for i in range(1, int(total) + 1):
        fileName = re.sub(r'\d', str(i), file)
        if os.path.exists(fileName):
            continue
        fileUrl = prefix + '/'+ fileName
        print(fileUrl)
        r = requests.get(fileUrl)
        with open(fileName, 'wb') as f:
            f.write(r.content)


    os.chdir(cur)
