import unittest
import cv2
import numpy as np


# 检测程序的效率
# • 一些能够提高程序效率的技巧
# • 你要学到的函数有：cv2.getTickCount,cv2.getTickFrequency

# Python 也提供了一个叫time 的的模块，你可以用它来测量
# 程序的运行时间。另外一个叫做profile 的模块会帮你得到一份关于你的程序
# 的详细报告，其中包含了代码中每个函数运行需要的时间，以及每个函数被调
# 用的次数
class c_11_test(unittest.TestCase):
	def test_111(self):
		# 11.1使用OpenCV检测程序效率
		# cv2.getTickCount 函数返回从参考点到这个函数被执行的时钟数。
		# cv2.getTickFrequency 返回时钟频率，或者说每秒钟的时钟数。
		e1 = cv2.getTickCount()
		array = []
		for i in range(1000, 1):
			array.append(i)
		e2 = cv2.getTickCount()
		time = (e2 - e1) / cv2.getTickFrequency()
		print(time)

	def test_1110(self):
		img1 = cv2.imread("python.png")
		e1 = cv2.getTickCount()
		# python3保留了xrange()的实现，且将xrange()重新命名成range()
		for i in range(5, 49, 2):
			img1 = cv2.medianBlur(img1, i)
		e2 = cv2.getTickCount()
		t = (e2 - e1) / cv2.getTickFrequency()
		print(t)

	def test_112(self):
		# 11.2OpenCV中的默认优化
		# OpenCV 运行的就是优化后的代码
		# 使用函数cv2.useOptimized()来查看优化是否被开启
		print(cv2.useOptimized())
		cv2.setUseOptimized(False)
		print(cv2.useOptimized())
		print("")

	def test_113(self):
		# 11.3在IPython中检测程序效率
		# IPython一个强大的python交互式shell
		# 使用IPython 为你提供的魔法命令%time
		# cv2.countNonZero() 和		# np.count_nonzero()。
		# 一般情况下OpenCV 的函数要比Numpy 函数快
		# 使用Numpy 对视图（而非复制）进行操作
		img = cv2.imread("python.png")
		cv2.countNonZero(img)
		np.count_nonzero(img)
		print("")

	def test_114(self):
		# 11.4更多IPython的魔法命令
		print("")

	def test_115(self):
		# 11.5效率优化技术
		# 首先用简单的方式实现你的算法（结果正确最重要
		# 1. 尽量避免使用循环，尤其双层三层循环，它们天生就是非常慢的。
		# 2. 算法中尽量使用向量操作，因为Numpy 和OpenCV 都对向量操作进行了优化。
		# 3. 利用高速缓存一致性。
		# 4. 没有必要的话就不要复制数组。使用视图来代替复制。数组复制是非常浪费资源的。
		print("1")
