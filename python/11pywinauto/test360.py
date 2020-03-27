'''启动360浏览器'''
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import os

__browser_url="D:\\360\\360se6\\Application\\360se.exe"
# __browser_url="C:\\Users\\THINK\\AppData\\Local\\360Chrome\\Chrome\\Application\\360chrome.exe"
chrome_options=Options()
# 设置好应用扩展
# extension_path = 'C:\\Users\\admin\\Desktop\\LinkRun.crx'
# chrome_options.add_extension(extension_path)
chrome_options.binary_location=__browser_url
driver=webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\\driver\\chromedriver78.exe')
# dr=webdriver.Chrome()
driver.get('https://www.baidu.com/')