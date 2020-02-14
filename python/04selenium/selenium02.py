# selenium定位方法
# Selenium提供了8种定位方式。
#
# id
# name
# class name
# tag name
# link text
# partial link text
# xpath
# css selector
# 这8种定位方式在Python selenium中所对应的方法为：
#
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')

driver.get('https://www.baidu.com')

print(driver.find_element_by_id("su").get_attribute("value"))

driver.quit()