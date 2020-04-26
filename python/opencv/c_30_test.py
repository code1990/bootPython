import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 理解Harris 角点检测的概念
# • 学习函数：cv2.cornerHarris()，cv2.cornerSubPix()
class c_30_test(unittest.TestCase):
	def test_301(self):
		#30.1OpenCV中的Harris角点检测
		# Open 中的函数cv2.cornerHarris() 可以用来进行角点检测。参数如下：
		# • img - 数据类型为float32 的输入图像。
		# • blockSize - 角点检测中要考虑的领域大小。
		# • ksize - Sobel 求导中使用的窗口大小
		# • k - Harris 角点检测方程中的自由参数，取值参数为[0,04，0.06].
		filename = 'chessboard.jpg'
		img = cv2.imread(filename)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = np.float32(gray)
		# 输入图像必须是float32，最后一个参数在0.04 到0.05 之间
		dst = cv2.cornerHarris(gray, 2, 3, 0.04)
		# result is dilated for marking the corners, not important
		dst = cv2.dilate(dst, None)
		# Threshold for an optimal value, it may vary depending on the image.
		img[dst > 0.01 * dst.max()] = [0, 0, 255]
		cv2.imshow('dst', img)
		if cv2.waitKey(0) & 0xff == 27:
			cv2.destroyAllWindows()
		print("")

	def test_302(self):
		#30.2亚像素级精确度的角点
		# 有时我们需要最大精度的角点检测。OpenCV 为我们提供了函数cv2.cornerSubPix()，
		# 它可以提供亚像素级别的角点检测。
		filename = 'chessboard2.jpg'
		img = cv2.imread(filename)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# find Harris corners
		gray = np.float32(gray)
		dst = cv2.cornerHarris(gray, 2, 3, 0.04)
		dst = cv2.dilate(dst, None)
		ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
		dst = np.uint8(dst)
		# find centroids
		# connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
		# OutputArray centroids, int connectivity=8, int ltype=CV_32S)
		ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
		# define the criteria to stop and refine the corners
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
		# Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
		# zeroZone – Half of the size of the dead region in the middle of the search zone
		# over which the summation in the formula below is not done. It is used sometimes
		# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
		# indicates that there is no such a size.
		# 返回值由角点坐标组成的一个数组（而非图像）
		corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
		# Now draw them
		res = np.hstack((centroids, corners))
		# np.int0 可以用来省略小数点后面的数字（非四􃮼五入）。
		res = np.int0(res)
		img[res[:, 1], res[:, 0]] = [0, 0, 255]
		img[res[:, 3], res[:, 2]] = [0, 255, 0]
		cv2.imwrite('subpixel5.png', img)
		print("")

