# NumPy 数学函数
# NumPy 包含大量的各种数学运算的函数，包括三角函数，算术运算的函数，复数处理函数等。
import numpy as np

# 三角函数
# NumPy 提供了标准的三角函数：sin()、cos()、tan()。
a = np.array([0, 30, 90])
print(np.sin(a * np.pi / 180))
print(np.cos(a * np.pi / 180))
print(np.tan(a * np.pi / 180))
# arcsin，arccos，和 arctan 函数返回给定角度的 sin，cos 和 tan 的反三角函数。
# 这些函数的结果可以通过 numpy.degrees() 函数将弧度转换为角度
sin = np.sin(a * np.pi / 180)
print(sin)
inv = np.arcsin(sin)
print(inv)
print(np.degrees(inv))
cos = np.cos(a * np.pi / 180)
print(cos)
inv = np.arccos(cos)
print(inv)
print(np.degrees(inv))
tan = np.tan(a * np.pi / 180)
print(tan)
inv = np.arctan(tan)
print(inv)
print(np.degrees(inv))

# 舍入函数
# numpy.around() 函数返回指定数字的四舍五入值。
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))

# numpy.floor()
# numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整。
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(np.floor(a))

# numpy.ceil()
# numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整。
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(np.ceil(a))
