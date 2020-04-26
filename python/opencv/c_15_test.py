import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 函数有cv2.threshold，cv2.adaptiveThreshold
# 简单阈值
class c_15_test(unittest.TestCase):
	def test_151(self):
		# 15.1简单阈值
		# 第一个参数就是原图像，原图像应该是灰度图。
		# 第二个参数就是用来对像素值进行分类的阈值。
		# 第三个参数就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值
		# 函数有两个返回值，
		# 第一个为retVal，我们后面会解释。
		# 第二个就是阈值化之后的结果图像
		# 使用是全局阈值，整幅图像采用同一个数作为阈值
		img = cv2.imread('python.png', 0)
		ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
		ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
		ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
		ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
		ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

		titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
		images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
		for i in range(6):
			plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
		plt.title(titles[i])
		plt.xticks([]), plt.yticks([])
		plt.show()

		print("")

	def test_152(self):
		# 15.2自适应阈值
		# 在同一幅图像上的不同区域采用的是		# 不同的阈值
		# 这种方法需要我们指定三个参数，返回值只有一个。
		# • Adaptive Method- 指定计算阈值的方法。
		# – cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平均值
		# – cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取值相邻区域的加权和，权重为一个高斯窗口。
		# • Block Size - 邻域大小（用来计算阈值的区域大小）。
		# • C - 这就是是一个常数，阈值就等于的平均值或者加权平均值减去这个常数。
		img = cv2.imread('python.png', 0)
		# 中值滤波
		img = cv2.medianBlur(img, 5)
		ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
		# 11 为Block size, 2 为C 值
		th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
		th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
		titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding',
		          'Adaptive Gaussian Thresholding']
		images = [img, th1, th2, th3]
		for i in range(4):
			plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
		plt.title(titles[i])
		plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

	def test_153(self):
		# 15.3Otsu’s二值化
		# 对一副双峰图像自动根据其直方图计算出一个阈值
		# 用到到的函数还是cv2.threshold()
		# 第一种方法，我们设127 为全局阈值。
		# 第二种方法，我们直接使用Otsu 二值化。
		# 第三种方法，我们首先使用一个5x5 的高斯核除去噪音，然后再使用Otsu 二值化
		img = cv2.imread('python.png', 0)
		# global thresholding
		ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
		# Otsu's thresholding
		ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		# Otsu's thresholding after Gaussian filtering
		# （5,5）为高斯核的大小，0 为标准差
		blur = cv2.GaussianBlur(img, (5, 5), 0)
		# 阈值一定要设为0！
		ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		# plot all the images and their histograms
		images = [img, 0, th1,
		          img, 0, th2,
		          blur, 0, th3]
		titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
		          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
		          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
		# # 这里使用了pyplot 中画直方图的方法，plt.hist, 要注意的是它的参数是一维数组
		# # 所以这里使用了（numpy）ravel 方法，将多维数组转换成一维，也可以使用flatten 方法
		for i in range(3):
			plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
			plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
			plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
			plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
			plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
			plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

	def test_154(self):
		# 15.4Otsu’s二值化是如何工作的？
		img = cv2.imread('python.png', 0)
		blur = cv2.GaussianBlur(img, (5, 5), 0)
		# 计算归一化直方图
		hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
		hist_norm = hist.ravel() / hist.max()
		Q = hist_norm.cumsum()
		bins = np.arange(256)
		fn_min = np.inf
		thresh = -1

		for i in range(1, 256):
			p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
			q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
			b1, b2 = np.hsplit(bins, [i])  # weights
			# finding means and variances
			m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
			v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
			# calculates the minimization function
			fn = v1 * q1 + v2 * q2
			if fn < fn_min:
				fn_min = fn
				thresh = i
			# find otsu's threshold value with OpenCV function
		ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		print(thresh)
		print(ret)
		print("")
