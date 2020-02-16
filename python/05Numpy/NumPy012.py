# NumPy 迭代数组
# NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。
#
# 迭代器最基本的任务的可以完成对数组元素的访问。
#
# 接下来我们使用 arange() 函数创建一个 2X3 数组，并使用 nditer 对它进行迭代。
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
for x in np.nditer(a):
    print(x, end=", ")
print("\n")

for x in np.nditer(a.T):
    print(x, end=", ")
print("\n")

for x in np.nditer(a.T.copy(order="C")):
    print(x, end=", ")
print("\n")

# 控制遍历顺序
# for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
# for x in np.nditer(a.T, order='C'):C order，即是行序优先；
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
b = a.T
print(b)
c = b.copy(order="C")
print(c)
for x in np.nditer(c):
    print(x, end=", ")
print("\n")
c = b.copy(order="F")
for x in np.nditer(c):
    print(x, end=", ")
print("\n")

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
for x in np.nditer(a, order="C"):
    print(x, end=", ")

for x in np.nditer(a, order="F"):
    print(x, end=", ")

# 修改数组中元素的值
# nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only）
for x in np.nditer(a, op_flags=["readwrite"]):
    x[...] = 2 * x
print(a)

# 使用外部循环
# nditer类的构造器拥有flags参数，它可以接受下列值：
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=", ")

# 广播迭代
# 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')
print('修改后的数组为：')
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=", ")
