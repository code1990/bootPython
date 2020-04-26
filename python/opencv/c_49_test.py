import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# 学习使用非局部平均值去噪算法去除图像中的噪音
# • 学习函数cv2.fastNlMeansDenoising()，cv2.fastNlMeansDenoisingColored()
# 等
class c_49_test(unittest.TestCase):
	def test_491(self):
		#49.1OpenCV中的图像去噪
		# OpenCV 提供了这种技术的四个变本。
		# 1. cv2.fastNlMeansDenoising() 使用对象为灰度图。
		# 2. cv2.fastNlMeansDenoisingColored() 使用对象为彩色图。
		# 3. cv2.fastNlMeansDenoisingMulti() 适用于短时间的图像序列（灰
		# 度图像）
		# 4. cv2.fastNlMeansDenoisingColoredMulti() 适用于短时间的图
		# 像序列（彩色图像）
		# 共同参数有：
		# • h : 决定过滤器强度。h 值高可以很好的去除噪声，但也会把图像的细节
		# 抹去。(取10 的效果不错)
		# • hForColorComponents : 与h 相同，但使用与彩色图像。（与h 相
		# 同）
		# • templateWindowSize : 奇数。(推荐值为7)
		# • searchWindowSize : 奇数。(推荐值为21)
		print("")

	#49.1.1cv2.fastNlMeansDenoisingColored()
	def test_4911(self):
		img = cv2.imread('die.png')
		dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
		plt.subplot(121), plt.imshow(img)
		plt.subplot(122), plt.imshow(dst)
		plt.show()
		print("")
	#49.1.2cv2.fastNlMeansDenoisingMulti()
	def test_4912(self):
		cap = cv2.VideoCapture('vtest.avi')
		# create a list of first 5 frames
		img = [cap.read()[1] for i in range(5)]
		# convert all to grayscale
		gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]
		# convert all to float64
		gray = [np.float64(i) for i in gray]
		# create a noise of variance 25
		noise = np.random.randn(*gray[1].shape) * 10
		# Add this noise to images
		noisy = [i + noise for i in gray]
		# Convert back to uint8
		noisy = [np.uint8(np.clip(i, 0, 255)) for i in noisy]
		# Denoise 3rd frame considering all the 5 frames
		dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)
		plt.subplot(131), plt.imshow(gray[2], 'gray')
		plt.subplot(132), plt.imshow(noisy[2], 'gray')
		plt.subplot(133), plt.imshow(dst, 'gray')
		plt.show()
		print("")
