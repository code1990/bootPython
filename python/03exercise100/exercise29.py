# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
import math
x = int(input("请输入一个数\n"))
a = math.trunc(x / 10000)
b = x % 10000 // 1000
c = x % 1000 // 100
d = x % 100 //10
e = x % 10

if a != 0:
    print("5位数", e, d, c, b, a)
elif b != 0:
    print("4位数", e, d, c, b)
elif c != 0:
    print("3位数", e, d, c)
elif d != 0:
    print("2位数", e, d)
else:
    print("1位数", e)
