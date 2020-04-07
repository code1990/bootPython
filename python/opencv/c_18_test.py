import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像梯度，图像边界等
# • 使用到的函数有：cv2.Sobel()，cv2.Schar()，cv2.Laplacian() 等
class c_18_test(unittest.TestCase):
	# OpenCV 提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr 和Laplacian。
	# Sobel，Scharr 其实就是求一阶或二阶导数。
	# Scharr 是对Sobel（使用小的卷积核求解求解梯度角度时）的优化。Laplacian 是求二阶导数。
	def test_181(self):
		# 18.1Sobel算子和Scharr算子
		# Sobel 算子是高斯平滑与微分操作的结合体，所以它的抗噪声能力很好。
		# 你可以设定求导的方向（xorder 或yorder）。还可以设定使用的卷积核的大
		# 小（ksize）。如果ksize=-1，会使用3x3 的Scharr 滤波器，它的的效果要
		# 比3x3 的Sobel 滤波器好
		print("")

	def test_182(self):
		# 18.2Laplacian算子
		# 拉普拉斯算子可以使用二阶导数的形式定义，可假设其离散实现类似于二
		# 阶Sobel 导数，事实上，OpenCV 在计算拉普拉斯算子时直接调用Sobel 算
		# 子。
		img = cv2.imread('opencv-logo.png', 0)
		# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致np.uint8
		laplacian = cv2.Laplacian(img, cv2.CV_64F)
		# 参数1,0 为只在x 方向求一阶导数，最大可以求2 阶导数。
		sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
		# 参数0,1 为只在y 方向求一阶导数，最大可以求2 阶导数。
		sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
		plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
		plt.title('Original'), plt.xticks([]), plt.yticks([])
		plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
		plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
		plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
		plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
		plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
		plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
		plt.show()

	def test_183(self):
		# 想象一下一个从黑到白的边界
		# 的导数是整数，而一个从白到黑的边界点导数却是负数。如果原图像的深度是
		# np.int8 时，所有的负值都会被截断变成0，换句话说就是把把边界丢失掉。
		# 所以如果这两种边界你都想检测到，最好的的办法就是将输出的数据类型
		# 设置的更高，比如cv2.CV_16S，cv2.CV_64F 等。取绝对值然后再把它转回
		# 到cv2.CV_8U
		img = cv2.imread('python.png', 0)
		# Output dtype = cv2.CV_8U
		sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
		# 也可以将参数设为-1
		# sobelx8u = cv2.Sobel(img,-1,1,0,ksize=5)
		# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
		sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)
		sobel_8u = np.uint8(abs_sobel64f)
		plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
		plt.title('Original'), plt.xticks([]), plt.yticks([])
		plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
		plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
		plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
		plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
		plt.show()