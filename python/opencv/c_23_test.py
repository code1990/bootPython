import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt


# • 使用OpenCV 对图像进行傅里叶变换
# • 使用Numpy 中FFT（快速傅里叶变换）函数
# • 傅里叶变换的一些用处
# • 我们将要学习的函数有：cv2.dft()，cv2.idft() 等
class c_23_test(unittest.TestCase):
	def test_231(self):
		# 23.1傅里叶变换
		# 傅里叶变换经常被用来分析不同滤波器的频率特性。我们可以使用2D 离
		# 散傅里叶变换(DFT) 分析图像的频域特性。实现DFT 的一个快速算法被称为
		# 快速傅里叶变换
		print("")

	def test_2311(self):
		# 23.1.1Numpy中的傅里叶变换
		# 如何使用Numpy 进行傅里叶变换。Numpy 中的FFT 包
		# 可以帮助我们实现快速傅里叶变换。函数np.fft.fft2() 可以对信号进行频率转
		# 换，输出结果是一个复杂的数组
		img = cv2.imread('messi5.jpg', 0)
		f = np.fft.fft2(img)
		fshift = np.fft.fftshift(f)
		# 这里构建振幅图的公式没学过
		magnitude_spectrum = 20 * np.log(np.abs(fshift))
		plt.subplot(121), plt.imshow(img, cmap='gray')
		plt.title('Input Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
		plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
		plt.show()
		rows, cols = img.shape
		crow, ccol = rows / 2, cols / 2
		fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
		f_ishift = np.fft.ifftshift(fshift)
		img_back = np.fft.ifft2(f_ishift)
		# 取绝对值
		img_back = np.abs(img_back)
		plt.subplot(131), plt.imshow(img, cmap='gray')
		plt.title('Input Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(132), plt.imshow(img_back, cmap='gray')
		plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
		plt.subplot(133), plt.imshow(img_back)
		plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
		# 结果显示高通滤波其实是一种边界检测操作
		plt.show()

	def test_2312(self):
		print("")
		# 23.1.2OpenCV中的傅里叶变换
		# OpenCV 中相应的函数是cv2.dft() 和cv2.idft()。和前面输出的结果
		# 一样，但是是双通道的。第一个通道是结果的实数部分，第二个通道是结果的 虚数部分。
		img = cv2.imread('messi5.jpg', 0)
		dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
		dft_shift = np.fft.fftshift(dft)
		magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
		plt.subplot(121), plt.imshow(img, cmap='gray')
		plt.title('Input Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
		plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
		plt.show()
		# 现在我们来做逆DFT
		rows, cols = img.shape
		crow, ccol = rows / 2, cols / 2
		# create a mask first, center square is 1, remaining all zeros
		mask = np.zeros((rows, cols, 2), np.uint8)
		mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
		# apply mask and inverse DFT
		fshift = dft_shift * mask
		f_ishift = np.fft.ifftshift(fshift)
		img_back = cv2.idft(f_ishift)
		img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
		plt.subplot(121), plt.imshow(img, cmap='gray')
		plt.title('Input Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(122), plt.imshow(img_back, cmap='gray')
		plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
		plt.show()

	# 23.1.3DFT的性能优化
	# 当数组的大小为某些值时DFT 的性能会更好。当数组的大小是2 的指数
	# 时DFT 效率最高。当数组的大小是2，3，5 的倍数时效率也会很高。所以
	# 如果你想提高代码的运行效率时，你可以修改输入图像的大小（补0）。对于
	# OpenCV 你必须自己手动补0。但是Numpy，你只需要指定FFT 运算的大
	# 小，它会自动补0。
	# 那我们怎样确定最佳大小呢？OpenCV 提供了一个函数:cv2.getOptimalDFTSize()。
	# 它可以同时被cv2.dft() 和np.fft.fft2() 使用
	def test_2314(self):
		# 23.1.4为什么拉普拉斯算子是高通滤波器？
		# simple averaging filter without scaling parameter
		mean_filter = np.ones((3, 3))
		# creating a guassian filter
		x = cv2.getGaussianKernel(5, 10)
		# x.T 为矩阵转置
		gaussian = x * x.T
		# different edge detecting filters
		# scharr in x-direction
		scharr = np.array([[-3, 0, 3],
		                   [-10, 0, 10],
		                   [-3, 0, 3]])
		# sobel in x direction
		sobel_x = np.array([[-1, 0, 1],
		                    [-2, 0, 2],
		                    [-1, 0, 1]])
		# sobel in y direction
		sobel_y = np.array([[-1, -2, -1],
		                    [0, 0, 0],
		                    [1, 2, 1]])
		# laplacian
		laplacian = np.array([[0, 1, 0],
		                      [1, -4, 1],
		                      [0, 1, 0]])
		filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
		filter_name = ['mean_filter', 'gaussian', 'laplacian', 'sobel_x', 'sobel_y', 'scharr_x']
		fft_filters = [np.fft.fft2(x) for x in filters]
		fft_shift = [np.fft.fftshift(y) for y in fft_filters]
		mag_spectrum = [np.log(np.abs(z) + 1) for z in fft_shift]
		for i in range(6):
			plt.subplot(2, 3, i + 1), plt.imshow(mag_spectrum[i], cmap='gray')
		plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])
		plt.show()
		print("")
