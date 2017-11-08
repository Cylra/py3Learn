#! /usr/bin/env python3 

from selenium import webdriver
import getpass
import time

print('请输入登录QQ号')
qq = input()
print('请输入密码')
qq_pwd = getpass.getpass()
print('请输入要访问的QQ')
qq_other = input()

if '' == qq:
    qq = '287168219'
if '' == qq_other:
    qq_other = '448207454'

#采用系统默认的firefox配置文件夹
fp = webdriver.FirefoxProfile(profile_directory='/home/long/.mozilla/firefox/bz3hsn56.default')
driver=webdriver.Firefox(firefox_profile=fp)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://qzone.qq.com')

driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()

#driver.refresh()
driver.find_element_by_xpath(".//*[@id='u']").clear()
driver.find_element_by_xpath(".//*[@id='u']").send_keys(qq)
driver.find_element_by_xpath(".//*[@id='p']").clear()
driver.find_element_by_xpath(".//*[@id='p']").send_keys(qq_pwd)
driver.find_element_by_xpath(".//*[@id='login_button']").click()
time.sleep(8)

'''
#注释掉点击过程,直接访问某人相册主页
driver.find_element_by_css_selector('#aMyFriends>span').click()
driver.find_element_by_css_selector('#friend_search_input').clear()
driver.find_element_by_css_selector('#friend_search_input').send_keys('goddess')
driver.find_element_by_css_selector('.name.ellipsis').click()
driver.switch_to.window(driver.window_handles[-1])

quser = driver.current_url
driver.get(quser+ "/4")
'''

basic = 'https://user.qzone.qq.com/#/4'
url = basic.replace('#', qq_other)
driver.refresh()
driver.get(url)

driver.switch_to.frame('tphoto')
driver.find_elements_by_css_selector('.js-cover-img')[1].click()
#需要滚动
driver.switch_to.parent_frame()
js='window.scrollTo(0, 10000);'
driver.execute_script(js)
driver.switch_to.frame('tphoto')
time.sleep(3)

list1 = driver.find_elements_by_css_selector('.j-pl-photoitem-img')
for u in list1:
    print(u.get_attribute('src'))