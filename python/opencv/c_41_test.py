import unittest
import numpy as np
import cv2
# 本节我们将要学习OpenCV 中的背景减除方法
class c_41_test(unittest.TestCase):
	def test_411(self):
		#41.1基础
		print("")

	def test_412(self):
		#41.2BackgroundSubtractorMOG
		# 这是一个以混合高斯模型为基础的前景/背景分割算法
		cap = cv2.VideoCapture(0)
		fgbg = cv2.createBackgroundSubtractorMOG()
		while (1):
			ret, frame = cap.read()
			fgmask = fgbg.apply(frame)
			cv2.imshow('frame', fgmask)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break
		cap.release()
		cv2.destroyAllWindows()
		print("")

	def test_413(self):
		#41.3BackgroundSubtractorMOG2
		# 这个也是以高斯混合模型为基础的背景/前景分割算法
		cap = cv2.VideoCapture('vtest.avi')
		fgbg = cv2.createBackgroundSubtractorMOG2()
		while (1):
			ret, frame = cap.read()
			fgmask = fgbg.apply(frame)
			cv2.imshow('frame', fgmask)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break
		cap.release()
		cv2.destroyAllWindows()
		print("")

	def test_414(self):
		#41.4BackgroundSubtractorGMG
		# 此算法结合了静态背景图像估计和每个像素的贝叶斯分割
		cap = cv2.VideoCapture('vtest.avi')
		kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
		fgbg = cv2.createBackgroundSubtractorGMG()
		while (1):
			ret, frame = cap.read()
			fgmask = fgbg.apply(frame)
			fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
			cv2.imshow('frame', fgmask)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break
		cap.release()
		cv2.destroyAllWindows()
		print("")

	def test_415(self):
		#41.5结果
		print("")

