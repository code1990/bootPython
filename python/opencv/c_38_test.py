import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt


# 联合使用特征提取和calib3d 模块中的findHomography 在复杂图像
# 中查找已知对象。
class c_38_test(unittest.TestCase):
	def test_381(self):
		# 38.1基础
		print("")

	def test_382(self):
		# 38.2代码
		# 和通常一样我们先在图像中来找到SIFT 特征点，然后再使用比值测试找
		# 到最佳匹配
		MIN_MATCH_COUNT = 10
		img1 = cv2.imread('box.png', 0)  # queryImage
		img2 = cv2.imread('box_in_scene.png', 0)  # trainImage
		# Initiate SIFT detector
		sift = cv2.SIFT()
		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(img1, None)
		kp2, des2 = sift.detectAndCompute(img2, None)
		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
		search_params = dict(checks=50)
		flann = cv2.FlannBasedMatcher(index_params, search_params)
		matches = flann.knnMatch(des1, des2, k=2)
		# store all the good matches as per Lowe's ratio test.
		good = []
		for m, n in matches:
			if m.distance < 0.7 * n.distance:
				good.append(m)
		# 查询图像的四个顶点（四个角）变换到目标图像中去了。然后再绘制出来。
		if len(good) > MIN_MATCH_COUNT:
			# 获取关键点的坐标
			src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
			dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
			# 第三个参数Method used to computed a homography matrix. The following methods are possible:
			# 0 - a regular method using all the points
			# CV_RANSAC - RANSAC-based robust method
			# CV_LMEDS - Least-Median robust method
			# 第四个参数取值范围在1 到10，􁲁绝一个点对的阈值。原图像的点经过变换后点与目标图像上对应点的误差
			# 超过误差就认为是outlier
			# 返回值中M 为变换矩阵。
			M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
			matchesMask = mask.ravel().tolist()
			# 获得原图像的高和宽
			h, w = img1.shape
			# 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标。
			pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
			dst = cv2.perspectiveTransform(pts, M)
			# 原图像为灰度图
			cv2.polylines(img2, [np.int32(dst)], True, 255, 10, cv2.LINE_AA)
		else:
			print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
			matchesMask = None
		# 	最后我再绘制inliers（如果能成功的找到目标图像的话）或者匹配的关键		# 点
		draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
		                   singlePointColor=None,
		                   matchesMask=matchesMask,  # draw only inliers
		                   flags=2)
		img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
		plt.imshow(img3, 'gray'), plt.show()
		print("")
