# 控制浏览器操作
# 控制浏览器窗口大小
# WebDriver提供了set_window_size()方法来设置浏览器的大小。
# 控制浏览器后退、前进
# WebDriver也提供了对应的back()和forward()方法来模拟后退和前进按钮。
# 刷新页面
# 有时候需要手动刷新（F5） 页面
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
# 设置数字为像素点
print("设置浏览器的宽高")
driver.set_window_size(480,800)

print("访问百度首页")
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

print("访问新闻页面")
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

print("返回（后退）到百度首页")
print("back to  %s "%(first_url))
driver.back()

#前进到新闻页
print("forward to  %s"%(second_url))
driver.forward()

driver.refresh() #刷新当前页面

driver.quit()