import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt


# 图像上的算术运算，加法，减法，位运算等
# 学习的函数与有：cv2.add()，cv2.addWeighted()
class c_10_test(unittest.TestCase):
	def test_101(self):
		# 10.1图像加法
		# 函数cv2.add() 将两幅图像进行加法运算，当然也可以直接使
		# 用numpy，res=img1+img。两幅图像的大小，类型必须一致，或者第二个
		# 图像可以使一个简单的标量值
		# OpenCV 的加法是一种饱和操作，而Numpy 的加法是一种模操作。
		x = np.unit8([250])
		y = np.unit8([10])
		# 250+10 = 260 => 255
		print(cv2.add(x, y))
		# # 250+10 = 260 % 256 = 4
		print(x + y)

	def test_102(self):
		# 10.2图像混合
		# 其实也是加法
		# 图像混合的计算公式如下：g(x)=(1-a)f0(x)+af1(x)
		# 第一幅图的权重是0.7，第二幅图的权重		# 是0.3。
		# 函数cv2.addWeighted() 可以按下面的公式对图片进行混合操作
		img1 = cv2.imread("python.png")
		img2 = cv2.imread("opencv-logo.png")
		# 两幅图像的大小，类型必须一致 上面给定的图片和类型不一致 所以报错了
		dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
		cv2.imshow("dst", dst)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def test_103(self):
		# 10.3按位运算
		# 这里包括的按位操作有：AND，OR，NOT，XOR 等
		img1 = cv2.imread("python.png")
		img2 = cv2.imread("opencv-logo.png")

		rows, cols, channels = img2.shape
		roi = img1[0:rows, 0:cols]

		img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
		ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
		mask_inv = cv2.bitwise_not(mask)

		# # 取roi 中与mask 中不为零的值对应的像素的值，其他值为0
		# # 注意这里必须有mask=mask 或者mask=mask_inv, 其中的mask= 不能忽略
		img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
		# 取roi 中与mask_inv 中不为零的值对应的像素的值，其他值为0。
		# Take only region of logo from logo image.
		img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

		dst = cv2.add(img1_bg, img2_fg)
		img1[0:rows, 0:cols] = dst
		cv2.imshow("res", img1)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		print("")
