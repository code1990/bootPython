import unittest
import cv2
import numpy as np

# 如何对图像进行颜色空间转换，比如从BGR 到灰度图，或者从BGR 到HSV
# 从一幅图像中获取某个特定颜色的物体
# 函数有：cv2.cvtColor()，cv2.inRange()
class c_13_test(unittest.TestCase):
	def test_131(self):
		# 13.1转换颜色空间
		# 经常用到的也就两种：BGR$Gray 和BGR$HSV
		# 对于BGR$Gray 的转换，我们要使用的flag 就是cv2.COLOR_BGR2GRAY。
		# 同样对于BGR$HSV 的转换，我们用的flag 就是cv2.COLOR_BGR2HSV
		# OpenCV 的HSV 值与其他软件的HSV 值进行对比时，一定要记得归一
		flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
		print(flags)

	def test_132(self):
		# 13.2物体跟踪
		# 要提取的是一个蓝色的物体。下面就是就是我们要做的几步：
		# • 从视频中获取每一帧图像
		# • 将图像转换到HSV 空间
		# • 设置HSV 阈值到蓝色范围。
		# • 获取蓝色物体，当然我们还可以做其他任何我们想做的事
		cap = cv2.VideoCapture(0)
		while (1):
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
			cv2.imshow("frame", frame)
			cv2.imshow("mask", mask)
			cv2.imshow("res", res)
			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				break
		# 关闭窗口
		cv2.destroyAllWindows()

	# 	当你学习了轮廓之后，你就会学到更多相关知识，
	# 那是你就可以找到物体的重心，并根据重心来跟踪物体

	def test_133(self):
		# 13.3怎样找到要跟踪对象的HSV值？
		# 其实这真的很简单，
		# 函数cv2.cvtColor() 也可以用到这里。但是现在你要传入的参数是（你想要
		# 的）BGR 值而不是一副图
		green = np.uint8([[[0, 255, 0]]])
		hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
		print(hsv_green)
		print("")
