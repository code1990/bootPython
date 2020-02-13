# Python 第一章 基础语法

# 编码
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串

# python保留字
import keyword
# 打印所有的保留字
print(dir(keyword))

# 第一个 Python 程序
# 打印输出并换行 hello world
print("Hello World")
# 打印不换行
print('hello', end='')

# 单行注释
# 多行注释 """""" 或者''''''
'''
这是多行注释，可以使用单引号 可以使用多引号。

标识符由字母、数字、下划线组成。
所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
标识符是区分大小写的。
以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。

'''

# python 最具特色的就是用缩进来写模块。 而不是使用{}
if True:
    print("this is true")
else:
    print("this is false")

# raw_input py2环境下
# 接受用户输入 Python3环境下
# a=input("按下enter键退出，其他键显示.....\n")
# print(a)

# 同一行显示多条语句 需要使用;分割
import sys;

x = 'jim';
print(x)

# 打印不换行
print('hello', end='')

# 多个语句构成代码组
aa = 10
if aa % 2 == 0:
    print(aa, "是偶数")
elif 10 % 2 != 0:
    print(aa, "是奇数")
else:
    print(aa, "other")
