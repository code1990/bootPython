import unittest
import cv2
import numpy as np, sys


# • 学习图像金字塔
# • 使用图像创建一个新水果：“橘子苹果”
# • 将要学习的函数有：cv2.pyrUp()，cv2.pyrDown()
class c_20_test(unittest.TestCase):
	def test_201(self):
		# 20.1原理
		# 我们需要对同一图像的不同分辨率的子图像进行处理。
		# 比如，我们要在一幅图像中查找某个目标，比如脸，我们不知道目标在图像中的尺寸大小。
		# 我们需要创建创建一组图像，这些图像是具有不同分辨率的原始图像。我们把这组图像叫做图像金字塔
		# 有两类图像金字塔：高斯金字塔和拉普拉斯金字塔。
		# 高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的。
		# 我们可以使用函数cv2.pyrDown() 和cv2.pyrUp() 构建图像金字塔。
		# 函数cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔（尺寸变小，分辨率降低）。
		# 函数cv2.pyrUp() 从一个低分辨率小尺寸的图像向下构建一个金子塔（尺寸变大，但分辨率不会增加）。
		# 一旦使用cv2.pyrDown()，图像的分辨率就会降低，信息就会被丢
		# 拉普拉金字塔的图像看起来就像边界图，其中很多像素都是0
		print("")

	def test_202(self):
		# 20.2使用金字塔进行图像融合
		# 图像金字塔的一个应用是图像融合。
		# 经典案例就是将两个水果融合成一个
		# 实现上述效果的步骤如下：
		# 1. 读入两幅图像，苹果和句子
		# 2. 构建苹果和橘子的高斯金字塔（6 层）
		# 3. 根据高斯金字塔计算拉普拉斯金字塔
		# 4. 在拉普拉斯的每一层进行图像融合（苹果的左边与橘子的右边融合）
		# 5. 根据融合后的图像金字塔重建原始图像。
		A = cv2.imread('apple.jpg')
		B = cv2.imread('orange.jpg')
		# generate Gaussian pyramid for A
		G = A.copy()
		gpA = [G]
		for i in range(6):
			G = cv2.pyrDown(G)
		gpA.append(G)
		# generate Gaussian pyramid for B
		G = B.copy()
		gpB = [G]
		for i in range(6):
			G = cv2.pyrDown(G)
		gpB.append(G)
		# generate Laplacian Pyramid for A
		lpA = [gpA[5]]
		for i in range(5, 0, -1):
			GE = cv2.pyrUp(gpA[i])
		L = cv2.subtract(gpA[i - 1], GE)
		lpA.append(L)
		# generate Laplacian Pyramid for B
		lpB = [gpB[5]]
		for i in range(5, 0, -1):
			GE = cv2.pyrUp(gpB[i])
		L = cv2.subtract(gpB[i - 1], GE)
		lpB.append(L)
		# Now add left and right halves of images in each level
		# numpy.hstack(tup)
		# Take a sequence of arrays and stack them horizontally
		# to make a single array.
		LS = []
		for la, lb in zip(lpA, lpB):
			rows, cols, dpt = la.shape
		ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
		LS.append(ls)
		# now reconstruct
		ls_ = LS[0]
		for i in range(1, 6):
			ls_ = cv2.pyrUp(ls_)
		ls_ = cv2.add(ls_, LS[i])
		# image with direct connecting each half
		real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))
		cv2.imwrite('Pyramid_blending2.jpg', ls_)
		cv2.imwrite('Direct_blending.jpg', real)
		print("")
