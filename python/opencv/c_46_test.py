import unittest
# • 本节我们要理解k 近邻（kNN）的基本概念。
# kNN 可以说是最简单的监督学习分类器
import cv2
import numpy as np
import matplotlib.pyplot as plt
class c_46_test(unittest.TestCase):
	def test_461(self):
		#46.1理解K近邻
		# Feature set containing (x,y) values of 25 known/training data
		trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
		# Labels each one either Red or Blue with numbers 0 and 1
		responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)
		# Take Red families and plot them
		red = trainData[responses.ravel() == 0]
		plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
		# Take Blue families and plot them
		blue = trainData[responses.ravel() == 1]
		plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')
		plt.show()
		newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
		plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')
		knn = cv2.KNearest()
		knn.train(trainData, responses)
		ret, results, neighbours, dist = knn.find_nearest(newcomer, 3)
		print("result: ", results, "\n")
		print("neighbours: ", neighbours, "\n")
		print("distance: ", dist)
		plt.show()
		print("")

		#46.1.1OpenCV中的kNN
	def test_462(self):
		# 46.2.1手写数字的OCR
		#46.2使用kNN对手写数字OCR
		# • 要根据我们掌握的kNN 知识创建一个基本的OCR 程序
		# • 使用OpenCV 自带的手写数字和字母数据测试我们的程序
		img = cv2.imread('digits.png')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# Now we split the image to 5000 cells, each 20x20 size
		cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
		# Make it into a Numpy array. It size will be (50,100,20,20)
		x = np.array(cells)
		# Now we prepare train_data and test_data.
		train = x[:, :50].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
		test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
		# Create labels for train and test data
		k = np.arange(10)
		train_labels = np.repeat(k, 250)[:, np.newaxis]
		test_labels = train_labels.copy()
		# Initiate kNN, train the data, then test it with test data for k=1
		knn = cv2.KNearest()
		knn.train(train, train_labels)
		ret, result, neighbours, dist = knn.find_nearest(test, k=5)
		# Now we check the accuracy of classification
		# For that, compare the result with test_labels and check which are wrong
		matches = result == test_labels
		correct = np.count_nonzero(matches)
		accuracy = correct * 100.0 / result.size
		print(accuracy)
		np.savez('knn_data.npz', train=train, train_labels=train_labels)
		# Now load the data
		with np.load('knn_data.npz') as data:
			print(data.files)
			train = data['train']
			train_labels = data['train_labels']
		print("")


		#46.2.2英文字母的OCR
	def test_11(self):
		# Load the data, converters convert the letter to a number
		data = np.loadtxt('letter-recognition.data', dtype='float32', delimiter=',',
		                  converters={0: lambda ch: ord(ch) - ord('A')})
		# split the data to two, 10000 each for train and test
		train, test = np.vsplit(data, 2)
		# split trainData and testData to features and responses
		responses, trainData = np.hsplit(train, [1])
		labels, testData = np.hsplit(test, [1])
		# Initiate the kNN, classify, measure accuracy.
		knn = cv2.KNearest()
		knn.train(trainData, responses)
		ret, result, neighbours, dist = knn.find_nearest(testData, k=5)
		correct = np.count_nonzero(result == labels)
		accuracy = correct * 100.0 / 10000
		print(accuracy)

