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
# 维度	描述
# broadcast	产生模仿广播的对象
# broadcast_to	将数组广播到新形状
# expand_dims	扩展数组的形状
# squeeze	从数组的形状中删除一维条目
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

b = np.broadcast(x, y)
print(b)

print('对 y 广播 x：')
r, c = b.iters

# Python3.x 为 next(context) ，
# Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))
print('广播对象的形状：')
print(b.shape)
print('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x, y)
c = np.empty(b.shape)

print('手动使用 broadcast 将 x 与 y 相加：')
print(c.shape)
print('\n')
c.flat = [u + v for (u, v) in b]

print('调用 flat 函数：')
print(c)
print('\n')
# 获得了和 NumPy 内建的广播支持相同的结果

print('x 与 y 的和：')
print(x + y)

# numpy.broadcast_to
# numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。
a = np.arange(4).reshape(1, 4)
print(a)
print(np.broadcast_to(a, (4, 4)))

# numpy.expand_dims
# numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状，函数格式如下:
x = np.array(([1, 2], [3, 4]))
print(x)
y = np.expand_dims(x, axis=0)
print(y)
print(x.shape, y.shape)
y = np.expand_dims(x, axis=1)
print(y)
print(x.ndim, y.ndim)

# numpy.squeeze
# numpy.squeeze 函数从给定数组的形状中删除一维的条目，函数格式如下：
x = np.arange(9).reshape(1, 3, 3)
print(x)
y = np.squeeze(x)
print(y)
print(x.shape, y.shape)
# 连接数组
# 函数	描述
# concatenate	连接沿现有轴的数组序列
# stack	沿着新的轴加入一系列数组。
# hstack	水平堆叠序列中的数组（列方向）
# vstack	竖直堆叠序列中的数组（行方向）
# numpy.concatenate
# numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.concatenate((a, b)))
print(np.concatenate((a, b), axis=1))

# numpy.stack
# numpy.stack 函数用于沿新轴连接数组序列，格式如下：
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.stack((a, b), 0))
print(np.stack((a, b), 1))

# numpy.hstack
# numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
print('水平堆叠：')
c = np.hstack((a, b))
print(c)
# numpy.vstack
# numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
print('竖直堆叠：')
c = np.vstack((a, b))
print(c)

# 分割数组
# 函数	数组及操作
# split	将一个数组分割为多个子数组
# hsplit	将一个数组水平分割为多个子数组（按列）
# vsplit	将一个数组垂直分割为多个子数组（按行）
# numpy.split
# numpy.split 函数沿特定的轴将数组分割为子数组，

a = np.arange(9)
b = np.split(a, 3)
print(b)
b = np.split(a, [4, 7])
print(b)
# numpy.hsplit
# numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
harr = np.floor(10 * np.random.random((2, 6)))
print('原array：')
print(harr)

print('拆分后：')
print(np.hsplit(harr, 3))

# numpy.vsplit
# numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同。
a = np.arange(16).reshape(4, 4)
print('竖直分割：')
b = np.vsplit(a, 2)
print(b)

# 数组元素的添加与删除
# 函数	元素及描述
# resize	返回指定形状的新数组
# append	将值添加到数组末尾
# insert	沿指定轴将值插入到指定下标之前
# delete	删掉某个轴的子数组，并返回删除后的新数组
# unique	查找数组内的唯一元素
# numpy.resize
# numpy.resize 函数返回指定大小的新数组。

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)
b = np.resize(a, (3, 2))
print(b)
# numpy.append
# numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。

a = np.array([[1, 2, 3], [4, 5, 6]])
print('向数组添加元素：')
print(np.append(a, [7, 8, 9]))
print('\n')

print('沿轴 0 添加元素：')
print(np.append(a, [[7, 8, 9]], axis=0))
print('\n')

print('沿轴 1 添加元素：')
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

# numpy.insert
# numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。

a = np.array([[1, 2], [3, 4], [5, 6]])
print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print('\n')
print('传递了 Axis 参数。 会广播值数组来配输入数组。')

print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print('\n')

print('沿轴 1 广播：')
print(np.insert(a, 1, 11, axis=1))

# numpy.delete
# numpy.delete 函数返回从输入数组中删除指定子数组的新数组

a = np.arange(12).reshape(3, 4)

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('\n')

print('删除第二列：')
print(np.delete(a, 1, axis=1))
print('\n')

print('包含从数组中删除的替代值的切片：')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))

# numpy.unique
# numpy.unique 函数用于去除数组中的重复元素。
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

print('第一个数组的去重值：')
u = np.unique(a)
print(u)

print('去重数组的索引数组：')
u, indices = np.unique(a, return_index=True)
print(indices)

print('我们可以看到每个和原数组下标对应的数值：')
print(a)

print('去重数组的下标：')
u, indices = np.unique(a, return_inverse=True)
print(u)

print('下标为：')
print(indices)

print('使用下标重构原数组：')
print(u[indices])

print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)
