import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 使用不同的低通滤波器对图像进行模糊
# • 使用自定义的滤波器对图像进行卷积
class c_16_test(unittest.TestCase):
	def test_161(self):
		# 对2D 图像实施低通滤波（LPF），高通滤波
		# （HPF）等。LPF 帮助我们去除噪音，模糊图像。HPF 帮助我们找到图像的边 # 缘
		# OpenCV 提供的函数cv.filter2D() 可以让我们对一幅图像进行卷积操		# 作
		# 16.1平均
		# 将核放在图像的一个像素A 上，求与核对应的图像上25（5x5）
		# 个像素的和，在取平均数，用这个平均数替代像素A 的值。重复以上操作直到
		# 将图像的每一个像素值都更新一边
		img = cv2.imread('opencv-logo.png')
		kernel = np.ones((5, 5), np.float32) / 25
		# when ddepth=-1, the output image will have the same depth as the source.
		dst = cv2.filter2D(img, -1, kernel)
		plt.subplot(121), plt.imshow(img), plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
		plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

	def test_1611(self):
		# OpenCV 提供了四种模糊技术。
		# 16.1 平均
		# 这是由一个归一化卷积框完成的。他只是用卷积框覆盖区域所有像素的平
		# 均值来代替中心元素。可以使用函数cv2.blur() 和cv2.boxFilter() 来完
		# 这个任务
		img = cv2.imread('opencv-logo.png')
		blur = cv2.blur(img, (5, 5))
		plt.subplot(121), plt.imshow(img), plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
		plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

	def test_162(self):
		# 16.2高斯模糊
		# 使用低通滤波器可以达到图像模糊的目的。这对与去除噪音很有帮助。其
		# 实就是去除图像中的高频成分（比如：噪音，边界
		# 现在把卷积核换成高斯核（简单来说，方框不变，将原来每个方框的值是
		# 相等的，现在里面的值是符合高斯分布的，方框中心的值最大，其余方框根据
		# 距离中心元素的距离递减，构成一个高斯小山包。原来的求平均数现在变成求
		# 加权平均数，全就是方框里的值）。实现的函数是cv2.GaussianBlur()。我
		# 们需要指定高斯核的宽和高（必须是奇数）。以及高斯函数沿X，Y 方向的标准
		# 差。
		# 0 是指根据窗口大小（5,5）来计算高斯函数标准差
		# 高斯滤波可以有效的从图像中去除高斯噪音。
		img = cv2.imread('opencv-logo.png')
		blur = cv2.GaussianBlur(img, (5, 5), 0)
		plt.subplot(121), plt.imshow(img), plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
		plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

	def test_163(self):
		# 16.3中值模糊
		# 中值滤波是用中心像素周围（也可以使他本身）的值来取代他。
		# 他能有效的去除噪声。卷积核的大小也应该是一个奇数。
		# 在这个例子中，我们给原始图像加上50% 的噪声然后再使用中值模糊。
		img = cv2.imread('opencv-logo.png')
		blur = cv2.medianBlur(img, 5)
		plt.subplot(121), plt.imshow(img), plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
		plt.xticks([]), plt.yticks([])
		plt.show()
		print("")

	def test_164(self):
		# 16.4双边滤波
		# 函数cv2.bilateralFilter() 能在保持边界清晰的情况下有效的去除噪
		# 音。但是这种操作与其他滤波器相比会比较慢
		# 双边滤波在同时使用空间高斯权重和灰度值相似性高斯权重。空间高斯函
		# 数确保只有邻近区域的像素对中心点有影响，灰度值相似性高斯函数确保只有
		# 与中心像素灰度值相近的才会被用来做模糊运算。所以这种方法会确保边界不
		# 会被模糊掉，因为边界处的灰度值变化比较大。
		img = cv2.imread('opencv-logo.png')
		# #9 邻域直径，两个75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
		blur = cv2.bilateralFilter(img, 9, 75, 75)
		plt.subplot(121), plt.imshow(img), plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
		plt.xticks([]), plt.yticks([])
		plt.show()
		print("")
