import unittest
import numpy as np
import cv2


# • 理解什么是轮廓
# • 学习找轮廓，绘制轮廓等
# • 函数：cv2.findContours()，cv2.drawContours()
class c_21_test(unittest.TestCase):
	def test_211(self):
		# 21.1初识轮廓
		# 轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线，具有相同的颜色或者灰度。
		# 轮廓在形状分析和物体的检测和识别中很有用。
		# • 为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理或者Canny 边界检测。
		# • 查找轮廓的函数会修改原始图像。
		# • 你应该记住，要找的物体应该是白色而背景应该是黑色。
		# 让我们看看如何在一个二值图像中查找轮廓：
		# 函数cv2.findContours()
		# 有三个参数，
		# 第一个是输入图像，
		# 第二个是轮廓检索模式，
		# 第三个是轮廓近似方法。
		# 返回值有三个，
		# 第一个是图像，
		# 第二个是轮廓，
		# 第三个是（轮廓的）层析结构。
		# 21.1.1什么是轮廓
		# 函数cv2.drawContours() 可以被用来绘制轮廓。
		# 它的第一个参数是原始图像，
		# 第二个参数是轮廓，一个Python 列表。
		# 第三个参数是轮廓的索引（当设置为-1 时绘制所有轮廓）。
		# 第4参数是轮廓的颜色和
		# 第5参数是厚度等。
		# 21.1.2怎样绘制轮廓
		im = cv2.imread('python.png')
		imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		ret, thresh = cv2.threshold(imgray, 127, 255, 0)
		image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		# 绘制独立轮廓，如第四个轮廓：
		img = cv2.drawContour(image, contours, -1, (0, 255, 0), 3)
		# 但是大多数时候，下面的方法更有用：
		img = cv2.drawContours(image, contours, 3, (0, 255, 0), 3)

	# 21.1.3轮廓的近似方法
	# 这就是cv2.CHAIN_APPROX_SIMPLE 要做的。它会将轮廓上的冗余点都去掉，压缩轮廓，从而节省内存开支。
	def test_212(self):
		# 21.2轮廓特征
		print("")
		# 查找轮廓的不同特征，例如面积，周长，重心，边界框等。
		# • 你会学到很多轮廓相关函数
		# 21.2.1矩
		# 图像的矩可以帮助我们计算图像的质心，面积等。
		# 函数cv2.moments() 会将计算得到的矩以一个字典的形式返回。
		img = cv2.imread('python.png', 0)
		ret, thresh = cv2.threshold(img, 127, 255, 0)
		contours, hierarchy = cv2.findContours(thresh, 1, 2)
		cnt = contours[0]
		M = cv2.moments(cnt)
		print(M)
		# 计算出对象的重心
		cx = int(M['m10'] / M['m00'])
		cy = int(M['m01'] / M['m00'])
		print(cx)
		print(cy)
		# 21.2.2轮廓面积
		# 轮廓的面积可以使用函数cv2.contourArea()
		area = cv2.contourArea(cnt)
		print(area)
		# 21.2.3轮廓周长
		# 使用函数cv2.arcLength() 计算得到。
		# 这个函数的第二参数可以用来指定对象的形状是闭合的（True），
		perimeter = cv2.arcLength(cnt, True)
		print(perimeter)
		# 21.2.4轮廓近似
		# 将轮廓形状近似到另外一种由更少点组成的轮廓形状，
		# 这个函数的第二个参数叫epsilon，它是从原始轮廓到近似轮廓的最大距离。
		# 它是一个准确度参数。选择一个好的epsilon 对于得到满意结果非常重要
		# 第三个参数设定弧线是否闭合。
		epsilon = 0.1 * cv2.arcLength(cnt, True)
		approx = cv2.approxPolyDP(cnt, epsilon, True)
		# 21.2.5凸包
		# 	凸包与轮廓近似相似
		# 函数cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷。
		# 如果有地方凹进去了就被叫做凸性缺陷。
		# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
		# • points 我们要传入的轮廓
		# • hull 输出，通常不需要
		# • clockwise 方向标志。如果设置为True，输出的凸包是顺时针方向的。否则为逆时针方向。
		# • returnPoints 默认值为True。它会返回凸包上点的坐标。
		# 如果设置为False，就会返回与凸包点对应的轮廓上的点。
		hull = cv2.convexHull(cnt)
		# 21.2.6凸性检测
		# 函数cv2.isContourConvex() 可以可以用来检测一个曲线是不是凸的。它只能返回True 或False
		k = cv2.isContourConvex(cnt)
		# 21.2.7边界矩形
		# 直边界矩形
		# 它不会考虑对象是否旋转。所以边界矩形的面积不是最小的。
		# 使用函数cv2.boundingRect() 查找得到。
		# （x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高。
		x, y, w, h = cv2.boundingRect(cnt)
		img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
		# 旋转的边界矩形这个边界矩形是面积最小的，因为它考虑了对象的旋转。
		# 函数为cv2.minAreaRect()。返回的是一个Box2D 结构，其中包含
		# 矩形左上角角点的坐标（x，y），矩形的宽和高（w，h），以及旋转角度。
		# 要绘制这个矩形需要矩形的4 个角点，可以通过函数cv2.boxPoints() 获得。
		x, y, w, h = cv2.boundingRect(cnt)
		img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# 21.2.8最小外接圆
		# 函数cv2.minEnclosingCircle()
		# 可以帮我们找到一个对象的外切圆。
		# 它是所有能够包括对象的圆中面积最小的一个。
		(x, y), radius = cv2.minEnclosingCircle(cnt)
		center = (int(x), int(y))
		radius = int(radius)
		img = cv2.circle(img, center, radius, (0, 255, 0), 2)
		# 21.2.9椭圆拟合
		# 使用的函数为cv2.ellipse()，返回值其实就是旋转边界矩形的内切圆。
		ellipse = cv2.fitEllipse(cnt)
		im = cv2.ellipse(img,ellipse,(0,255,0),2)
		# 21.2.10线拟合
		# 根据一组点拟合出一条直线
		rows, cols = img.shape[:2]
		[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
		lefty = int((-x * vy / vx) + y)
		righty = int(((cols - x) * vy / vx) + y)
		img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
	def test_213(self):
		# 21.3轮廓的性质
		print("")

		# 21.3.1长宽比
		# 21.3.2Extent
		# 21.3.3Solidity
		# 21.3.4EquivalentDiameter
		# 21.3.5方向
		# 21.3.6掩模和像素点
		# 21.3.7最大值和最小值及它们的位置
		# 21.3.8平均颜色及平均灰度
		# 21.3.9极点
	def test_214(self):
		# 21.4轮廓：更多函数
		print("")

		# 21.4.1凸缺陷
		# 21.4.2PointPolygonTest
		# 21.4.3形状匹配
	def test_215(self):
		# 21.5轮廓的层次结构
		print("")

		# 21.5.1什么是层次结构
		# 21.5.2OpenCV中层次结构
		# 21.5.3轮廓检索模式
