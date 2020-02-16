# Numpy 数组操作
# Numpy 中包含了一些函数用于处理数组，大概可分为以下几类：
#
# 修改数组形状
# reshape	不改变数据的条件下修改形状
# flat	数组元素迭代器
# flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# ravel	返回展开数组
# 翻转数组
# transpose	对换数组的维度
# ndarray.T	和 self.transpose() 相同
# rollaxis	向后滚动指定的轴
# swapaxes	对换数组的两个轴
# 修改数组维度
# broadcast	产生模仿广播的对象
# broadcast_to	将数组广播到新形状
# expand_dims	扩展数组的形状
# squeeze	从数组的形状中删除一维条目
# 连接数组
# concatenate	连接沿现有轴的数组序列
# stack	沿着新的轴加入一系列数组。
# hstack	水平堆叠序列中的数组（列方向）
# vstack	竖直堆叠序列中的数组（行方向）
# 分割数组
# split	将一个数组分割为多个子数组
# hsplit	将一个数组水平分割为多个子数组（按列）
# vsplit	将一个数组垂直分割为多个子数组（按行）
# 数组元素的添加与删除
# resize	返回指定形状的新数组
# append	将值添加到数组末尾
# insert	沿指定轴将值插入到指定下标之前
# delete	删掉某个轴的子数组，并返回删除后的新数组
# unique	查找数组内的唯一元素

# numpy.reshape
# numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')
import numpy as np

a = np.arange(8)
print(a)
b = a.reshape(4, 2)
print(b)

# numpy.ndarray.flat
# numpy.ndarray.flat 是一个数组元素迭代器，实例如下:
a = np.arange(9).reshape(3)
print(a)
for row in a:
    print(row)

for element in a.flat:
    print(element)

# numpy.ndarray.flatten
# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
a = np.arange(8).reshape(2, 4)
print(a)
print(a.flattern())
print(a.flatten(order='F'))

# numpy.ravel
# numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（
a = np.arange(8).reshape(2, 4)
print(a)
print(a.ravel())
print(a.ravel(order="F"))

# numpy.transpose
# numpy.transpose 函数用于对换数组的维度，格式如下：
a = np.arange(12).reshape(3, 4)
print(a)
print(np.transpose(a))
# numpy.ndarray.T 类似 numpy.transpose：
print(a.T)

# numpy.rollaxis
# numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
a = np.arange(8).reshape(2, 2, 2)
print(a)
# # 将轴 2 滚动到轴 0（宽度到深度）
print(np.rollaxis(a, 2))
print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2, 1))

# numpy.swapaxes
# numpy.swapaxes 函数用于交换数组的两个轴，格式如下：
a = np.arange(8).reshape(2, 2, 2)
print(a)
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
print('调用 swapaxes 函数后的数组：')
print(np.swapaxesa, 2, 0)

# 修改数组维度
