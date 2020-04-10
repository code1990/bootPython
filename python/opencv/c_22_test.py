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
		# 这里使用了Numpy 的掩模数组
		# 构建Numpy 掩模数组，cdf 为原数组，当数组元素为0 时，掩盖（计算时被忽略）。
		cdf_m = np.ma.masked_equal(cdf, 0)
		cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
		# 对被掩盖的元素赋值，这里赋值为0
		cdf = np.ma.filled(cdf_m, 0).astype('uint8')
		# 直方图均衡化经常用来使所有的图片具有相同的亮度条件的参考	# 工具。

	# 22.2.1OpenCV中的直方图均衡化
	def test_22111(self):
		# 	cv2.equalizeHist()。这个函数的输
		# 入图片仅仅是一副灰度图像，输出结果是直方图均衡化之后的图像。
		img = cv2.imread('python.png', 0)
		equ = cv2.equalizeHist(img)
		res = np.hstack((img, equ))
		# stacking images side-by-side
		cv2.imwrite('res.png', res)

	# 22.2.2CLAHE有限对比适应性直方图均衡化
	def test_22221(self):
		# 需要使用自适应的直方图均衡化
		img = cv2.imread('python.png', 0)
		# create a CLAHE object (Arguments are optional).
		# 不知道为什么我没好到createCLAHE 这个模块
		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
		cl1 = clahe.apply(img)
		cv2.imwrite('clahe_2.jpg', cl1)
		print("")
	def test_2232(self):
		# 22.32D直方图
		print("")

	# 22.3.1介绍
	# 在2D 直方图中我们就要考虑两个图像特征
	# 需要考虑每个的颜色（Hue）和饱和度（Saturation） 具体案例
	# 具体案例 color_histogram.py

	def test_22321(self):
		# 22.3.2OpenCV中的2D直方图
		# 使用函数cv2.calcHist() 来计算直方图既简单又方便。
		# 计算颜色直方图/一维直方图，要从BGR 转换到HSV
		# 计算2D 直方图，函数的参数要做如下修改：
		# • channels=[0，1] 因为我们需要同时处理H 和S 两个通道。
		# • bins=[180，256]H 通道为180，S 通道为256。
		# • range=[0，180，0，256]H 的取值范围在0 到180，S 的取值范围在0 到256
		img = cv2.imread('python.png')
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

	def test_22333(self):
		# 22.3.3Numpy中2D直方图
		# 绘制2D 直方图的函数：np.histogram2d()。
		# 绘制1D 直方图时我们使用的是np.histogram()
		# 第一个参数是H 通道，
		# 第二个参数是S 通道，
		# 第三个参数是bins 的数目，
		# 第四个参数是数值范围。
		img = cv2.imread('home.jpg')
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		# hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]])

	def test_2234(self):
		# 22.3.4绘制2D直方图
		# 方法1：使用cv2.imshow()
		# 方法2：使用Matplotlib()matplotlib.pyplot.imshow()
		# 方法3：OpenCV 􅉽格 color_histogram.py
		img = cv2.imread('python.png')
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
		plt.imshow(hist, interpolation='nearest')
		plt.show()

	# 22.4.1Numpy中的算法
	def test_11(self):
		# roi is the object or region of object we need to find
		roi = cv2.imread('rose_red.png')
		hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
		# target is the image we search in
		target = cv2.imread('rose.png')
		hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
		# Find the histograms using calcHist. Can be done with np.histogram2d also
		M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
		I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])
		# 以用来做图像分割，或者在图像中找寻我们感兴趣的部分
		# 首先，我们要创建两幅颜色直方图，目标图像的直方图（'M'），（待搜索）输入图像的直方图（'I'）。
		# 计算比值：R = M / I 。反向投影R，也就是根据R
		# 这个”调色板“创建一
		# 副新的图像，其中的每一个像素代表这个点就是目标的概率。
		R = M/I
		h, s, v = cv2.split(hsvt)
		B = R[h.ravel(), s.ravel()]
		B = np.minimum(B, 1)
		B = B.reshape(hsvt.shape[:2])
		# 现在使用一个圆盘算子做卷积，B = D  B，其中D
		# 为卷积核。
		disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
		B = cv2.filter2D(B, -1, disc)
		B = np.uint8(B)
		cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)
		# 如果我们要找的是一个区域，我们就可以使用一个阈值对图像进行二值化，这样就可以得到一个很好的结果了
		ret, thresh = cv2.threshold(B, 50, 255, 0)

	# 22.4.2OpenCV中的反向投影
	def test_224(self):
		# 22.4直方图反向投影
		# OpenCV 提供的函数cv2.calcBackProject() 可以用来做直方图反向
		# 投影。它的参数与函数cv2.calcHist 的参数基本相同。其中的一个参数是我
		# 们要查找目标的直方图。同样再使用目标的直方图做反向投影之前我们应该先
		# 对其做归一化处理。返回的结果是一个概率图像，我们再使用一个圆盘形卷积
		# 核对其做卷操作，最后使用阈值进行二值化
		roi = cv2.imread('tar.jpg')
		hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
		target = cv2.imread('roi.jpg')
		hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
		# calculating object histogram
		roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
		# normalize histogram and apply backprojection
		# 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
		# cv2.NORM_MINMAX 对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
		# 归一化之后的直方图便于显示，归一化之后就成了0 到255 之间的数了。
		cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
		dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)
		# Now convolute with circular disc
		# 此处卷积可以把分散的点连在一起
		disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
		dst = cv2.filter2D(dst, -1, disc)
		# threshold and binary AND
		ret, thresh = cv2.threshold(dst, 50, 255, 0)
		# 别忘了是三通道图像，因此这里使用merge 变成3 通道
		thresh = cv2.merge((thresh, thresh, thresh))
		# 按位操作
		res = cv2.bitwise_and(target, thresh)
		res = np.hstack((target, thresh, res))
		cv2.imwrite('res.jpg', res)
		# 显示图像
		cv2.imshow('1', res)
		cv2.waitKey(0)
		print("")

