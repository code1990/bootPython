# （九）设置元素等待

# WebDriver提供了两种类型的等待：显式等待和隐式等待。

# WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：
#
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.ID, "kw"))
)
element.send_keys('selenium')
driver.quit()

# WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')

# 设置隐式等待为10秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
