# Python Number(数字)
# Python Number 数据类型用于存储数值。
var1 = 1
var2 = 10
var3 = 3
del var1
del var2, var3

# Python Number 类型转换
# 简而言之 就是类型(x)

# Python math 模块、cmath 模块
# Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
#
# Python math 模块提供了许多对浮点数的数学运算函数。
#
# Python cmath 模块包含了一些用于复数运算的函数。
import math

print(dir(math))
import cmath

print(dir(cmath))

# 具体的复数运算实例
print(cmath.sqrt(-1))
print(cmath.sqrt(9))
print(cmath.sin(1))
print(cmath.log10(100))

# Python数学函数
print(abs(-1))
# 向上取整
print(math.ceil(4.1))
# e的x次幂
print(math.exp(1))
# 绝对值
print(math.fabs(-1))
# 向下取整数
print(math.floor(2.1))
# 取对数
print(math.log(100, 10))
# 取10的对数
print(math.log10(100))
# 获取给定参数序列的最大值
print(max(12, 11))
# 给定参数学列的最小值
print(min(12, 11))
# 返回整数部分与小数部分的序列
print(math.modf(12.12))
# x**y 2的2次方
print(math.pow(2, 2))
# 四舍五入
print(round(1.22, 0))
# 开方
print(math.sqrt(2))

# Python随机数函数
import random

# 从序列中随机获取一个数字
print(random.choice(range(10)))
# 从集合中随机获取一个数字
print(random.randrange(0, 200, 1))
# 获取一个0-1之间的浮点数
print(random.random())
# seed 改变生成随机数的seed 不建议改变
# shuffle 随机洗牌
shuffleList = [10, 11, 12, 13]
random.shuffle(shuffleList)
print(shuffleList)
# uniform() 生成指定范围的随机数
print(random.uniform(1, 2))
# Python三角函数
print(math.acos(1))  # 反余弦弧度值
print(math.sin(1))  # 反正玄弧度值
print(math.atan(1))  # 反正切弧度
print(math.atan2(1, 2))  # 给定x,y坐标查询反正切
print(math.cos(1))  # 余弦值
print(math.hypot(1, 2))  # 返回欧几里德范数 sqrt(x*x + y*y)。
print(math.sin(90))  # 正弦
print(math.tan(1))  # 正切
print(math.degrees(math.pi))  # 弧度转角度
print(math.radians(90))  # 角度转弧度
# Python数学常量
print(math.pi)
print(math.e)
