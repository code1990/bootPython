# （十）定位一组元素
# WebDriver还提供了8种用于定位一组元素的方法。
#
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_class_name()
# find_elements_by_tag_name()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_xpath()
# find_elements_by_css_selector()

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()