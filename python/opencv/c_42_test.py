import unittest
import numpy as np
import cv2
import glob


# • 学习摄像机畸变以及摄像机的内部参数和外部参数
# • 学习找到这些参数，对畸变图像进行修复
class c_42_test(unittest.TestCase):
	def test_421(self):
		# 42.1基础
		print("")

	def test_422(self):
		# 42.2代码
		# termination criteria
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
		objp = np.zeros((6 * 7, 3), np.float32)
		objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
		# Arrays to store object points and image points from all the images.
		objpoints = []  # 3d point in real world space
		imgpoints = []  # 2d points in image plane.
		images = glob.glob('*.jpg')
		for fname in images:
			img = cv2.imread(fname)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			# Find the chess board corners
			ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
			# If found, add object points, image points (after refining them)
			if ret == True:
				objpoints.append(objp)
				corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
				imgpoints.append(corners2)
				# Draw and display the corners
				img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
				cv2.imshow('img', img)
				cv2.waitKey(500)
		cv2.destroyAllWindows()
		# 42.2.1设置
		# 42.2.2标定
		# 42.2.3畸变校正
		# 标定
		ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
		# 我们读取一个新的图像（left2.ipg）
		img = cv2.imread('left12.jpg')
		h, w = img.shape[:2]
		newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
		# 使用cv2.undistort() 这是最简单的方法。只需使用这个函数和上边得到
		# 的ROI 对结果进行裁剪。
		# undistort
		dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
		# crop the image
		x, y, w, h = roi
		dst = dst[y:y + h, x:x + w]
		cv2.imwrite('calibresult.png', dst)
		# 使用remapping
		# 这应该属于“曲线救国”了。首先我们要找到从畸变图像到
		# 非畸变图像的映射方程。再使用重映射方程。
		# undistort
		mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
		dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
		# crop the image
		x, y, w, h = roi
		dst = dst[y:y + h, x:x + w]
		cv2.imwrite('calibresult.png', dst)
		print("")


	def test_423(self):
		# 42.3反向投影误差
		print("")
