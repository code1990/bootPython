import unittest
# 任何一副灰度图像都可以被看成拓扑平面，灰度值高的区域可以被看成是
# 山峰，灰度值低的区域可以被看成是山谷。我们向每一个山谷中灌不同颜色的
# 水。随着水的位的升高，不同山谷的水就会相遇汇合，为了防止不同山谷的水
# 汇合，我们需要在水汇合的地方构建起堤坝。不停的灌水，不停的构建堤坝知
# 道所有的山峰都被水淹没。我们构建好的堤坝就是对图像的分割。这就是分水
# 岭算法的背后哲理。
import numpy as np
import cv2
from matplotlib import pyplot as plt
class c_27_test(unittest.TestCase):
	def test_271(self):
		#27.1代码
		# 下面的例子中我们将就和距离变换和分水岭算法对紧挨在一起的对象进行
		# 分割。
		# 如下图所示，这些硬币紧挨在一起。就算你使用阈值操作，它们任然是紧
		# 挨着的。
		img = cv2.imread('water_coins.jpg')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
		# 现在我们要去除图像中的所有的白噪声。这就需要使用形态学中的开运算。
		# 为了去除对象上小的空洞我们需要使用形态学闭运算。所以我们现在知道靠近
		# 对象中心的区域肯定是前景，而远离对象中心的区域肯定是背景。而不能确定
		# noise removal
		kernel = np.ones((3, 3), np.uint8)
		opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
		# sure background area
		sure_bg = cv2.dilate(opening, kernel, iterations=3)
		# Finding sure foreground area
		# 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，也就是到零像素点的最短距离
		# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全
		# 腐蚀。这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心􅑗􂅥像素点的
		# 距离。根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
		# cv2.distanceTransform(src, distanceType, maskSize)
		# 第二个参数0,1,2 分别表示CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
		dist_transform = cv2.distanceTransform(opening, 1, 5)
		ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
		# Finding unknown region
		sure_fg = np.uint8(sure_fg)
		unknown = cv2.subtract(sure_bg, sure_fg)
		# Marker labelling
		ret, markers1 = cv2.connectedComponents(sure_fg)
		# Add one to all labels so that sure background is not 0, but 1
		markers = markers1 + 1
		# Now, mark the region of unknown with zero
		markers[unknown == 255] = 0
		markers3 = cv2.watershed(img, markers)
		img[markers3 == -1] = [255, 0, 0]
		print("")

