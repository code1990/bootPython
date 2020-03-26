import pyautogui
# 整个屏幕截图并保存
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')

im2 = pyautogui.screenshot('my_screenshot2.png')
# 屏幕查找图片位置并获取中间点
#在当前屏幕中查找指定图片(图片需要由系统截图功能截取的图)
coords = pyautogui.locateOnScreen('folder.png')
#获取定位到的图中间点坐标
x,y=pyautogui.center(coords)
#右击该坐标点
pyautogui.rightClick(x,y)
