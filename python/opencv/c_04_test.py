import unittest
import numpy as np
import cv2
from matplotlib import pyplot as plt

class c_04_test(unittest.TestCase):
    def test_41(self):
        # 4.1读入图像
        # 使用函数cv2.imread() 读入图像。这幅图像应该在此程序的工作路径，    # 或者给函数提供完整路径，
        # 第二个参数是要告诉函数应该如何读取这幅图片。
        # • cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略， # 这是默认参数。
        # • cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
        # cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的alpha 通道
        img = cv2.imread('python.png', 0)
        print(img)
        print(type(img))

    def test_42(self):
        # 4.2显示图像
        img = cv2.imread("python.png", 0)
        # 使用函数cv2.imshow() 显示图像。窗口会自动调整为图像大小。
        # 第一个参数是窗口的名字，其次才是我们的图像
        cv2.imshow("windowName", img)
        # cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫秒级
        # 如果没	有键盘输入，返回值为-1，如果我们设置这个函数的参数为0，那它将会无限期的等待键盘输入
        cv2.waitKey(0)
        # cv2.destroyAllWindows() 可以轻易删除任何我们建立的窗口。如果
        # 你想删除特定的窗口可以使用cv2.destroyWindow()，在括号内输入你想删
        # 除的窗口名。
        cv2.destroyAllWindows()

    def test_421(self):
        img = cv2.imread("python.png", 0)
        cv2.namedWindow("testwindow", cv2.WINDOW_NORMAL)
        cv2.imshow("testwindow", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_43(self):
        # 4.3保存图像
        # 使用函数cv2.imwrite() 来保存一个图像。首先需要一个文件名，之后才
        # 是你要保存的图像。
        img = cv2.imread("python_copy.png",0)
        cv2.imwrite("1.png",img)

    def test_summary(self):
        img = cv2.imread("python.png",0)
        cv2.imshow("summary_window",img)
        k = cv2.waitKey(0)
        if k==27:#esc
            cv2.destroyAllWindows()
        elif k==ord('s'):
            cv2.imwrite("python_copy.png",img)
            cv2.destroyAllWindows()

    def test_sreencut(self):
        # 彩色图像使用OpenCV 加载时是BGR 模式。
        # 但是Matplotib 是RGB模式
        img = cv2.imread("python.png",0)
        plt.imshow(img,cmap="gray",interpolation="bicubic")
        # 隐藏X和Y轴上的刻度值
        plt.xticks([]),plt.yticks([])
        plt.show()
