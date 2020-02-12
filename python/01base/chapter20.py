# Python 模块
# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

# import 语句
# 模块的引入
# 模块定义好后，我们可以使用 import 语句来引入模块，语法如下：

# 引入指定的模块
import sys

# from…import 语句
# 导入一个指定的部分到当前命名空间中
from sys import stdout
# from…import* 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的
from sys import *

# 搜索路径

# PYTHONPATH 变量
# 作为环境变量，PYTHONPATH 由装在一个列表里的许多目录组成。

# 命名空间和作用域
# 变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。

money=200
def addMoney():
    "global VarName 的表达式会告诉 Python， VarName 是一个全局变量"
    global  money
    money = money+1

print(money)
print(addMoney())
print(money)

# dir()函数
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

print(dir(sys))

# globals() 和 locals() 函数
# 根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
#
# 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
#
# 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

# reload() 函数
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
#
# 因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数


# Python中的包
# 包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。
# __init__.py 用于标识当前文件夹是一个包。
