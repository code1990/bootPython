# NumPy 从已有的数组创建数组
# numpy.asarray
# numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个
import numpy as np

x = [1, 2, 3]
# 将列表转换为 ndarray:
a = np.asanyarray(x)
print(x)

x = (1, 2, 3)
# 将元组转换为 ndarray:
a = np.asanyarray(x)
print(x)

# 将元组列表转换为 ndarray:
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)

# 设置dtype参数
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

# numpy.frombuffer
# numpy.frombuffer 用于实现动态数组。
# numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。
s = b"Hello python"
a = np.frombuffer(s, dtype="S1")
print(a)

# numpy.fromiter
# numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
list = range(5)
it = iter(list)

# 使用迭代器创建ndarray
x = np.fromiter(it, dtype=float)
print(x)
