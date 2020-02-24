# 系列(Series)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组。轴标签统称为索引。
# 创建一个基本系列是一个空系列。
import pandas as pd
import numpy as np
s= pd.Series()
print(s)
# 从ndarray创建一个系列
# 如果数据是ndarray，则传递的索引必须具有相同的长度。 如果没有传递索引值，那么默认的索引将是范围(n)，其中n是数组长度，即[0,1,2,3…. range(len(array))-1] - 1]。
data=np.array(["a","b","c","d"])
s=pd.Series(data)
print(s)
# 在这里传递了索引值
s = pd.Series(data,index=[100,101,102,103])
print(s)
# 从字典创建一个系列
# 字典(dict)可以作为输入传递，如果没有指定索引，则按排序顺序取得字典键以构造索引。 如果传递了索引，索引中与标签对应的数据中的值将被拉出。
data={"a":0,"b":2,"c":3}
s=pd.Series(data)
print(s)
# 索引顺序保持不变，缺少的元素使用NaN(不是数字)填充。
s = pd.Series(data,index=['b','c','d','a'])
print(s)
# 从标量创建一个系列
# 如果数据是标量值，则必须提供索引。将重复该值以匹配索引的长度。
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
#