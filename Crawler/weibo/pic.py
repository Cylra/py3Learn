#! /usr/bin/env python3

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://weibo.com")
driver.implicitly_wait(8)
time.sleep(8)
driver.find_element_by_css_selector('input[id="loginname"]').clear()
driver.find_element_by_css_selector('input[id="loginname"]').send_keys("username")

driver.find_element_by_css_selector('[name="password"]').clear()
driver.find_element_by_css_selector('[name="password"]').send_keys("password")


#driver.find_element_by_css_selector('input[name="verifycode"]').clear()
print("请输入验证码")
code = input() #卡住,等待登录
#driver.find_element_by_css_selector('input[name="verifycode"]').send_keys(code)

#关闭模拟鼠标点击登录
#driver.find_element_by_xpath('//a[@suda-data="key=tblog_weibologin3&value=click_sign"]').click()
#time.sleep(2)

#base = 'http://photo.weibo.com/2314546853/talbum/index#!/mode/1/page/'
base = 'http://photo.weibo.com/1896603022/talbum/index#!/mode/1/page/'
f = open("jie", "w")
for i in range(1,107):
    url = base + str(i)
    driver.get(url)
    driver.refresh()

    list1 = driver.find_elements_by_css_selector('div.m_photo_list_a > ul > li > dl > dt > a > img')
    for i in list1:
        #print(i.get_attribute('src').replace("small", "large"))
        f.write(i.get_attribute('src').replace("small", "large") + "\n")
    f.write("--------------------------------------------------\n")

f.close()