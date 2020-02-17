# NumPy 副本和视图
# 副本是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置。
#
# 视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。
#
# 视图一般发生在：
#
# 1、numpy 的切片操作返回原数据的视图。
# 2、调用 ndarray 的 view() 函数产生一个视图。
# 副本一般发生在：
#
# Python 序列的切片操作，调用deepCopy()函数。
# 调用 ndarray 的 copy() 函数产生一个副本。
# 无复制
# 简单的赋值不会创建数组对象的副本。
import numpy as np

# id()返回 Python 对象的通用标识符，类似于 C 中的指针。
a = np.arange(6)
print(a)
print(id(a))
b = a
print(b)
print(id(b))
b.shape = 3, 2
print(b)
print(a)
print(id(a))
print(id(b))

# 视图或浅拷贝
# ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数。
a = np.arange(6).reshape(3, 2)
print(a)
b = a.view()
print(a)
print(id(a))
print(id(b))
b.shape = 3, 2
print(b)
print(a)
print(id(a))
print(id(b))
# 使用切片创建视图修改数据会影响到原始数组：
arr = np.arange(12)
print(arr)
b = arr[3:]
a = arr[3:]
print(b)
print(a)
a[1] = 123
b[2] = 234
print(arr)
print(id(a), id(b), id(arr[3:]))

# 副本或深拷贝
# ndarray.copy() 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。
a = np.array([[10, 10], [2, 3], [4, 5]])
print(a)
b = a.copy()
print(b)
print(b is a)
b[0, 0] = 100
print(b)
