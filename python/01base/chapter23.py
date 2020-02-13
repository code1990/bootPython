# Python 异常处理
# 异常处理:
# 断言(Assertions):

# 什么是异常？
# 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。

# 以下为简单的try....except...else的语法：
import sys

try:
    "写模式下 如果文件不存在 则会创建文件"
    fh = open("C:\\Users\\Administrator\\Desktop\\11111.txt", "w+")
    fh.write("hello python 123")
except IOError:
    print("文件找不到")
else:
    print("写入文件ok")
    fh.close()

# 使用except而不带任何异常类型
'''
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
'''

# 使用except而带多种异常类型

'''
try:
    正常的操作
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
'''

# try-finally 语句
# try-finally 语句无论是否发生异常都将执行最后的代码。

try:
    fh1 = open("C:\\Users\\Administrator\\Desktop\\11111.txt", "w")
    fh1.write("111")
finally:
    print("没有找到文件或者没有权限")
    fh1.close()

# 上面的案例改写
try:
    fh1 = open("C:\\Users\\Administrator\\Desktop\\11111.txt", "w")
    try:
        fh1.write("这是一个测试文件")
    finally:
        print("关闭文件")
        fh1.close()
except:
    print("没有找到文件或者文件夹不存在")

# 异常的参数
# 一个异常可以带上参数，可作为输出的异常信息参数。python3不支持

# 触发异常
# raise语句自己触发异常
'''
try:
    正常逻辑
except Exception,err:
    触发自定义异常    
else:
    其余代码
'''

x=10
if x>5:
    print("111")
    # raise Exception("x 不能大于5，x 的参数值为{}".format(x))

# 用户自定义异常
# 你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:

class MyError(Exception):
    # 类 Exception 默认的 __init__() 被覆盖。
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print("My Exception is ",e.value)


# 当创建一个模块有可能抛出多种不同的异常时，
# 一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,expression,message):
        self.expression=expression
        self.message=message

class TransitionError(Error):
    def __init__(self,previous,next,message):
        self.previous = previous
        self.next = next
        self.message = message

# 定义清理行为
# 不管 try 子句里面有没有发生异常，finally 子句都会执行。
def divide(x,y):
    try:
        result =x/y
    except ZeroDivisionError:
        print("zero error")
    else:
        print("result is",result)
    finally:
        print("executed finally clause")

divide(2, 0)

# 预定义的清理行为
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("C:\\Users\\Administrator\\Desktop\\11111.txt") as f:
    for line in f:
        print(line, end="")


# Python3 assert（断言）
# Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
assert True     # 条件为 true 正常执行
assert False    # 条件为 false 触发异常