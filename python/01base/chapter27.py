# Python3 标准库概览
# os模块提供了不少与操作系统相关联的函数。
import os

print(os.getcwd())
# print(os.system("dir"))
# 在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
print(dir(os))
# print(help(os))

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil
# shutil.copyfile("1.txt","2.txt")
# shutil.move("1.txt","/")

# 文件通配符
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob

print(glob.glob("*.py"))

# 命令行参数
# 通用工具脚本经常调用命令行参数。
import sys

print(sys.argv)

# 错误输出重定向和程序终止
# sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。
sys.stdout.write("123\n")

# 字符串正则匹配
# re模块为高级字符串处理提供了正则表达式工具
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# 数学
# math模块为浮点运算提供了对底层C函数库的访问:
import math

print(math.cos(math.pi))
print(math.log(1024, 2))
# random提供了生成随机数的工具。
import random

print(random.choice(["apple", "123"]))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

# 访问 互联网
# 其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:

from urllib.request import urlopen

# for line in urlopen("https://www.baidu.com//"):
#     if "baidu" in line:
#         print(line)

import smtplib
# server=smtplib.SMTP("localhost")
# server.send("123")
# server.quit()

# 日期和时间
# datetime模块为日期和时间处理同时提供了简单和复杂的方法。
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(2000,1,1)
age= now-birthday
print(age.days)

# 数据压缩
# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib
s=b'hello python'
print(len(s))
t=zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

# 性能度量
# 不同方法之间的性能差异,timeit 证明了现代的方法更快一些。
# 相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 测试模块
# doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
def average(values):
    return sum(values)/len(values)

# if __name__=='_main_':
#     import doctest
#     doctest.testmod()
# import doctest
# doctest.testmod()   # 自动验证嵌入测试

# unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
# 注意文件夹不要重名 unittest 或者unittest.py
import unittest
class TestFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)
unittest.main() # Calling from the command line invokes all tests
