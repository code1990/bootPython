# 第二章 变量类型

# Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# 声明不同的类型 并赋值
counter = 10
miles = 1000.0
name = "John"

print(counter)
print(miles)
print(name)

# 同时给多个变量赋值
a = b = c = 1
aa, bb, cc = 1, 2.0, "John"

# 数字数据类型用于存储数值。
var1 = 10
# del删除一个对象的引用
del var1
# python 支持int long float complex 四种数字形式
# NameError: name 'var1' is not defined
# print(var1)

# 字符串 支持单引号 双引号
str1 = "Hello"
string = 'world'
# 从左到右索引默认0开始的下标是从 0 开始算起
# 右到左索引默认-1开始的
print(str1[0])
print(str1[-1])
print(str1[1:2])
print(str1[2:])
# 打印2次
print(str1 * 2)
print(str1 + " python")

# List（列表） 是 Python 中使用最频繁的数据类型。
list1 = ["Hello", 123, 123.0, "World"]
smallList = ["Hello", "Spark"]
print(list1)
print(list1[0])
print(list1[1:2])
print(list1[2:])
print(list1 * 2)
print(list1 + smallList)

# 元祖 元祖类似于只读列表 不可以二次赋值
tuple1 = ("Hello", 123, 123.0, "World")
smallTuple = ("Hello", "Spark")
print(tuple1)
print(tuple1[0])
print(tuple1[1:2])
print(tuple1[2:])
print(tuple1 * 2)
print(tuple1 + smallTuple)

# 尝试赋值 来改变元祖和列表
list1[1] = 1000
# 元祖不可以二次赋值
# tuple[1]=1000

print(list1)
print(tuple1)

# Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#
# 基本功能是进行成员关系测试和删除重复元素。

student = {"1", "2", "3", "3"}
# 重复的元素被自动去掉
print(student)
# 成员测试
if "1" in student:
    print("in")
else:
    print("not in")

#     set集合可以执行集合运算
a = set("abca")
b = set("defa")
print(a)
print(b)
print(a - b)  # 差集
print(a | b)  # 并集
print(a & b)  # 交集
print(a ^ b)  # 同时不存在的元素

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型
dict1 = {}
dict1["one"] = "Hello"
dict1["two"] = "python"
dict1[3] = "ok"
print(dict1)
print(dict1['one'])
print(dict1[3])
print(dict1.keys())
print(dict1.values())

# 类型的相互转换
print(int(10))
print(float(10))
print(complex(10.0))
# 把对象转换为字符串
a1 = 26
print('我有' + str(a1) + '个苹果')
# 对象转换为表达式字符串
print(repr("sss"))
# 用来计算在字符串中的有效Python表达式,并返回一个对象
num1 = eval("123.1")
print(type(num1))
# 把序列s转换为元祖tuple
spam = (1, 2, 3, 4)
spam = list(spam)
print(spam)
# 把序列转换为元祖
spam = tuple(spam)
print(spam)
# set转换为可变集合
s1 = frozenset()  # 创建一个不可变的空集合。
l = [1.23, "a"]  # 列表类型
d = {1: "a", 2: "b"}  # 字典类型
a = (1, 2, "b")  # 元组类型
s = "厉害了，我的国"  # 字符串
c = set("1,2,3a")  # 可变集合

# 创建一个字典
ddd = dict(d)
print(ddd)

# frozenset(s) 转换为不可变集合
s3 = frozenset(l)
print(s3)

# chr把一个整数类型转换为字符
print(chr(99))
# ord 把一个字符转换为整数值
print(ord('c'))
# hex 整数转换为16进制
print(hex(1))
# oct 整数转换为8进制
print(oct(1))
