# NumPy 字节交换
# 在几乎所有的机器上，多字节对象都被存储为连续的字节序列。字节顺序，是跨越多字节的程序对象的存储规则。
import numpy as np
a= np.array([1,256,8755],dtype=np.int16)
print(a)
print (map(hex,a))
# byteswap() 函数通过传入 true 来原地交换
print(a.byteswap(True))
print (map(hex,a))