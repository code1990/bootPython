# Python 函数
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

# 定义一个函数

# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 圆括号之间可以用于定义参数。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

# 实例
# 函数定义
def printme(str):
    "打印传入的字符串到显示设备上"
    print(str)
    return


# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

# 参数传递
# 在 python 中，类型属于对象，变量是没有类型的：
# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

# python 传不可变对象实例
def changeInt(a):
    a=10

b=2
changeInt(b)
print(b)

# 传可变对象实例
def changename(mylist):
    # 修改传入的列表
    mylist.append([1,2,3,5])
    print("函数取值",mylist)
    return

mylist=[10,20,30]
changename(mylist)
print(mylist)

"""
参数
以下是调用函数时可使用的正式参数类型：

必备参数
关键字参数
默认参数
不定长参数

"""
#必备参数
# 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

printme("hello")

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
printme( str = "My string")

# 下例能将关键字参数顺序不重要展示得更清楚：
def printinfo(name,age):
    "打印任何传入的字符串"
    print("name",name)
    print("age",age)
    return

printinfo(age=50,name="jim")

# 默认参数
# 调用函数时，默认参数的值如果没有传入，则被认为是默认值。
def printinfo2(name,age=30):
    "打印任何传入的字符串"
    print("name",name)
    print("age",age)
    return

printinfo2(age=50,name="mike")
printinfo2(name="milk")

# 不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。不定长参数实例如下：
def printInfo123(arg1,*v):
    "打印任何输入的字符串"
    print(arg1)
    for var in v:
        print(var)
    return


printInfo123(10)
printInfo123(10,100,1000)

#匿名函数
# python 使用 lambda 来创建匿名函数。

# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。
sum = lambda a1,a2:a1+a2
# 调用sum函数
print(sum(100,100))
print(sum(200,100))

# return 语句
# return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
def sum2(a1,a2):
    "返回2个参数的和"
    total = a1+a2
    print("函数内:",total)
    return total

print(sum2(12,100))

# 变量作用域
# 两种最基本的变量作用域如下：
# 全局变量
# 局部变量

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

total =0# 这是一个全局作用域
def sum3(a1,a2):
    total = a1+a2 #total是局部作用域
    print(total)
    return total

sum3(20,20)
print(total)
