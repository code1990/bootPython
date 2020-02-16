# NumPy 切片和索引
# ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。
import numpy as np

a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])

# 我们也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作：
a = np.arange(10)
b = a[2:7:2]
print(b)

a = np.arange(10)
b = a[5]
print(b)
print(a[2:])
print(a[2:5])

# 多维数组同样适用上述索引提取方法：
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[1:])

# 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。
# 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。
print("numpy009")
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素
