import pywinauto
import pyautogui
from pywinauto.keyboard import SendKeys
from pywinauto.mouse import *
# from pywinauto.keyboard import *
import time

# 1.运行360浏览器
browser_path = 'D:\\360\\360se6\\Application\\360se.exe'
kw_path = 'C:\\Users\\admin\\Desktop\\searchkw.txt'
user_page = 3
app = pywinauto.Application().start(browser_path)
# 2.打开360浏览器主窗口
mainWindow = app.window(class_name=r'360se6_Frame')
time.sleep(20)
pyautogui.moveTo(1199, 232)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'x')
pyautogui.typewrite(message='10', interval=0.5)
pyautogui.press('enter')
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX)
print(currentMouseY)
pyautogui.alert(text='This is an alert box.', title='Test')
app.kill()

