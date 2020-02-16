# NumPy 位运算
# NumPy "bitwise_" 开头的函数是位运算函数。
#
# NumPy 位运算包括以下几个函数：
#
# 函数	描述
# bitwise_and	对数组元素执行位与操作
# bitwise_or	对数组元素执行位或操作
# invert	按位取反
# left_shift	向左移动二进制表示的位
# right_shift	向右移动二进制表示的位
import numpy as np

# bitwise_and
# bitwise_and() 函数对数组中整数的二进制形式执行位与运算。
print("二进制")
a, b = 13, 17
print(bin(a), bin(b))
print(np.bitwise_and(13, 17))

# bitwise_or
# bitwise_or()函数对数组中整数的二进制形式执行位或运算。
print(np.bitwise_or(13, 17))

# invert
# invert() 函数对数组中整数进行位取反运算，即 0 变成 1，1 变成 0。
#
# 对于有符号整数，取该二进制数的补码，然后 +1。二进制数，最高位为0表示正数，最高位为 1 表示负数。
print(np.invert(np.array([13], dtype=np.unit8)))
print(np.binary_repr(13, width=8))
print(np.binary_repr(242, width=8))

# left_shift
# left_shift() 函数将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的 0。
print(np.left_shift(10, 2))
print(np.binary_repr(10, width=8))
print(np.binary_repr(40, width=8))

# right_shift
# right_shift() 函数将数组元素的二进制形式向右移动到指定位置，左侧附加相等数量的 0。
print(np.right_shift(40,2))
print(np.binary_repr(40,width=8))
print(np.binary_repr(40,width=8))
