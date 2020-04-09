import unittest
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 使用OpenCV 或Numpy 函数计算直方图
# • 使用Opencv 或者Matplotlib 函数绘制直方图
# • 将要学习的函数有：cv2.calcHist()，np.histogram()
class c_22_test(unittest.TestCase):
	def test_221(self):
		# 22.1直方图的计算，绘制与分析
		# 通过直方图你可以对整幅图像的灰度分布有一个整体的了解
		# 直方图其实就是对图像的另一种解释
		# 直方图是根据灰度图像绘制的，而不是彩色图像
		# BINS：上面的直方图显示了每个灰度值对应的像素数
		# DIMS：表示我们收集数据的参数数目
		# RANGE：就是要统计的灰度值范围
		#
		# 函数cv2.calcHist 可以帮助我们统计一幅图像的直方图。
		# cv2:calcHist(images; channels; mask; histSize; ranges[; hist[; accumulate]])
		# 1. images: 原图像（图像格式为uint8 或float32）。
		# 当传入函数时应该用中括号[] 括起来，例如：[img]。
		# 2. channels: 同样需要用中括号括起来，它会告诉函数我们要统计那幅图像的直方图。
		# 如果输入图像是灰度图，它的值就是[0]；
		# 如果是彩色图像的话，传入的参数可以是[0]，[1]，[2] 它们分别对应着通道B，G，R。
		# 3. mask: 掩模图像。要统计整幅图像的直方图就把它设为None。
		# 但是如果你想统计图像某一部分的直方图的话，你就需要制作一个掩模图像
		# 4. histSize:BIN 的数目。也应该用中括号括起来，例如：[256]。
		# 5. ranges: 像素值范围，通常为[0，256]
		img = cv2.imread('python.png', 0)
		# 别忘了中括号[img],[0],None,[256],[0,256]，只有mask 没有中括号
		hist = cv2.calcHist([img], [0], None, [256], [0, 256])
		# hist 是一个256x1 的数组，每一个值代表了与次灰度值对应的像素点数目。
		# img.ravel() 将图像转成一维数组，这里没有中括号。
		hist, bins = np.histogram(img.ravel(), 256, [0, 256])

	# 对于一维直方图， 我们最好使用这个函数
	# hist=np.bincount(img.ravel()，minlength=256)
	# 22.1.1统计直方图
	# 22.1.2绘制直方图
	def test_1111(self):
		# 1. Short Way（简单方法）：使用Matplotlib 中的绘图函数。
		img = cv2.imread('python.png', 0)
		plt.hist(img.ravel(), 256, [0, 256])
		plt.show()

	def test_1112(self):
		# 2. Long Way（复杂方法）：使用OpenCV 绘图函数
		img = cv2.imread('python.png')
		color = ('b', 'g', 'r')
		# 对一个列表或数组既要遍历索引又要遍历元素时
		# 使用内置enumerrate 函数会有更加直接，优美的做法
		# enumerate 会将数组或列表组成一个索引序列。
		# 使我们再获取索引和索引内容的时候更加方便
		for i, col in enumerate(color):
			histr = cv2.calcHist([img], [i], None, [256], [0, 256])
		plt.plot(histr, color=col)
		plt.xlim([0, 256])
		plt.show()

	def test_1113(self):
		# 22.1.3使用掩模
		# 要统计图像某个局部区域的直方图只需要构建一副掩模图像。将要统计的
		# 部分设置成白色，其余部分为黑色，就构成了一副掩模图像。然后把这个掩模
		# 图像传给函数就可以了。
		img = cv2.imread('python.png', 0)
		# create a mask
		mask = np.zeros(img.shape[:2], np.uint8)
		mask[100:300, 100:400] = 255
		masked_img = cv2.bitwise_and(img, img, mask=mask)
		# Calculate histogram with mask and without mask
		# Check third argument for mask
		hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
		hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])
		plt.subplot(221), plt.imshow(img, 'gray')
		plt.subplot(222), plt.imshow(mask, 'gray')
		plt.subplot(223), plt.imshow(masked_img, 'gray')
		plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
		plt.xlim([0, 256])
		plt.show()

	def test_222(self):
		# 22.2直方图均衡化
		# 如何使用它来改善图片的对比。
		# 把它的直方图做一个横向拉伸（如下图），这就是直方图均衡化要做的事情
		# 这种操作会改善图像的对比度。
		# 先看看怎样使用Numpy 来进行直方图均衡化，
		# 然后再学习使用OpenCV 进行直方图均衡化。
		img = cv2.imread('python.png', 0)
		# flatten() 将数组变成一维
		hist, bins = np.histogram(img.flatten(), 256, [0, 256])
		# 计算累积分布图
		cdf = hist.cumsum()
		cdf_normalized = cdf * hist.max() / cdf.max()
		plt.plot(cdf_normalized, color='b')
		plt.hist(img.flatten(), 256, [0, 256], color='r')
		plt.xlim([0, 256])
		plt.legend(('cdf', 'histogram'), loc='upper left')
		plt.show()

	# 22.2.1OpenCV中的直方图均衡化
	# 22.2.2CLAHE有限对比适应性直方图均衡化
	def test_2232(self):
		# 22.32D直方图
		print("")

	# 22.3.1介绍
	# 22.3.2OpenCV中的2D直方图
	# 22.3.3Numpy中2D直方图
	# 22.3.4绘制2D直方图
	def test_224(self):
		# 22.4直方图反向投影
		print("")

# 22.4.1Numpy中的算法
# 22.4.2OpenCV中的反向投影
