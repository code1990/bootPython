import pywinauto
import pyautogui
import time
# 本地先安装360浏览器 安装领跑插件 并且登录完成 可以保证后面可以免密登录
# 本地运行 请设置360浏览器安装位置
# 配置 配置https://www.linkedin.com/feed/为360主页
# 设置 人脉搜索关键字的位置
# 1.运行360浏览器
browser_path = 'D:\\360\\360se6\\Application\\360se.exe'
kw_path = 'C:\\Users\\admin\\Desktop\\searchkw.txt'
user_page = 3
app = pywinauto.Application().start(browser_path)
# 2.打开360浏览器主窗口
mainWindow = app.window(class_name=r'360se6_Frame')
time.sleep(10)
# print("鼠标点击领跑插件>>>>>")
# pyautogui.moveTo(935, 44)
# pyautogui.click()
# time.sleep(12)
# time.sleep(6)
print("鼠标移动到屏幕中间>>>>>")
pyautogui.moveTo(673, 5)
time.sleep(10)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX)
# print(currentMouseY)
print("鼠标点击关闭领英帮助界面>>>>>")
pyautogui.moveTo(1211, 286)
pyautogui.click()
time.sleep(6)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX)
# print(currentMouseY)
# pyautogui.alert(text='This is an alert box.', title='Test')
# # app.kill()
print("点击人脉菜单>>>>>")
pyautogui.moveTo(1167, 158)
pyautogui.click()
pyautogui.click()
time.sleep(3)
print("请务必保持英文输入法状态>>>>>")
print("模拟键盘输入文字>>>>>")
f2 = open(kw_path, "r")
lines = f2.readlines()
print(type(lines))
for index in range(len(lines)):
    kw = lines[index]
    print(kw, end='')
    # 模拟输入信息
    pyautogui.typewrite(message=kw, interval=0.5)
    pyautogui.press('enter')
    time.sleep(3)
    for i in range(user_page):
        time.sleep(3)
        print("当前页面是>>>>>", i + 1)
        print("鼠标点击多选选择框>>>>>")
        pyautogui.moveTo(935, 227)
        pyautogui.click()
        time.sleep(3)
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
        # pyautogui.click()55
        # time.sleep(10*28)
        # print("鼠标点击下一页>>>>>")
        # pyautogui.moveTo(1231, 227)
        # pyautogui.click()
        pyautogui.moveTo(1182, 231)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'x')
        page = str(i + 2)
        pyautogui.typewrite(message=page, interval=0.5)
        pyautogui.press('enter')
        time.sleep(5)
        # currentMouseX, currentMouseY = pyautogui.position()
        # print(currentMouseX)
        # print(currentMouseY)
    if (index != user_page - 1):
        pyautogui.moveTo(1167, 158)
        pyautogui.click()
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

# pyautogui.alert(text='This is an alert box.', title='Test')
print("关闭360浏览器")
app.kill()
