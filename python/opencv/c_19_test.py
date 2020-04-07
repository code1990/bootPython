import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt
# 了解Canny 边缘检测的概念
# • 学习函数cv2.Canny()
class c_19_test(unittest.TestCase):
	def test_191(self):
		# Canny 边缘检测是一种非常流行的边缘检测算法
		# 由于边缘检测很容易受到噪声影响，所以第一步是使用5x5 的高斯滤波器
		# 去除噪声
		#19.1原理
		print("")

		#19.1.1噪声去除
		#19.1.2计算图像梯度
		# 对平滑后的图像使用Sobel 算子计算水平方向和竖直方向的一阶导数（图像梯度）（Gx 和Gy）。
		# 根据得到的这两幅梯度图（Gx 和Gy）找到边界的梯度和方向，
		# 梯度的方向一般总是与边界垂直。梯度方向被归为四类：垂直，水平，和两个对角线。
		#19.1.3非极大值抑制
		# 在获得梯度的方向和大小之后，应该对整幅图像做一个扫描，去除那些非
		# 边界上的点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯
		# 度方向的点中最大的
		#19.1.4滞后阈值
		# 现在要确定那些边界才是真正的边界。
		# 这时我们需要设置两个阈值：minVal 和maxVal。
		# 当图像的灰度梯度高于maxVal 时被认为是真的边界，
		# 那些低于minVal 的边界会被抛弃。
		# 如果介于两者之间的话，就要看这个点是
		# 否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是就抛弃
	def test_192(self):
		#19.2OpenCV中的Canny边界检测
		# 在OpenCV 中只需要一个函数：cv2.Canny()，就可以完成以上几步。
		# 第一个参数是输入图像。
		# 第二和第三个分别是minVal 和maxVal。
		# 第三个参数设置用来计算图像梯度的Sobel卷积核的大小，默认值为3。
		# 最后一个参数是L2gradient，它可以用来设定求梯度大小的方程。
		# 如果设为True，就会使用我们上面提到过的方程，否则使用方程默认值为False
		img = cv2.imread('opencv-logo.png', 0)
		edges = cv2.Canny(img, 100, 200)
		plt.subplot(121), plt.imshow(img, cmap='gray')
		plt.title('Original Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(edges, cmap='gray')
		plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

