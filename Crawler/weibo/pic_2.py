#! /usr/bin/env python3

from selenium import webdriver
import time
import getpass
from pymongo import MongoClient
import re
import datetime

pwd = getpass.getpass("请输入微博密码: ")
driver = webdriver.Firefox()
client = MongoClient('localhost', 27017)
db = client.test
collection = db.weibo

def login():
    driver.get("http://weibo.com")
    driver.implicitly_wait(10)
    time.sleep(8)
    driver.find_element_by_css_selector('input[id="loginname"]').clear()
    driver.find_element_by_css_selector('input[id="loginname"]').send_keys("lllyu@3g.sina.cn")

    driver.find_element_by_css_selector('[name="password"]').clear()
    driver.find_element_by_css_selector('[name="password"]').send_keys(pwd)

#通过Ta的微博主页识别用户名和ID,转入微博配图页面
def user_homepage(url_user):
    driver.get(url_user)
    user_name = driver.find_element_by_css_selector('.username').text
    print(user_name)
    ta_album = driver.find_element_by_css_selector('.tb_tab > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
    user_id = re.findall( r'100505(\d+)', ta_album.get_attribute('href') )[0]
    url_peitu = 'http://photo.weibo.com/#/talbum/index'
    url_peitu = url_peitu.replace('#', user_id)
    driver.get(url_peitu)
    return user_name,user_id

#首次处理某用户,将用户目前的微博配图信息全部记录下来,使用mongdb存储
def handle_one_user(url_user):
    user_name,user_id = user_homepage(url_user)
    #数据库已有该ID
    if collection.find( {"user_id" : user_id } ).count() > 0:
        return
    while True:
        '''不知道原因,出现了重复的图片网址,改为1页的全部获取后(检测重复),再批量插入到数据库
        已查明,是此微博的第1页最后8张图,和第2页的前8张图重复,属于微博那边的显示问题,
        暂时不对此重复做处理
        '''
        list_li = driver.find_elements_by_css_selector('.photoList > li')
        for li in list_li:
            url_pic = li.find_element_by_css_selector('img').get_attribute('src')
            url_pic = url_pic.replace("small", "large")

            date = li.find_elements_by_css_selector('p')[0].text
            #今年的日期,转换一下格式
            if len( re.findall(r'(\d*)月(\d*)日', date) ) != 0:
                year = datetime.datetime.now().year
                month, day = re.findall(r'(\d*)月(\d*)日', date)[0]
                if len(month) < 2:
                    month = '0' + month
                if len(day) < 2:
                    day = '0' + day
                date = "{}-{}-{}".format(year, month, day)

            title = li.find_elements_by_css_selector('p')[1].get_attribute('title')
            title = title.replace('\u200b', '')
            # title = title.replace('\n', '')

            dict1 = {"user_id": user_id,
                "user_name": user_name,
                "date": date,
                "title": title,
                "url": url_pic
            }
            collection.insert_one(dict1)
        try:
            #翻到下一页
            next = driver.find_element_by_link_text('下一页')
            next.click()
            time.sleep(2)
        except Exception as e:
            break

login()
print("请等待登录成功后,输入目标用户的主页网址")
url_user = input() #卡住,等待登录,顺便输入目标用户的主页网址

# url_user = ''   #调试用
handle_one_user(url_user)