import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt
# 学习对图像进行各种几个变换，例如移动，旋转，仿射变换等。
# • 将要学到的函数有：cv2.getPerspectiveTransform。
class c_14_test(unittest.TestCase):
	# # OpenCV 提供了两个变换函数，cv2.warpAffine 和cv2.warpPerspective，
	# 		# cv2.warpAffine 接收的参数是2  3 的变换矩阵，
	# 		# 而cv2.warpPerspective 接收的参数是3  3 的变换矩阵。
	# 		#13.1转换颜色空间
	def test_141(self):
		# 14.1扩展缩放
		img = cv2.imread("python.png")
		# 下面的None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
		# 因此这里为None
		res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

		# OR
		# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
		height, width = img.shape[:2]
		res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

		while (1):
			cv2.imshow('res', res)
			cv2.imshow('img', img)
			if cv2.waitKey(1) & 0xFF == 27:
				break
		cv2.destroyAllWindows()

	def test_142(self):
		# 14.2平移
		# 平移就是将对象换一个位置。如果你要沿（x，y）方向移动，移动的距离是（tx，ty），
		# 构建这个矩阵（数据类型是np.float32），
		# 然后把它传给函数cv2.warpAffine()。看看下面这个例子吧，它被移动了（100,50）个像素。
		cap = cv2.VideoCapture(0)
		while 1:
			# 获取每一帧
			ret, frame = cap.read()
			# 转换到HSV
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			# 设定蓝色的阈值
			lower_blue = np.array([110, 50, 50])
			upper_blue = np.array([130, 255, 255])
			# 根据阈值构建掩模
			mask = cv2.inRange(hsv, lower_blue, upper_blue)
			# 对原图像和掩模进行位运算
			res = cv2.bitwise_and(frame, frame, mask=mask)
			# 显示图像
			cv2.imshow('frame', frame)
			cv2.imshow('mask', mask)
			cv2.imshow('res', res)
			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				break
			# 关闭窗口
		cv2.destroyAllWindows()
		# 函数cv2.warpAffine() 的第三个参数的是输出图像的大小，它的格式应该是图像的（宽，高）。
		# 应该记住的是图像的宽对应的是列数，高对应的是行数。

	def test_143(self):
		# 14.3旋转
		# 对一个图像旋转角度, 需要使用到下面形式的旋转矩阵
		# 为了构建这个旋转矩阵，OpenCV 提供了一个函数：cv2.getRotationMatrix2D。
		# 下面的例子是在不缩放的情况下将图像旋转90 度
		img = cv2.imread('python.png', 0)
		rows, cols = img.shape
		# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
		# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
		M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)
		# 第三个参数是输出图像的尺寸中心
		dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
		while (1):
			cv2.imshow('img', dst)
			if cv2.waitKey(1) & 0xFF == 27:
				break
		cv2.destroyAllWindows()
		print("")

	def test_144(self):
		# 14.4仿射变换
		# 要从原图像中找到三个点以及他们在输出图像中的位置。然后
		# cv2.getAffineTransform 会创建一个2x3 的矩阵，最后这个矩阵会被传给
		# 函数cv2.warpAffine。
		img = cv2.imread('python.png')
		rows, cols, ch = img.shape
		pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
		pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
		M = cv2.getAffineTransform(pts1, pts2)
		dst = cv2.warpAffine(img, M, (cols, rows))
		plt.subplot(121, plt.imshow(img), plt.title('Input'))
		plt.subplot(121, plt.imshow(img), plt.title('Output'))
		plt.show()

	def test_145(self):
		# 14.5透视变换
		# 对于视角变换，我们需要一个3x3 变换矩阵。在变换前后直线还是直线。
		# 要构建这个变换矩阵，你需要在输入图像上找4 个点，以及他们在输出图
		# 像上对应的位置。这四个点中的任意三个都不能共线。这个变换矩阵可以有
		# 函数cv2.getPerspectiveTransform() 构建。然后把这个矩阵传给函数
		# cv2.warpPerspective。
		img = cv2.imread('python.png')
		rows, cols, ch = img.shape
		pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
		pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
		M = cv2.getPerspectiveTransform(pts1, pts2)
		dst = cv2.warpPerspective(img, M, (300, 300))
		plt.subplot(121, plt.imshow(img), plt.title('Input'))
		plt.subplot(121, plt.imshow(img), plt.title('Output'))
		plt.show()
