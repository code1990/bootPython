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
		print("11111")

def nothing():
	pass
