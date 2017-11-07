#! /usr/bin/env python3

from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = "file://" + os.path.abspath('checkbox.html')
driver.get(file_path)

checkboxs = driver.find_elements_by_css_selector('input[type="checkbox"]')
for checkbox in checkboxs:
    checkbox.click()
    time.sleep(1)

print(len(checkboxs))

driver.find_elements_by_css_selector('input[type="checkbox"]').pop().click()

driver.quit()