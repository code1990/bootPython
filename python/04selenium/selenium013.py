# （十三）警告框处理
# 使用 switch_to.alert 方法定位到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作。
#
# text：返回 alert/confirm/prompt 中的文字信息。
#
# accept()：接受现有警告框。
#
# dismiss()：解散现有警告框。
#
# send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()

driver.quit()