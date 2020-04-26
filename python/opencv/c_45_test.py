import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# • 本节我们要学习为立体图像制作深度地图
class c_45_test(unittest.TestCase):
	def test_451(self):
		#45.1基础
		imgL = cv2.imread('tsukuba_l.png', 0)
		imgR = cv2.imread('tsukuba_r.png', 0)
		stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
		disparity = stereo.compute(imgL, imgR)
		plt.imshow(disparity, 'gray')
		plt.show()
		print("")

	def test_452(self):
		#45.2代码
		print("")

