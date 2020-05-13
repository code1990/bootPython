import pywinauto
import pyautogui
import time

# 本地先安装360浏览器 安装领跑插件 并且登录完成 可以保证后面可以免密登录
# 本地运行 请设置360浏览器安装位置
# 配置 配置https://www.linkedin.com/feed/为360主页
# 设置 人脉搜索关键字的位置
# 1.运行360浏览器
browser_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# kw_path = 'C:\\Users\\admin\\Desktop\\searchkw.txt'
# user_page = 3
app = pywinauto.Application(backend='uia').start(browser_path)
# 2.打开浏览器主窗口
# mainWindow = app.window(class_name=r'Chrome_WidgetWin_1')
# time.sleep(100)
