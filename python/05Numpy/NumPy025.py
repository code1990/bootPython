# NumPy Matplotlib
# Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。

# Windows 系统安装 Matplotlib
#
# 进入到 cmd 窗口下，执行以下命令：
#
# python -m pip install -U pip setuptools
# python -m pip install matplotlib
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("demo")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()
# 图形中文显示
# Matplotlib 默认情况不支持中文，我们可以使用以下简单的方法来解决：
import numpy as np
from matplotlib import pyplot as plt
# from matplotlib


# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.plot(x, y)
plt.show()
# 绘制正弦波
# 以下实例使用 matplotlib 生成正弦波图。
x=np.arange(1,11)
y=2*x+5
plt.title("demo")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,"ob")
plt.show()

x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.title("123")
plt.plot(x,y)
plt.show()
# subplot()
# subplot() 函数允许你在同一图中绘制不同的东西。
# 以下实例绘制正弦和余弦值:
x=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title("sin")
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()
# bar()
# pyplot 子模块提供 bar() 函数来生成条形图。
#
# 以下实例生成两组 x 和 y 数组的条形图。
x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x,y,align="center")
plt.bar(x2,y2,color="g",align="center")
plt.title("demo")
plt.ylabel(y)
plt.xlabel(x)
plt.show()

# numpy.histogram()
# numpy.histogram() 函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
#
# numpy.histogram()函数将输入数组和 bin 作为两个参数。 bin 数组中的连续元素用作每个 bin 的边界。
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
np.histogram(a,bins =  [0,20,40,60,80,100])
hist,bins = np.histogram(a,bins =  [0,20,40,60,80,100])
print (hist)
print (bins)
# plt()
# Matplotlib 可以将直方图的数字表示转换为图形。 pyplot 子模块的 plt() 函数将包含数据和 bin 数组的数组作为参数，并转换为直方图。
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a, bins =  [0,20,40,60,80,100])
plt.title("histogram")
plt.show()