import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt
# GrabCut 算法原理，使用GrabCut 算法提取图像的前景
# • 创建一个交互是程序完成前景提取
class c_28_test(unittest.TestCase):
	def test_281(self):
		#28.1演示
		img = cv2.imread('messi5.jpg')
		mask = np.zeros(img.shape[:2], np.uint8)
		bgdModel = np.zeros((1, 65), np.float64)
		fgdModel = np.zeros((1, 65), np.float64)
		rect = (50, 50, 450, 290)
		# 函数的返回值是更新的mask, bgdModel, fgdModel
		cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
		mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
		img = img * mask2[:, :, np.newaxis]
		plt.imshow(img), plt.colorbar(), plt.show()
		# newmask is the mask image I manually labelled
		newmask = cv2.imread('newmask.png', 0)
		# whereever it is marked white (sure foreground), change mask=1
		# whereever it is marked black (sure background), change mask=0
		mask[newmask == 0] = 0
		mask[newmask == 255] = 1
		mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
		mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
		img = img * mask[:, :, np.newaxis]
		plt.imshow(img), plt.colorbar(), plt.show()
		print("")

