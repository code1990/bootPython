# import linecache
# import threading
# import win32api as api
# import wx
# import random
# import tkinter
# from tkinter import ttk
# from tkinter import *
# import sys
#
#
# class WorkerThread(threading.Thread):
# 	def __init__(self, frame):
# 		threading.Thread.__init__(self)
# 		self.frame = frame
# 		self.timeToQuit = threading.Event()
# 		self.timeToQuit.clear()
# 		self.system_mouse_pos = api.GetCursorPos()
#
# 	def run(self):
# 		鼠窗坐标差_x = self.system_mouse_pos[0] - self.frame.GetPosition()[0]
# 		鼠窗坐标差_y = self.system_mouse_pos[1] - self.frame.GetPosition()[1]
# 		while 1:
# 			self.timeToQuit.wait(0.02)
# 			if self.timeToQuit.isSet():
# 				break
# 			self.system_mouse_pos = api.GetCursorPos()
# 			frame_pos_x = self.system_mouse_pos[0] - 鼠窗坐标差_x
# 			frame_pos_y = self.system_mouse_pos[1] - 鼠窗坐标差_y
# 			frame_pos = (frame_pos_x, frame_pos_y)
# 			wx.CallAfter(self.frame.move_start, frame_pos)
# 		else:
# 			wx.CallAfter(self.frame.move_stop, self)
#
#
# class MyFrame(wx.Frame):
# 	def __init__(self, parent, ):
# 		wx.Frame.__init__(self, parent, )
# 		wx.Frame.__init__(self, parent, size=(120, 130), style=wx.CAPTION | wx.STAY_ON_TOP)
# 		self.threads = []
# 		self.Bind(wx.EVT_CLOSE, self.evt_close)
#
# 		global panel
# 		panel = wx.Panel(self)
# 		panel.Bind(wx.EVT_RIGHT_DOWN, self.evt_left_down)
# 		panel.Bind(wx.EVT_RIGHT_UP, self.evt_left_up)
# 		panel.Bind(wx.EVT_LEFT_DOWN, self.changevoc)
# 		self.SetTransparent(500)  # 设置透明
# 		global lbl
# 		lbl = wx.StaticText(panel, -1, )
# 		# 读取单词并显示
# 		global file
# 		file = open('voc.txt', 'rb')
# 		global count1
# 		count1 = len(file.readlines())
# 		global count
# 		print('myframe')
#
# 	def changevoc(self, event):
# 		lbl.Bind(wx.EVT_RIGHT_DOWN, self.evt_left_down)
# 		lbl.Bind(wx.EVT_RIGHT_UP, self.evt_left_up)
# 		lbl.Bind(wx.EVT_LEFT_DOWN, self.changevoc)
# 		print('123')
# 		# 获取行数
# 		font = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
# 		lbl.SetFont(font)
# 		lbl.SetForegroundColour("Red")
# 		num1 = random.randrange(1, count1, 1)  # 生成随机行数
# 		global txt
# 		txt = linecache.getline('voc.txt', num1)  # 随机读取某行
# 		fuwu = txt.split(' ', 2)[0]
# 		voc = txt.split(' ', 2)[1]
# 		trans = txt.split(' ', 2)[2]
# 		if len(trans) > 5:
# 			a = trans[0:9]
# 			b = trans[9:18]
# 			c = trans[18:len(trans)]
# 			trans = a + '\n' + b + '\n' + c
# 		text = voc + '\n' + trans
# 		# text = wx.StaticText(panel, wx.ID_ANY, "设置文本font", (20, 100))
#
# 		# lbl.SetForegroundColour((255, 0, 0))
# 		lbl.SetFont(font)
# 		lbl.SetLabel(text)
#
# 	def evt_close(self, event):
# 		while self.threads:
# 			thread = self.threads[0]
# 			thread.timeToQuit.set()
# 			self.threads.remove(thread)
# 		self.Destroy()
# 		file.closed
# 		sys.exit()
#
# 	def evt_left_down(self, event):
# 		thread = WorkerThread(self)
# 		self.threads.append(thread)
# 		thread.start()
#
# 	def evt_left_up(self, event):
# 		if self.threads:
# 			self.threads[0].timeToQuit.set()
# 			self.threads.remove(self.threads[0])
#
# 	def move_start(self, frame_pos):
# 		# wx.MilliSleep(2)
# 		self.SetPosition(frame_pos)
#
# 	def move_stop(self, thread):
# 		self.threads.remove(thread)
#
#
# def main():
# 	app = wx.App()
# 	frame = MyFrame(None)
# 	frame.Show()
# 	app.MainLoop()
#
#
# if __name__ == "__main__":
# 	main()