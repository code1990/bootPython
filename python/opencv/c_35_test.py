import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 我们学习BRIEF 算法的基础
# BRIEF 是一种特征描述符，它不提供查找特征的方法。
# 所以我们不得不使用其他特征检测器，比如SIFT 和SURF 等
class c_35_test(unittest.TestCase):
	def test_351(self):
		#35.1OpenCV中的BRIEF
		img = cv2.imread('simple.jpg', 0)
		# Initiate STAR detector
		star = cv2.FeatureDetector_create("STAR")
		# Initiate BRIEF extractor
		brief = cv2.DescriptorExtractor_create("BRIEF")
		# find the keypoints with STAR
		kp = star.detect(img, None)
		# compute the descriptors with BRIEF
		kp, des = brief.compute(img, kp)
		# 函数brief:getInt(′bytes′) 会以字节格式给出nd 的大小，默认值为32
		print(brief.getInt('bytes'))
		print(des.shape)
		print("")

