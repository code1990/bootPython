# NumPy 矩阵库(Matrix)
# NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。

# matlib.empty()
# matlib.empty() 函数返回一个新的矩阵，语法格式为
import numpy.matlib
import numpy as np

# # 填充为随机数据
print(np.matlib.empty((2, 2)))
# numpy.matlib.zeros()
# numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵
print(np.matlib.zeros((2, 2)))
# numpy.matlib.ones()
# numpy.matlib.ones()函数创建一个以 1 填充的矩阵。
print(np.matlib.ones((2, 2)))
# numpy.matlib.eye()
# numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零
print(np.matlib.eye(n=3, M=4, k=0, dtype=float))
# numpy.matlib.identity()
# numpy.matlib.identity() 函数返回给定大小的单位矩阵。
print(np.matlib.identity(5, dtype=float))
# numpy.matlib.rand()
# numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
print(np.matlib.rand(2, 3))
#
i = np.matrix("1,2;3,4")
print(i)

j = np.asarray(i)
print(j)
k = np.asarray(j)
print(k)
