import pywinauto
import pyautogui
from pywinauto.keyboard import SendKeys
from pywinauto.mouse import *
# from pywinauto.keyboard import *
import time
#1.运行360浏览器
browser_path = 'D:\\360\\360se6\\Application\\360se.exe'
user_page = 373
app = pywinauto.Application().start(browser_path)
#2.打开360浏览器主窗口
mainWindow = app.window(class_name=r'360se6_Frame')
time.sleep(10)
print("配置https://www.linkedin.com/feed/为360主页")
# print("鼠标点击领跑插件>>>>>")
# pyautogui.moveTo(935, 44)
# pyautogui.click()
# time.sleep(12)
# print("鼠标点击关闭360主页>>>>>")
# pyautogui.moveTo(279, 12)
# pyautogui.click()
time.sleep(3)
# print("鼠标移动到屏幕中间>>>>>")
# pyautogui.moveTo(300, 200)
# time.sleep(10)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX)
# print(currentMouseY)
print("鼠标点击关闭领英帮助界面>>>>>")
pyautogui.moveTo(1211, 286)
pyautogui.click()
time.sleep(3)
print("点击人脉菜单>>>>>")
pyautogui.moveTo(1167, 158)
pyautogui.click()
# time.sleep(3)
print("移动到input输入框，点击输入框获取输入状态>>>>>")
pyautogui.moveTo(930, 187)
pyautogui.click()
# time.sleep(3)
print("请务必保持英文输入法状态>>>>>")
print("模拟键盘输入文字>>>>>")
#模拟输入信息
pyautogui.typewrite(message='bolts inc',interval=0.5)
pyautogui.press('enter')
time.sleep(10)
# 鼠标左击一次
# pyautogui.click()
# time.sleep(3)

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX)
# print(currentMouseY)
# print("鼠标点击搜索按钮>>>>>")
# pyautogui.moveTo(1230, 185)
# pyautogui.click()
# time.sleep(3)
print("鼠标点击多选选择框>>>>>")
pyautogui.moveTo(935, 227)
pyautogui.click()
# time.sleep(3)
# print("鼠标点击添加按钮>>>>>")
# pyautogui.moveTo(1060, 229)
# pyautogui.click()
# # time.sleep(3)
# print("鼠标移动到文本输入框>>>>>")
# pyautogui.moveTo(932, 274)
# pyautogui.click()
# print("全选删除文本输入框>>>>>")
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.hotkey('ctrl', 'x')
# pyautogui.click()
# time.sleep(3)
# print("鼠标点击发送按钮>>>>>")
# pyautogui.moveTo(1220, 422)
# pyautogui.click()
# time.sleep(10*28)
print("鼠标点击下一页>>>>>")
pyautogui.moveTo(1231, 227)
pyautogui.click()
time.sleep(20)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX)
print(currentMouseY)
pyautogui.alert(text='This is an alert box.', title='Test')
# app.kill()
# #4.点击新弹出窗体的确定按钮
# out_note=u'关于记事本'
# button_name_ok='确定'
# app[out_note][button_name_ok].click()
# #5.查看一个窗体含有的控件，子窗体，菜单
# print(app[title_notepad].print_control_identifiers())
# #-------------------无标题记事本的含有的控件，子窗体，菜单-----------------
# # Control Identifiers:
# #
# # Notepad - '无标题 - 记事本'    (L8, T439, R892, B815)
# # ['无标题 - 记事本Notepad', 'Notepad', '无标题 - 记事本']
# # child_window(title="无标题 - 记事本", class_name="Notepad")
# #    |
# #    | Edit - ''    (L16, T490, R884, B807)
# #    | ['无标题 - 记事本Edit', 'Edit']
# #    | child_window(class_name="Edit")
# #    |
# #    | StatusBar - ''    (L16, T785, R884, B807)
# #    | ['StatusBar', '无标题 - 记事本StatusBar', 'StatusBar   第 1 行，第 1 列']
# #    | child_window(class_name="msctls_statusbar32")
# # None
#
# #6.在记事本中输入一些文本
# #[tips-> ctrl+点击鼠标左键快速查看被调用函数]
# app.title_notepad.Edit.type_keys('pywinauto works!\n',with_spaces=True,with_newlines=True)
# app.title_notepad.Edit.type_keys('hello word !\n',with_spaces=True,with_newlines=True)
# #7.选择编辑菜单->编辑时间/日期
# # app[title_notepad].menu_select('编辑->时间/日期(&d)')
# #8.连接已运行程序
# #如连接微信 借助spy++找到运行程序的handle
# app1=pywinauto.Application(backend='uia').connect(handle=0x00320830)
# #9.查看运行窗口窗体名称
# print(app1.window())
# print(app1['Dialog'].print_control_identifiers())
# # Dialog - '微信'    (L968, T269, R1678, B903)
# # ['微信Dialog', 'Dialog', '微信']
# # child_window(title="微信", control_type="Window")
# #    |
# #    | Pane - 'ChatContactMenu'    (L-10000, T-10000, R-9999, B-9999)
# #    | ['ChatContactMenu', 'ChatContactMenuPane', 'Pane', 'Pane0', 'Pane1']
# #    | child_window(title="ChatContactMenu", control_type="Pane")
# #    |    |
# #    |    | Pane - ''    (L-10019, T-10019, R-9980, B-9980)
# #    |    | ['', 'Pane2', '0', '1']
# #    |
# #    | Pane - ''    (L948, T249, R1698, B923)
# #    | ['2', 'Pane3']
# # None
# #10.通过路径去打开一个已有程序
# #11.鼠标控制
# x=0
# y=0
# for i in range(20):
#     step_x = i*8
#     step_y = i*5
#     move(coords=(step_x,step_y ))
#     time.sleep(1)
#
# #12.键盘控制
# #键盘对应的ascii http://www.baike.com/wiki/ASCII
# #发送键盘指令,打开命令行，输入一条命令for /l %i in (1,1,100) do tree
# SendKeys('{VK_LWIN}')
# SendKeys('cmd')
# SendKeys('{VK_RETURN}')
# time.sleep(3)
# SendKeys('for /L +5i in +9 1,1,100+0 do tree {VK_RETURN}',with_spaces=True)