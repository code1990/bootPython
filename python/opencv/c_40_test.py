import unittest
# • 光流的概念以及Lucas-Kanade 光流法
# • 使用函数cv2.calcOpticalFlowPyrLK() 对图像中的特征点进行跟# 踪
import numpy as np
import cv2


class c_40_test(unittest.TestCase):
	def test_401(self):
		# 40.1光流
		# 它是一个2D 向量场，可以用来显示一个点从第一帧图像到第二
		# 帧图像之间的移动
		print("")

	def test_402(self):
		# 40.2Lucas-Kanade法
		print("")

	def test_403(self):
		# 40.3OpenCV中的Lucas-Kanade光流
		# 上述所有过程都被OpenCV 打包成了一个函数：cv2.calcOpticalFlowPyrLK()。
		# lk_track.py
		cap = cv2.VideoCapture('slow.flv')
		# params for ShiTomasi corner detection
		feature_params = dict(maxCorners=100,
		                      qualityLevel=0.3,
		                      minDistance=7,
		                      blockSize=7)
		# Parameters for lucas kanade optical flow
		# maxLevel 为使用的图像金字塔层数
		lk_params = dict(winSize=(15, 15),
		                 maxLevel=2,
		                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
		# Create some random colors
		color = np.random.randint(0, 255, (100, 3))
		# Take first frame and find corners in it
		ret, old_frame = cap.read()
		old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
		p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
		# Create a mask image for drawing purposes
		mask = np.zeros_like(old_frame)
		while (1):
			ret, frame = cap.read()
			frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# calculate optical flow 能够获取点的新位置
			p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
			# Select good points
			good_new = p1[st == 1]
			good_old = p0[st == 1]
			# draw the tracks
			for i, (new, old) in enumerate(zip(good_new, good_old)):
				a, b = new.ravel()
			c, d = old.ravel()
			mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
			frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
			img = cv2.add(frame, mask)
			cv2.imshow('frame', img)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break
			# Now update the previous frame and previous points
			old_gray = frame_gray.copy()
			p0 = good_new.reshape(-1, 1, 2)
		cv2.destroyAllWindows()
		cap.release()
		print("")

	def test_404(self):
		# 40.4OpenCV中的稠密光流
		# OpenCV 还提供了一种计算稠密光流的
		# 方法。它会图像中的所有点的光流。这是基于Gunner_Farneback 的算法
		# opt_flow.py
		cap = cv2.VideoCapture("vtest.avi")
		ret, frame1 = cap.read()
		prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
		hsv = np.zeros_like(frame1)
		hsv[..., 1] = 255
		while (1):
			ret, frame2 = cap.read()
			next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
			flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
			# cv2.cartToPolar Calculates the magnitude and angle of 2D vectors.
			mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
			hsv[..., 0] = ang * 180 / np.pi / 2
			hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
			rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
			cv2.imshow('frame2', rgb)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break
			elif k == ord('s'):
				cv2.imwrite('opticalfb.png', frame2)
			cv2.imwrite('opticalhsv.png', rgb)
			prvs = next
		cap.release()
		cv2.destroyAllWindows()
		print("")
