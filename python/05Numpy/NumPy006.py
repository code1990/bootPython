# NumPy 创建数组
# ndarray 数组除了可以使用底层 ndarray 构造器来创建外，也可以通过以下几种方式来创建。
#
# numpy.empty
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：

import numpy as np
x=np.empty([3,2],dtype=np.int)
print(x)

# numpy.zeros
# 创建指定大小的数组，数组元素以 0 来填充：
x=np.zeros(5)
print(x)

y=np.zeros((5,),dtype=np.int)
print(y)

z=np.zeros((2,2),dtype=np.int)
print(z)

# numpy.ones
# 创建指定形状的数组，数组元素以 1 来填充

x=np.ones([2,2],dtype=np.int)
print(x)