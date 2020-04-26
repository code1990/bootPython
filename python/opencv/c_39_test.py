import unittest
import numpy as np
import cv2

# 本节我们要学习使用Meanshift 和Camshift 算法在视频中找到并跟踪
# 目标对象
class c_39_test(unittest.TestCase):
	def test_391(self):
		# 39.1Meanshift
		# 要在OpenCV 中使用Meanshift 算法首先我们要对目标对象进行设置，
		# 计算目标对象的直方图，这样在执行meanshift 算法时我们就可以将目标对
		# 象反向投影到每一帧中去了。另外我们还需要提供窗口的起始位置。在这里我
		# 们值计算H（Hue）通道的直方图，同样为了避免低亮度造成的影响，我们使
		# 用函数cv2.inRange() 将低亮度的值忽略掉
		print("")

	def test_392(self):
		# 39.2OpenCV中的Meanshift
		cap = cv2.VideoCapture('slow.flv')
		# take first frame of the video
		ret, frame = cap.read()
		# setup initial location of window
		r, h, c, w = 250, 90, 400, 125  # simply hardcoded the values
		track_window = (c, r, w, h)
		# set up the ROI for tracking
		roi = frame[r:r + h, c:c + w]
		hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
		roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
		cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
		# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
		term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
		while (1):
			ret, frame = cap.read()
			if ret == True:
				hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
				dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
				# apply meanshift to get the new location
				ret, track_window = cv2.meanShift(dst, track_window, term_crit)
				# Draw it on image
				x, y, w, h = track_window
				img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
				cv2.imshow('img2', img2)
				k = cv2.waitKey(60) & 0xff
				if k == 27:
					break
				else:
					cv2.imwrite(chr(k) + ".jpg", img2)
			else:
				break
		cv2.destroyAllWindows()
		cap.release()
		print("")


	def test_393(self):
		# 39.3Camshift
		# 39.4OpenCV中的Camshift
		# 这个算法首先要使用meanshift，meanshift 找到（并覆盖）目标之后，
		# 再去调整窗口的大小，s = 2x
		# √
		# M00
		# 256 。它还会计算目标对象的最佳外接椭圆的
		# 角度，并以此调节窗口角度。然后使用更新后的窗口大小和角度来在原来的位
		# 置继续进行meanshift。重复这个过程知道达到需要的精度。
		print("")


	def test_394(self):
		cap = cv2.VideoCapture('slow.flv')
		# take first frame of the video
		ret, frame = cap.read()
		# setup initial location of window
		r, h, c, w = 250, 90, 400, 125  # simply hardcoded the values
		track_window = (c, r, w, h)
		# set up the ROI for tracking
		roi = frame[r:r + h, c:c + w]
		hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
		roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
		cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
		# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
		term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
		while (1):
			ret, frame = cap.read()
			if ret == True:
				hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
				dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
				# apply meanshift to get the new location
				ret, track_window = cv2.CamShift(dst, track_window, term_crit)
				# Draw it on image
				pts = cv2.boxPoints(ret)
				pts = np.int0(pts)
				img2 = cv2.polylines(frame, [pts], True, 255, 2)
				cv2.imshow('img2', img2)
				k = cv2.waitKey(60) & 0xff
				if k == 27:
					break
				else:
					cv2.imwrite(chr(k) + ".jpg", img2)
			else:
				break
		cv2.destroyAllWindows()
		cap.release()
		print("")

