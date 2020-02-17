# NumPy 算术函数
# NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
import numpy as np

a = np.arange(9, dtype=np.float_).reshape(3, 3)
print(a)
b = np.array([10, 10, 10])
print(b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

# numpy.reciprocal()
# numpy.reciprocal() 函数返回参数逐元素的倒数。如 1/4 倒数为 4/1。
a=np.array([0.25,1.33,1,100])
print(a)
print(np.reciprocal(a))

# numpy.power()
# numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
a=np.array([10,100,1000])
print(np.power(a,2))
b=np.array([1,2,3])
print(b)
print(np.power(a,b))

# numpy.mod()
# numpy.mod() 计算输入数组中相应元素的相除后的余数。
# 函数 numpy.remainder() 也产生相同的结果。
a=np.array([10,20,30])
b=np.array([3,5,7])
print(np.mod(a,b))
print(np.remainder(a,b))




