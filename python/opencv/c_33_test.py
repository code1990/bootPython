import unittest
# • SUFR 的基础是什么？
# • OpenCV 中的SURF加速稳健特征
import cv2
import numpy as np
from matplotlib import pyplot as plt
class c_33_test(unittest.TestCase):
	def test_331(self):
		#33.1OpenCV中的SURF
		# 首先我们要初
		# 始化一个SURF 对象，同时设置好可选参数：64/128 维描述符，Upright/
		# Normal 模式等
		img = cv2.imread('fly.png', 0)
		surf = cv2.SURF(400)
		kp, des = surf.detectAndCompute(img, None)
		surf.hessianThreshold = 50000
		kp, des = surf.detectAndCompute(img, None)
		img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
		plt.imshow(img2), plt.show()
		print("")

