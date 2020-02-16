# NumPy Ndarray 对象
# NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
#
# ndarray 对象是用于存放同类型元素的多维数组。
#
# ndarray 中的每个元素在内存中都有相同存储大小的区域。
#
# ndarray 内部由以下内容组成：

import numpy as np
a=np.array([1,2,3])
print(a)
a=np.array([[1,2],[3,4]])
print(a)
a=np.array([2,3,4,4,5],ndmin=2)
print(a)
a=np.array([1,2,3],dtype=complex)
print(a)

# ndarray 对象由计算机内存的连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置。
# 内存块以行顺序(C样式)或列顺序(FORTRAN或MatLab风格，即前述的F样式)来保存元素。


