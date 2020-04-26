import unittest
import numpy as np
import cv2


class c_05_test(unittest.TestCase):
	def test_51(self):
		# 5.1用摄像头捕获视频
		# 为了获取视频，你应该创建一个VideoCapture 对象。他的参数可以是
		# 设备的索引号，或者是一个视频文件。设备索引号就是在指定要使用的摄像头。
		# 一般的笔记本电脑都有内置摄像头。所以参数就是0。你可以通过设置成1 或
		# 者其他的来选择别的摄像头
		cap = cv2.VideoCapture(0)
		while (True):
			# ＃ 逐帧捕获
			# cap.read() 返回一个布尔值（True/False）。如果帧读取的是正确的，就是True
			# 使用cap.isOpened()，来检查是否成功初始化了。
			# 如果返回值是True，那就没有问题。否则就要使用函数cap.open()。
			# 使用函数cap.get(propId) 来获得视频的一些参数信息
			# 使用cap.set(propId,value) 来修改，value 就是你想要设置成的新值。
			# 使用cap.get(3) 和cap.get(4) 来查看每一帧的宽和高。默认情况下得到的值是640X480。
			# 可以使用ret=cap.set(3,320)和ret=cap.set(4,240) 来把宽和高改成320X240。
			ret, frame = cap.read()
			# ＃ 我们在框架上的操作来到这里
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# ＃ 显示结果帧
			cv2.imshow('frame', gray)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		# ＃ 完成所有操作后，释放捕获
		cap.release()
		cv2.destroyAllWindows()

	# 确保你已经装了合适版本的ffmpeg 或者gstreamer。
	def test_52(self):
		# # 5.2从文件中播放视频
		# 在播放每一帧时，使用cv2.waiKey() 设置适当的持续时间
		# 通常情况下25 毫秒就可以
		cap = cv2.VideoCapture(0)
		## ＃定义编解码器并创建VideoWriter对象
		fourcc = cv2.VideoWriter(*'XVID')
		out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 470))
		while True:
			ret, frame = cap.read()
			if ret == True:
				frame = cv2.flip(frame, 0)
				# ＃写翻转的框架
				out.write(frame)
				cv2.imshow('frame', frame)
				# ＃完成工作后释放所有内容
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			else:
				break
		cap.release()
		out.release()
		cv2.destroyAllWindows()

	def test_53(self):
		# 5.3保存视频
		# 要创建一个VideoWriter 的对象。我们应该确定一个输出文件的名字。
		# 接下来指定FourCC 编码（下面会介绍）。播放频率和帧的大小也都需要确定。
		# 最后一个是isColor 标签。如果是True，每一帧就是彩色图，否则就是灰度图。
		# FourCC 就是一个4 字节码，用来确定视频的编码格式。可用的编码列表可以从fourcc.org查到
		# In Windows: DIVX
		cap = cv2.VideoCapture(0)
		# 13＃定义编解码器并创建VideoWriter对象
		fourcc = cv2.cv.FOURCC(*'XVID')
		out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
		while(cap.isOpened()):
			ret,frame = cap.read()
			if ret==True:
				frame=cv2.flip(frame,0)
				# 22＃编写翻转的框架
				out.write(frame)

				cv2.imshow('frame',frame)
				if cv2.waitKey(1) & 0xFF==ord('q'):
					break
			else:
				break
		# 31＃如果作业完成，则释放所有内容
		cap.release()
		out.release()
		cv2.destroyAllWindows()
