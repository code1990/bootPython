import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# • 理解FAST 算法的基础
# • 使用OpenCV 中的FAST 算法相关函数进行角点检测
class c_34_test(unittest.TestCase):
	def test_341(self):
		#34.1使用FAST算法进行特征提取
		# 一个最好例子就是SLAM（同步定位与地
		# 图构建），移动机器人，它们的计算资源非常有限
		# 1. 在图像中选取一个像素点p，来判断它是不是关键点。Ip 等于像素点p的灰度值。
		# 2. 选择适当的阈值t。
		# 3. 如下图所示在像素点p 的周围选择16 个像素点进行测试。
		# 4. 如果在这16 个像素点中存在n 个连续像素点的灰度值都高于Ip + t，或
		# 者低于Ip 􀀀t，那么像素点p 就被认为是一个角点。
		# 5. 为了获得更快的效果，还采用了而外的加速办法。
		print("")

	def test_342(self):
		#34.2机器学习的角点检测器
		# 1. 选择一组训练图片（最好是跟最后应用相关的图片）
		# 2. 使用FAST 算法找出每幅图像的特征点
		# 3. 对每一个特征点，将其周围的16 个像素存储构成一个向量。对所有图像
		# 都这样做构建一个特征向量P
		# 4. 每一个特征点的16 像素点都属于下列三类中的一种。
		# 5. 根据这些像素点的分类，特征向量P 也被分为3 个子集：Pd，Ps，Pb
		# 6. 定义一个新的布尔变量Kp，如果p 是角点就设置为Ture，如果不是就
		# 设置为False。
		# 7. 使用ID3 算法（决策树分类器）
		# 8.递归地将其应用于所有子集，直到其熵为		# 零。
		# 9. 将构建好的决策树运用于其他图像的快速的检测。
		print("")

	def test_343(self):
		#34.3非极大值抑制
		# 使用极大值抑制的方法可以解决检测到的特征点相连的问题
		# 1. 对所有检测到到特征点构建一个打分函数V。V 就是像素点p 与周围16
		# 个像素点差值的绝对值之和。
		# 2. 计算临近两个特征点的打分函数V。
		# 3. 忽略V 值最低的特征点

		# FAST 算法比其它角点检测算法都快。
		# 但是在噪声很高时不够稳定，这是由阈值决定的。
		print("")

	def test_345(self):
		#34.5OpenCV中FAST特征检测器
		img = cv2.imread('simple.jpg', 0)
		# Initiate FAST object with default values
		fast = cv2.FastFeatureDetector()
		# find and draw the keypoints
		kp = fast.detect(img, None)
		img2 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))
		# Print all default params
		print("Threshold: ", fast.getInt('threshold'))
		print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
		print("neighborhood: ", fast.getInt('type'))
		print("Total Keypoints with nonmaxSuppression: ", len(kp))
		cv2.imwrite('fast_true.png', img2)
		# Disable nonmaxSuppression
		fast.setBool('nonmaxSuppression', 0)
		kp = fast.detect(img, None)
		print("Total Keypoints without nonmaxSuppression: ", len(kp))
		img3 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))
		cv2.imwrite('fast_false.png', img3)
		print("")

