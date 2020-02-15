# （十二）多窗口切换
# WebDriver提供了switch_to.window()方法，可以实现在不同的窗口之间切换。
# 以百度首页和百度注册页为例，在两个窗口之间的切换如下图。

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
print(all_handles)
# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("account").send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)
        # ……

driver.quit()
