# NumPy 高级索引
# NumPy 比一般的 Python 序列提供更多的索引方式。除了之前看到的用整数和切片的索引外，数组可以由整数数组索引、布尔索引及花式索引。
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
# 以下实例获取数组中(0,0)，(1,1)和(2,0)位置处的元素。
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

# 以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)

# 可以借助切片 : 或 … 与索引数组组合。如下面例子：
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
d = a[..., 1:]
print(b)
print(a)
print(c)

# 布尔索引
# 我们可以通过一个布尔数组来索引目标数组。
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print("数组是")
print(x)
print("\n")
# 大于5的元素
print("大于5的元素")
print(x[x > 5])
# 以下实例使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])
# 以下实例演示如何从数组中过滤掉非复数元素。
a = np.array([1, 2 + 6j, 5, 5.0 + 5j])
print(a[np.iscomplex(a)])

# 花式索引
# 花式索引指的是利用整数数组进行索引。
# 花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。
# 1、传入顺序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[4, 2, 1, 7]])
# 2、传入倒序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[-4, -2, -1, -7]])
# 3、传入多个索引数组（要使用np.ix_）
x = np.arange(32).reshape(8, 4)
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
