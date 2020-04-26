import unittest
import cv2
import numpy as np
from matplotlib import pyplot as plt
# • 获取像素值并修改
# • 获取图像的属性（信息）
# • 图像的ROI（）
# • 图像通道的拆分及合并
class c_09_test(unittest.TestCase):
	def test_91(self):
		#9.1获取并修改像素值
		# 首先我们需要读入一幅图像：
		img =cv2.imread("python.png")
		px = img[100,100]
		print(px)
		blue = img[100,100,0]
		print(blue)
		# 能有矩阵运算就不要用循环
		img[100,100]=[25,255,255]
		print(img[100,100])
		# 获取像素值及修改的更好方法。
		print(img.item(10,10,2))
		img.itemset((10,10,2),100)
		print(img.item(10,10,2))
		print("")

	def test_92(self):
		#9.2获取图像属性
		# 图像的属性包括：行，列，通道，图像数据类型，像素数目等
		# img.shape 可以获取图像的形状。他的返回值是一个包含行数，列数，
		# 通道数的元组。
		img = cv2.imread("python.png")
		# 注意：如果图像是灰度图，返回值仅有行数和列数
		print(img.shape)
		# img.size 可以返回图像的像素数目
		print(img.size)
		# img.dtype 返回的是图像的数据类型.
		# 经常出现数据类型的不一致
		print(img.dtype)

	def test_93(self):
		#9.3图像ROI
		# ROI 也是使用Numpy 索引来获得的。现在我们选择球的部分并把他拷贝
		# 到图像的其他区域。
		# 对一幅图像的特定区域进行操作
		img = cv2.imread("python.png")
		ball = img[280:340,330:390]
		img[273:333,100:160]=ball
		print("")

	def test_94(self):
		#9.4拆分及合并图像通道
		# 对BGR 三个通道分别进行操作
		img = cv2.imread("python.png")
		# ：cv2.split() 是一个比较耗时的操作
		b,g,r = cv2.split(img)
		img = cv2.merge(b,g,r)
		# 获取采取如下的方式
		b=img[:,:,0]
		# 使所有像素的红色通道值都为0
		img[:, :, 2]=0
		print("")

	def test_95(self):
		#9.5为图像扩边（填充）
		# 在图像周围创建一个边，就像相框一样，你可以使用cv2.copyMakeBorder()函数。
		# • src 输入图像
		# • top, bottom, left, right 对应边界的像素数目。
		# • borderType 要添加那种类型的边界
		# • value 边界颜色
		BLUE = [255, 0, 0]
		img1 = cv2.imread("opencv-logo.png")
		replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
		reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
		reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
		wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
		constant = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
		plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
		plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
		plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
		plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
		plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
		plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
		plt.show()

