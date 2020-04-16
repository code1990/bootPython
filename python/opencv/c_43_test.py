import unittest
import cv2
import numpy as np
import glob
# 本节我们要学习使用calib3D 模块在图像中创建3D 效果
# 在上一节的摄像机标定中，我们已经得到了摄像机矩阵，畸变系数等
class c_43_test(unittest.TestCase):
	def draw(img, corners, imgpts):
		corner = tuple(corners[0].ravel())
		img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255, 0, 0), 5)
		img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0, 255, 0), 5)
		img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0, 0, 255), 5)
		return img
	def test_431(self):
		#43.1基础
		# 首先我们要加载前面结果中摄像机矩阵和畸变系数。
		with np.load('B.npz') as X:
			mtx, dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]
		print("")

		#43.1.1渲染一个立方体
