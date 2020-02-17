# NumPy 排序、条件刷选函数
# NumPy 提供了多种排序的方法。
#
# 种类	速度	最坏情况	工作空间	稳定性
# 'quicksort'（快速排序）	1	O(n^2)	0	否
# 'mergesort'（归并排序）	2	O(n*log(n))	~n/2	是
# 'heapsort'（堆排序）	3	O(n*log(n))	0	否
import numpy as np

# numpy.sort()
# numpy.sort() 函数返回输入数组的排序副本。函数格式如下：
a = np.array([[1, 2], [3, 4]])
print(a)
print(np.sort(a))
print(np.sort(a, axis=0))
dt = np.dtype([("name", "S10"), ("age", int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print(a)
print(np.sort(a, order="name"))
# numpy.argsort()
# numpy.argsort() 函数返回的是数组值从小到大的索引值。
x = np.array([3, 2, 1])
print(x)
y = np.argsort(x)
print(x)
print(y)
print(x[y])
for i in y:
    print(x[i], end=" ")
# numpy.lexsort()
# numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print(ind)
print(nm[i] + "," + dv[i] for i in ind)

# msort、sort_complex、partition、argpartition
# 函数	描述
# msort(a)	数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。
# sort_complex(a)	对复数按照先实部后虚部的顺序进行排序。
# partition(a, kth[, axis, kind, order])	指定一个数，对数组进行分区
# argpartition(a, kth[, axis, kind, order])	可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
print(np.sort_complex([5, 3, 6, 2, 1]))
print(np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j]))

# numpy.argmax() 和 numpy.argmin()
# numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。
a = np.array([1, 2, 3, 4])
# 3 表示的是排序数组索引为 3 的数字
print(np.partition(a, 3))
# 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间
print(np.partition(a, (1, 3)))
# 找到数组的第 3 小（index=2）的值和第 2 大（index=-2）的值
arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print(arr[np.argpartition(arr, 2)[2]])
print(arr[np.argpartition(arr, -2)[-2]])
# 用 [2,3] 同时将第 3 和第 4 小的排序好，然后可以分别通过下标 [2] 和 [3] 取得
print(arr[np.argpartition(arr, [2, 3])[2]])
print(arr[np.argpartition(arr, [2, 3])[3]])

a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(a)
print(np.argmax(a))
# 展开数组
print(a.flatten())
maxindex = np.argmax(a, axis=1)
print(maxindex)
minindex = np.argmin(a)
print(a.flatten()[minindex])
print(minindex)
minindex = np.argmin(a, axis=0)
print(minindex)
minindex = np.argmin(a, axis=1)
# numpy.nonzero()
# numpy.nonzero() 函数返回输入数组中非零元素的索引。
a = np.array([[40, 30, 0], [10, 20, 30]])
print(a)
print(np.nonzero(a))
# numpy.where()
# numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
x = np.arange(9.).reshape(3, 3)
print(x)
y = np.where(x > 3)
print(y)
print(x[y])
# numpy.extract()
# numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素。
condition = np.mod(x, 2) == 0
print(condition)
print(np.extract(condition, x))
