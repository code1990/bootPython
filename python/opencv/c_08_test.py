import unittest
import cv2
import numpy as np


# 会学习这些函数：cv2.getTrackbarPos()，cv2.creatTrackbar()
class c_08_test(unittest.TestCase):
	# 通过调节滑动条来设定画板颜色
	# cv2.getTrackbarPos() 函数的
	# 第一个参数是滑动条的名字，
	# 第二个参数是滑动条被放置窗口的名字，
	# 第三个参数是滑动条的默认位置。
	# 第四个参数是滑动条的最大值，
	# 第五个函数是回调函数
	def test_81(self):
		# 8.1代码示例
		# 创建一副黑色图像
		img = np.zeros((300, 512, 3), np.uint8)
		cv2.namedWindow('image')
		cv2.createTrackbar("R", "image", 0, 255, nothing)
		cv2.createTrackbar("G", "image", 0, 255, nothing)
		cv2.createTrackbar("B", "image", 0, 255, nothing)
		switch = '0:OFF\n1:ON'
		cv2.createTrackbar(switch, "image", 0, 1, nothing)
		while (1):
			cv2.imshow("image", img)
			k = cv2.waitKey(1) & 0xFF
			if k == 27:
				break

			r = cv2.getTrackbarPos("R", "image")
			g = cv2.getTrackbarPos("G", "image")
			b = cv2.getTrackbarPos("B", "image")
			s = cv2.getTrackbarPos(switch, "image")

			if (s == 0):
				img[:] = 0
			else:
				img[:] = [b, g, r]
		cv2.destroyAllWindows()

	# 	创建一个画板，可以自选各种颜色的画笔绘画各种图 形。
	def exercise(self):
		# 当鼠标按下时变为True
		drawing = False
		# 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。
		mode = True
		ix, iy = -1, -1
		img = np.zeros((512, 512, 3), np.uint8)
		cv2.namedWindow("image")
		cv2.createTrackbar("R", 'image', 0, 255, nothing)
		cv2.createTrackbar("G", 'image', 0, 255, nothing)
		cv2.createTrackbar("B", 'image', 0, 255, nothing)
		cv2.setMouseCallback("image", self.draw_circle())
		while (1):
			cv2.imshow("image", img)
			k = cv2.waitKey(1) & 0xFF
			if k == ord('m'):
				mode = not mode
			elif k == 27:
				break
		print("11111")

	# 创建回调函数
	def draw_circle(event, x, y, flags, param, img):
		r = cv2.getTrackbarPos('R', 'image')
		g = cv2.getTrackbarPos('G', 'image')
		b = cv2.getTrackbarPos('B', 'image')
		color = (b, g, r)
		global ix, iy, drawing, mode
		# 当按下左键是返回起始位置坐标
		if event == cv2.EVENT_LBUTTONDOWN:
			drawing = True
			ix, iy = x, y
		# 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
		elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
			if drawing == True:
				if mode == True:
					cv2.rectangle(img, (ix, iy), (x, y), color, -1)
		else:
			# 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
			cv2.circle(img, (x, y), 3, color, -1)
			# 下面注释掉的代码是起始点为圆心，起点到终点为半径的
			# r=int(np.sqrt((x-ix)**2+(y-iy)**2))
			# cv2.circle(img,(x,y),r,(0,0,255),-1)
			# 当鼠标松开停止绘画。
			if event == cv2.EVENT_LBUTTONUP:
				drawing = False
		# if mode==True:
		# cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
		# else:
		# cv2.circle(img,(x,y),5,(0,0,255),-1)


def nothing():
	pass
