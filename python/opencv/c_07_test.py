import unittest
import cv2
import numpy as np


# 学习使用OpenCV 处理鼠标事件
# • 你将要学习的函数是：cv2.setMouseCallback()
# 鼠标事件的回调案例 不是很好
class c_07_test(unittest.TestCase):
	# 下列代码查看所有被支持的鼠标事件
	def test_71(self):
		# 7.1简单演示
		events = [i for i in dir(cv2) if 'EVENT' in i]
		print()
		# ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
		print(events)

	# 在双击过的地方绘制一个圆圈
	def test_71high(self):
		# 创建图像与窗口并将窗口与回调函数绑定
		img = np.zeros((512, 512, 3), np.uint8)
		cv2.namedWindow("image")
		cv2.setMouseCallback("image", self.draw_circle())
		while (1):
			cv2.imshow("image", img)
			if cv2.waitKey(20) & 0xFF == 27:
				break
		cv2.destroyAllWindows()

	def draw_circle(event, x, y, flags, param, img):
		if event == cv2.EVENT_MBUTTONDBLCLK:
			cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

	# 根据我	# 们选择的模式在拖动鼠标时绘制矩形或者是圆圈
	def test_72(self):
		# 7.2高级一点的示例
		print("")
		# 当鼠标按下时变为True
		drawing = False
		# 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。
		mode = True
		ix, iy = -1, -1
		img = np.zeros((512, 512, 3), np.uint8)
		cv2.namedWindow("image")
		cv2.setMouseCallback("image", self.draw_circle2())
		while (1):
			cv2.imshow("image", img)
			k = cv2.waitKey(1) & 0xFF
			if k == ord('m'):
				mode = not mode
			elif k == 27:
				break

	# 创建回调函数
	def draw_circle2(event, x, y, flags, param, img):
		global ix, iy, drawing, mode
		# 当按下左键是返回起始位置坐标
		if (event == cv2.EVENT_LBUTTONDOWN):
			drawing = True
			ix, iy = x, y
		# 	当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
		elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
			if drawing == True:
				if mode == True:
					cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
				else:
					# 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
					cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
			# 下面注释掉的代码是起始点为圆心，起点到终点为半径的
			# r=int(np.sqrt((x-ix)**2+(y-iy)**2))
			# cv2.circle(img,(x,y),r,(0,0,255),-1)
		# 当鼠标松开停止绘画
		elif event == cv2.EVENT_LBUTTONUP:
			drawing = False
