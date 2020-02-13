# Python3 命名空间和作用域
# 命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
#  Python 的查找顺序为：局部的命名空间去 -> 全局命名空间 -> 内置命名空间。
# var1是全局名称
var1 = 5
def some_func():
    # var2是局部名称
    var2 =6
    def some_inner_func():
        # var3是内部嵌套的局部名称
        var3=7

# 作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
# 规则顺序： L –> E –> G –>gt; B。
g_count=0 # 全局作用域
def counter():
    o_count=1 #闭包函数外的函数中
    def inner():
        i_count=2 #局部作用域

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
total =0#全局变量
def sum(a1,a2):
    # 返回2个参数的和
    total = a1+a2
    print("函数内是局部变量",total)
    return total
# 调用函数
sum(10,10)
print("函数外事全局变量",total)

# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
num=1
def fun1():
    global num #使用global关键字声明
    print(num)
    num=123
    print(num)

fun1()
print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：

def outer():
    num =10
    def inner():
        nonlocal num #关键字声明
        num=100
        print(num)
    inner()
    print(num)
outer()

a=10
def test(a):
    a=a+1
    print(a)
test(a)
