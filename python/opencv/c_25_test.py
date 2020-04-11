import unittest
import cv2
import numpy as np
# • 理解霍夫变换的概念
# • 学习如何在一张图片中检测直线
# • 学习函数：cv2.HoughLines()，cv2.HoughLinesP()
class c_25_test(unittest.TestCase):
	def test_251(self):
		#25.1OpenCV中的霍夫变换
		# 霍夫变换在检测各种形状的的技术中非常流行，如果你要检测的形状可以
		# 用数学表达式写出，你就可以是使用霍夫变换检测它
		# cv2.HoughLines()。
		# 返回值就是（; ）。 的单位是像素， 的单位是弧度。
		# 第一个参数是一个二值化图像，所以在进行霍夫变换之前要首先进行二值化，或者进行Canny 边缘检测。
		# 第二和第三个值分别代表 和 的精确度。
		# 第四个参数是阈值，只有累加其中的值高于阈值时才被认为是一条直线，也可以把它看成能
		# 检测到的直线的最短长度（以像素点为单位）。
		img = cv2.imread('dave.jpg')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(gray, 50, 150, apertureSize=3)
		lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
		for rho, theta in lines[0]:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a * rho
			y0 = b * rho
			x1 = int(x0 + 1000 * (-b))
			y1 = int(y0 + 1000 * (a))
			x2 = int(x0 - 1000 * (-b))
			y2 = int(y0 - 1000 * (a))
			cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
		cv2.imwrite('houghlines3.jpg', img)
		print("")

	def test_252(self):
		#25.2ProbabilisticHoughTransform
		# Probabilistic_Hough_Transform 是对霍夫变换的一种优化。它
		# 不会对每一个点都进行计算，而是从一幅图像中随机选取（是不是也可以使用
		# 图像金字塔呢？）一个点集进行计算，对于直线检测来说这已经足够了。但是
		# 使用这种变换我们必须要降低阈值
		img = cv2.imread('dave.jpg')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(gray, 50, 150, apertureSize=3)
		minLineLength = 100
		maxLineGap = 10
		lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
		for x1, y1, x2, y2 in lines[0]:
			cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
		cv2.imwrite('houghlines5.jpg', img)
		print("")

