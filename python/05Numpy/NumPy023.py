# NumPy 线性代数
# NumPy 提供了线性代数函数库 linalg，该库包含了线性代数所需的所有功能，可以看看下面的说明：
#
# 函数	描述
# dot	两个数组的点积，即元素对应相乘。
# vdot	两个向量的点积
# inner	两个数组的内积
# matmul	两个数组的矩阵积
# determinant	数组的行列式
# solve	求解线性矩阵方程
# inv	计算矩阵的乘法逆矩阵
import numpy.matlib
import numpy as np

# numpy.dot()
# numpy.dot() 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b))
# numpy.vdot()
# numpy.vdot() 函数是两个向量的点积
print(np.vdot(a, b))
# numpy.inner()
# numpy.inner() 函数返回一维数组的向量内积。
print(np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[1, 2], [3, 4]])
print(b)
print(np.inner(a, b))
# numpy.matmul
# numpy.matmul 函数返回两个数组的矩阵乘积。
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
print(np.matmul(a, b))
a = [[1, 0], [0, 1]]
b = [1, 2]
print(np.matmul(a, b))
print(np.matmul(b, a))
a = np.arange(8).reshape(2, 2, 2)
b = np.arange(4).reshape(2, 2)
print(np.matmul(a, b))
# numpy.linalg.det()
# numpy.linalg.det() 函数计算输入矩阵的行列式。
a = np.array([[1, 2], [3, 4]])

print(np.linalg.det(a))
b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(b)
print(np.linalg.det(b))
# numpy.linalg.solve()
# numpy.linalg.solve() 函数给出了矩阵形式的线性方程的解。
a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])

print('数组 a：')
print(a)
ainv = np.linalg.inv(a)

print('a 的逆：')
print(ainv)

print('矩阵 b：')
b = np.array([[6], [-4], [27]])
print(b)

print('计算：A^(-1)B：')
x = np.linalg.solve(a, b)
print(x)
# 这就是线性方向 x = 5, y = 3, z = -2 的解
# numpy.linalg.inv()
# numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵。
x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))
a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])

print('数组 a：')
print(a)
ainv = np.linalg.inv(a)

print('a 的逆：')
print(ainv)

print('矩阵 b：')
b = np.array([[6], [-4], [27]])
print(b)

print('计算：A^(-1)B：')
x = np.linalg.solve(a, b)
print(x)
