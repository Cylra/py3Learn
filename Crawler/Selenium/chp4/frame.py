#! /usr/bin/env python3

from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = "file://" + os.path.abspath('frame.html')
driver.get(file_path)

#切换到iframe(id='if')
driver.switch_to.frame('if')

driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()
time.sleep(3)

driver.quit()