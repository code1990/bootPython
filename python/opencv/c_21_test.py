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
		im = cv2.ellipse(img, ellipse, (0, 255, 0), 2)
		# 21.2.10线拟合
		# 根据一组点拟合出一条直线
		rows, cols = img.shape[:2]
		[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
		lefty = int((-x * vy / vx) + y)
		righty = int(((cols - x) * vy / vx) + y)
		img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
		# def test_213(self):
		# 21.3轮廓的性质
		# 可以在Matlab# regionprops documentation 更多的图像特征。
		print("")
		# 21.3.1长宽比
		# 边界矩形的宽高比
		x, y, w, h = cv2.boundingRect(cnt)
		aspect_ratio = float(w) / h
		print(aspect_ratio)
		# 21.3.2Extent
		# 轮廓面积与边界矩形面积的比。
		area = cv2.contourArea(cnt)
		x, y, w, h = cv2.boundingRect(cnt)
		rect_area = w * h
		extent = float(area) / rect_area
		print(extent)
		# 21.3.3Solidity
		# 轮廓面积与凸包面积的比。
		area = cv2.contourArea(cnt)
		hull = cv2.convexHull(cnt)
		hull_area = cv2.contourArea(hull)
		solidity = float(area) / hull_area
		# 21.3.4EquivalentDiameter
		# 与轮廓面积相等的圆形的直径
		area = cv2.contourArea(cnt)
		equi_diameter = np.sqrt(4 * area / np.pi)
		print(equi_diameter)
		# 21.3.5方向
		# 对象的方向，下面的方法还会返回长轴和短轴的长度
		(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
		# 21.3.6掩模和像素点
		# 有时我们需要构成对象的所有像素点，我们可以这样做：
		mask = np.zeros(img.shape, np.uint8)
		# 这里一定要使用参数-1, 绘制填充的的轮廓
		cv2.drawContours(mask, [cnt], 0, 255, -1)
		pixelpoints = np.transpose(np.nonzero(mask))
		# pixelpoints = cv2.findNonZero(mask)
		# 21.3.7最大值和最小值及它们的位置
		# 使用掩模图像得到这些参数。
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask=mask)
		# 21.3.8平均颜色及平均灰度
		# 使用相同的掩模求一个对象的平均颜色或平均灰度
		mean_val = cv2.mean(im, mask=mask)
		# 21.3.9极点
		# 一个对象最上面，最下面，最左边，最右边的点。
		leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
		rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
		topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
		bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
		# def test_214(self):
		# 21.4轮廓：更多函数
		# 凸缺陷，以及如何找凸缺陷
		# • 找某一点到一个多边形的最短距离
		# • 不同形状的匹配
		# 对象上的任何凹陷都被成为凸缺陷。
		# OpenCV 中有一个函数cv.convexityDefect() 可以帮助我们找到凸缺陷。
		# returnPoints 一定要是False。
		hull = cv2.convexHull(cnt, returnPoints=False)
		defects = cv2.convexityDefects(cnt, hull)

	# 它会返回一个数组，其中每一行包含的值是[起点，终点，最远的点，到最
	# 远点的近似距离]
	def test_2211(self):
		print("")
		img = cv2.imread('python.png')
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
		contours, hierarchy = cv2.findContours(thresh, 2, 1)
		cnt = contours[0]
		hull = cv2.convexHull(cnt, returnPoints=False)
		defects = cv2.convexityDefects(cnt, hull)
		for i in range(defects.shape[0]):
			s, e, f, d = defects[i, 0]
		start = tuple(cnt[s][0])
		end = tuple(cnt[e][0])
		far = tuple(cnt[f][0])
		cv2.line(img, start, end, [0, 255, 0], 2)
		cv2.circle(img, far, 5, [0, 0, 255], -1)
		cv2.imshow('img', img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		# 21.4.1凸缺陷
		# 21.4.2PointPolygonTest
		# 求解图像中的一个点到一个对象轮廓的最短距离。如果点在轮廓的外部，
		# 返回值为负。如果在轮廓上，返回值为0。如果在轮廓内部，返回值为正。
		# 下面我们以点（50，50）为例：
		# 此函数的第三个参数是measureDist。如果设置为True，就会计算最
		# 短距离。如果是False，只会判断这个点与轮廓之间的位置关系（返回值为
		# +1，-1，0）
		dist = cv2.pointPolygonTest(cnt, (50, 50), True)

	def test_220(self):
		# 21.4.3形状匹配
		# 	函数cv2.matchShape() 可以帮我们比较两个形状或轮廓的相似度。如
		# 果返回值越小，匹配越好。它是根据Hu 矩来计算的
		img1 = cv2.imread('star.jpg', 0)
		img2 = cv2.imread('star2.jpg', 0)
		ret, thresh = cv2.threshold(img1, 127, 255, 0)
		ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
		contours, hierarchy = cv2.findContours(thresh, 2, 1)
		cnt1 = contours[0]
		contours, hierarchy = cv2.findContours(thresh2, 2, 1)
		cnt2 = contours[0]
		ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
		print(ret)

	def test_215(self):
		# 21.5轮廓的层次结构
		# 现在我们要学习轮廓的层次结构了，比如轮廓之间的父子关系。
		print("")
		# 21.5.1什么是层次结构
		# 21.5.2OpenCV中层次结构
		# 21.5.3轮廓检索模式
		# 可以确定一个轮廓与其他轮廓是怎样连接的，
		# 比如它是不是某个轮廓的子轮廓，或者是父轮廓。这种关系就成为组织结构
		# 了解释层次结构，外轮廓，子轮廓，父轮廓，子轮廓。
		# OpenCV 使用一个含有四个元素的数组表示。[Next，Previous，First_Child，Parent]
		# Next 表示同一级组织结构中的下一个轮廓。
		# Previous 表示同一级结构中的前一个轮廓。
		# First_Child 表示它的第一个子轮廓。
		# Parent 表示它的父轮廓。
		# 21.5.3 轮廓检索模式
		# RETR_LIST 它只是提取所有的轮廓
		# RETR_EXTERNAL 返回最外边的的轮廓，所有的子轮廓都会被忽略掉。
		# RETR_CCOMP 返回所有的轮廓并将轮廓分为两级组织结构
		# RETR_TREE 返回所有轮廓，并且创建一个完整的组织结构列表
