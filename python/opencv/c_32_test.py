import unittest
# • 学习SIFT 算法的概念
# • 学习在图像中查找SIFT 关键点和描述符
import cv2
import numpy as np
from matplotlib import pyplot as plt
class c_32_test(unittest.TestCase):
	def test_131(self):
		# 现在来计算关键点描述符，OpenCV 提供了两种方法。
		# 1. 由于我们已经找到了关键点，我们可以使用函数sift.compute() 来计
		# 算这些关键点的描述符。例如：kp; des = sift:compute(gray; kp)。
		# 2. 如果还没有找到关键点，可以使用函数sift.detectAndCompute()
		# 一步到位直接找到关键点并计算出其描述符。
		#看看OpenCV 中关于SIFT 的函数吧。让我们从关键点检
		# 测和绘制开始吧
		img = cv2.imread('home.jpg')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		sift = cv2.SIFT()
		# sift.detect() 可以在图像中找到关键
		kp = sift.detect(gray, None)
		img = cv2.drawKeypoints(gray, kp)
		cv2.imwrite('sift_keypoints.jpg', img)
		# OpenCV 也提供了绘制关键点的函数：cv2.drawKeyPoints()，它可以
		# 在关键点的部位绘制一个小圆圈。如果你设置参数为cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_就会绘制代表关键点大小的圆圈甚至可以绘制除关键点的方向。
		img = cv2.drawKeypoints(gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		cv2.imwrite('sift_keypoints.jpg', img)
		print("")

