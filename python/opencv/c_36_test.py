import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 我们要学习ORB 算法的基础
class c_36_test(unittest.TestCase):
	def test_361(self):
		#36.1OpenCV中的ORB算法
		# ORB 基本是FAST 关键点检测和BRIEF 关键点描述器的结合体，并通
		# 过很多修改增强了性能
		# 下面是一个使用ORB 的简单代码
		img = cv2.imread('simple.jpg', 0)
		# Initiate STAR detector
		orb = cv2.ORB()
		# find the keypoints with ORB
		kp = orb.detect(img, None)
		# compute the descriptors with ORB
		kp, des = orb.compute(img, kp)
		# draw only keypoints location,not size and orientation
		img2 = cv2.drawKeypoints(img, kp, color=(0, 255, 0), flags=0)
		plt.imshow(img2), plt.show()
		print("")

