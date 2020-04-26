import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 学习不同的形态学操作，例如腐蚀，膨胀，开运算，闭运算等
# • 我们要学习的函数有：cv2.erode()，cv2.dilate()，cv2.morphologyEx()
# 形态学操作是根据图像形状进行的简单操作。一般情况下对二值化图像进
# 行的操作。需要输入两个参数，一个是原始图像，第二个被称为结构化元素或
# 核，它是用来决定操作的性质的。两个基本的形态学操作是腐蚀和膨胀。他们
# 的变体构成了开运算，闭运算，梯度等
class c_17_test(unittest.TestCase):
	def test_171(self):
		# 17.1腐蚀
		# 这个操作会把前景物体的边界腐蚀掉
		# 卷积核沿着图像滑动，如果与卷积核对应的原图
		# 像的所有像素值都是1，那么中心元素就保持原来的像素值，否则就变为零
		img = cv2.imread("python.png", 0)
		kernel = np.ones((5, 5), np.uint8)
		erosion = cv2.erode(img,kernel,iterations=1)

	def test_172(self):
		# 17.2膨胀
		# 与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1，中心元
		# 素的像素值就是1
		# 一般在去噪声时先用腐蚀再用膨胀
		img = cv2.imread("python.png", 0)
		kernel = np.ones((5, 5), np.uint8)
		dilation = cv2.dilate(img, kernel, iterations=1)

	def test_173(self):
		# 17.3开运算
		# 先进性腐蚀再进行膨胀就叫做开运算
		img = cv2.imread("python.png", 0)
		kernel = np.ones((5, 5), np.uint8)
		opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

	def test_174(self):
		# 17.4闭运算
		# 先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的
		# 小黑点。
		img = cv2.imread("python.png", 0)
		kernel = np.ones((5, 5), np.uint8)
		closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

	def test_175(self):
		# 17.5形态学梯度
		# 其实就是一幅图像膨胀与腐蚀的差别。
		# 结果看上去就像前景物体的轮廓。
		img = cv2.imread("python.png", 0)
		kernel = np.ones((5, 5), np.uint8)
		gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

	def test_176(self):
		# 17.6礼帽
		# 原始图像与进行开运算之后得到的图像的差。下面的例子是用一个9x9 的
		# 核进行礼帽操作的结果。
		img = cv2.imread("python.png", 0)
		kernel = np.ones((9, 9), np.uint8)
		tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

	def test_177(self):
		# 17.7黑帽
		# 进行闭运算之后得到的图像与原始图像的差。
		img = cv2.imread("python.png", 0)
		kernel = np.ones((9, 9), np.uint8)
		blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

	def test_178(self):
		# 17.8形态学操作之间的关系
		# 我们使用Numpy 构建了结构化元素，它是正方形的。但
		# 有时我们需要构建一个椭圆形/圆形的核。为了实现这种要求，提供了OpenCV
		# 函数cv2.getStructuringElement()。你只需要告诉他你需要的核的形状
		# 和大小。
		# Rectangular Kernel
		print(cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
		# Elliptical Kernel
		print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
		# Cross-shaped Kernel
		print(cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)))

