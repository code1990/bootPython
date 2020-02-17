# NumPy ufunc通用函数
# NumPy 提供了两种基本的对象，即 ndarray 和 ufunc 对象。前面几节已经介绍了 ndarray，本节将介绍 Numpy。
# ufunc 是 universal function 的缩写，意思是“通用函数”，
# 它是一种能对数组的每个元素进行操作的函数。
# ufun 比 math 模块中的函数更灵活。
# math 模块的输入一般是标量，但 NumPy 中的函数可以是向量或矩阵，
# 而利用向量或矩阵可以避免使用循环语句，这点在机器学习、深度学习中非常重要。

# math 与 numpy 函数的性能比较
import time
import math
import numpy as np

x = [i * 0.001 for i in np.arange(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print(time.clock() - start)

x = [i * 0.001 for i in np.arange(1000000)]
start = time.clock()
x = np.array(x)
np.sin(x)
print(time.clock() - start)

# 循环与向量运算比较
# 如下使用的向量化要比使用循环计算速度快得多
x1 = np.random.rand(10000)
x2 = np.random.rand(10000)
# 使用循环计算向量点积
tic = time.process_time()
dot = 0
for i in range(len(x1)):
    dot += x1[i] * x2[i]
toc = time.process_time()
print(tic - toc)

tic = time.process_time()
dot = 0
dot = np.dot(x1, x2)
toc = time.process_time()
print(tic - toc)
