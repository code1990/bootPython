# NumPy 从数值范围创建数组
# numpy.arange
# numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：
import numpy as np

x = np.arange(5)
print(x)

# 设置返回值为float类型
x = np.arange(5, dtype=float)
print(x)

# 设置起始位置 设置步长
x = np.arange(10, 20, 2)
print(x)

# numpy.linspace
# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
a = np.linspace(1, 10, 10)
print(a)
a = np.linspace(1, 1, 10)
print(a)

# 将 endpoint 设为 false，不包含终止值：
a = np.linspace(10, 20, 5, endpoint=False)
print(a)

# 设置间距问题
a = np.linspace(1, 10, 10, retstep=True)
print(a)
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)

# numpy.logspace
# numpy.logspace 函数用于创建一个于等比数列。格式如下：
# 默认底数为10
a=np.logspace(1.0,2.0,num=10)
print(a)

a=np.logspace(0,9,10,base=2)
print(a)