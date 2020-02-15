# （十八）窗口截图
# WebDriver提供了截图函数get_screenshot_as_file()来截取当前窗口。

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("D:\\baidu_img.jpg")

driver.quit()
# 脚本运行完成后打开D盘，就可以找到baidu_img.jpg图片文件了。