import unittest
import numpy as np
import cv2
# 使用修补技术去除老照片中小的噪音和划痕
# • 使用OpenCV 中与修补技术相关的函数
class c_50_test(unittest.TestCase):
	def test_501(self):
		#50.1基础
		img = cv2.imread('messi_2.jpg')
		mask = cv2.imread('mask2.png', 0)
		dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
		cv2.imshow('dst', dst)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("")

	def test_502(self):
		#50.2代码
		print("")

