import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt


# 我们将要学习在图像间进行特征匹配
# • 使用OpenCV 中的蛮力（Brute-Force）匹配和FLANN 匹配
class c_37_test(unittest.TestCase):
	def test_371(self):
		# 37.1Brute-Force匹配的基础
		# 首先在第一幅图像中选取一个关键点然后依次与
		# 第二幅图像的每个关键点进行（描述符）距离测试，最后返回距离最近的关键点。
		# 对于BF 匹配器，我们首先要使用cv2.BFMatcher() 创建一个BFMatcher
		# 对象。它有两个可选参数。第一个是normType。它是用来指定要
		# 使用的距离测试类型。默认值为cv2.Norm_L2
		# 第二个参数是布尔变量crossCheck，默认值为False。如果设置为
		# True，匹配条件就会更加严格
		print("")

	def test_372(self):
		# 37.2对ORB描述符进行蛮力匹配
		# 在本例中我们
		# 有一个查询图像和一个目标图像。我们要使用特征匹配的方法在目标图像中寻
		# 找查询图像的位置
		img1 = cv2.imread('box.png', 0)  # queryImage
		img2 = cv2.imread('box_in_scene.png', 0)  # trainImage
		# Initiate SIFT detector
		orb = cv2.ORB()
		# find the keypoints and descriptors with SIFT
		kp1, des1 = orb.detectAndCompute(img1, None)
		kp2, des2 = orb.detectAndCompute(img2, None)
		# create BFMatcher object
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
		# Match descriptors.
		matches = bf.match(des1, des2)
		# Sort them in the order of their distance.
		matches = sorted(matches, key=lambda x: x.distance)
		print("")

	def test_373(self):
		# 37.3匹配器对象是什么？
		# matches = bf:match(des1; des2) 返回值是一个DMatch 对象列表。这个
		# DMatch 对象具有下列属性：
		# • DMatch.distance - 描述符之间的距离。越小越好。
		# • DMatch.trainIdx - 目标图像中描述符的索引。
		# • DMatch.queryIdx - 查询图像中描述符的索引。
		# • DMatch.imgIdx - 目标图像的索引。
		print("")

	def test_374(self):
		# 37.4对SIFT描述符进行蛮力匹配和比值测试
		# 现在我们使用BFMatcher.knnMatch() 来获得k 对最佳匹配。在本例中
		# 我们设置k = 2，这样我们就可以使用D.Lowe 文章中的比值测试了。
		img1 = cv2.imread('box.png', 0)  # queryImage
		img2 = cv2.imread('box_in_scene.png', 0)  # trainImage
		# Initiate SIFT detector
		sift = cv2.SIFT()
		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(img1, None)
		kp2, des2 = sift.detectAndCompute(img2, None)
		# BFMatcher with default params
		bf = cv2.BFMatcher()
		matches = bf.knnMatch(des1, des2, k=2)
		# Apply ratio test
		# 比值测试，首先获取与A 距离最近的点B（最近）和C（次近），只有当B/C
		# 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为0
		good = []
		for m, n in matches:
			if m.distance < 0.75 * n.distance:
				good.append([m])
		# cv2.drawMatchesKnn expects list of lists as matches.
		img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], flags=2)
		plt.imshow(img3), plt.show()
		print("")

	def test_375(self):
		# 37.5FLANN匹配器
		# 使用FLANN 匹配，我们需要传入两个字典作为参数。这两个用来确定要
		# 使用的算法和其他相关参数等。第一个是IndexParams。各种不同算法的信
		# 息可以在FLANN 文档中找到
		# 第二个字典是SearchParams。用它来指定递归遍历的次数。值越高
		# 结果越准确，但是消耗的时间也越多
		img1 = cv2.imread('box.png', 0)  # queryImage
		img2 = cv2.imread('box_in_scene.png', 0)  # trainImage
		# Initiate SIFT detector
		sift = cv2.SIFT()
		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(img1, None)
		kp2, des2 = sift.detectAndCompute(img2, None)
		# BFMatcher with default params
		bf = cv2.BFMatcher()
		matches = bf.knnMatch(des1, des2, k=2)
		# Apply ratio test
		good = []
		for m, n in matches:
			if m.distance < 0.75 * n.distance:
				good.append([m])
		# cv2.drawMatchesKnn expects list of lists as matches.
		img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, flags=2)
		plt.imshow(img3), plt.show()
		print("")

	def test_3751(self):
		img1 = cv2.imread('box.png', 0)  # queryImage
		img2 = cv2.imread('box_in_scene.png', 0)  # trainImage
		# Initiate SIFT detector
		sift = cv2.SIFT()
		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(img1, None)
		kp2, des2 = sift.detectAndCompute(img2, None)
		# FLANN parameters
		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
		search_params = dict(checks=50)  # or pass empty dictionary
		flann = cv2.FlannBasedMatcher(index_params, search_params)
		matches = flann.knnMatch(des1, des2, k=2)
		# Need to draw only good matches, so create a mask
		matchesMask = [[0, 0] for i in range(len(matches))]
		# ratio test as per Lowe's paper
		for i, (m, n) in enumerate(matches):
			if m.distance < 0.7 * n.distance:
				matchesMask[i] = [1, 0]
		draw_params = dict(matchColor=(0, 255, 0),
		                   singlePointColor=(255, 0, 0),
		                   matchesMask=matchesMask,
		                   flags=0)
		img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
		plt.imshow(img3, ), plt.show()
		print("")
