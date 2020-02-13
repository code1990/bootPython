# Python 文件I/O
# 本章只讲述所有基本的 I/O 函数，更多函数请参考Python标准文档。

# 打印到屏幕
# 最简单的输出方法是用print语句
#  print函数是对sys.stdout的高级封装
# sys.stdout.write()
# sys.stdout.flush()
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
print("hello python")
import sys
sys.stdout.write("111")
sys.stdout.flush()

#
print("format")
print("{},{}".format("hello","python"))
print(str("1111"))
print(repr("1111"))

# 读取键盘输入 input
print("用户输入")
# varInput = input("请输入\n")
# print(varInput)


# 打开和关闭文件
# 用 file 对象做大部分的文件操作。
# open 函数
# 你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 首先 桌面创建一个文件夹
"打开一个文件"
# 只要使用了open函数，就一定记得close掉
fileInfo = open("C:\\Users\\Administrator\\Desktop\\123456.txt","w")
print("文件名",fileInfo.name)
print("文件是否已关闭",fileInfo.closed)
print("访问模式",fileInfo.mode)

# File对象的属性
# 一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。
# 以下是和file对象相关的所有属性的列表：

# close()方法
# File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
"关闭一个文件"
# fileInfo.close()

# write()方法
# write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
fileInfo.write("hello python,hello java")
# 关闭打开的文件
fileInfo.close()

# read()方法
# read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# f.readline() 会从文件中读取单独的一行。
# f.readlines() 将返回该文件中包含的所有行。
file1 = open("C:\\Users\\Administrator\\Desktop\\123456.txt","r+")
# 10 表示长度
fileContent = file1.read(10)
print(fileContent)


# 文件定位
# tell()方法告诉你文件内的当前位置,
# seek（）方法改变当前文件的位置。
# 查找当前文件的位置
position = file1.tell()
print(position)
# 移动指针到文件开头
position= file1.seek(0,0)
print(file1.read(10))
file1.close()
# 重命名和删除文件
# rename()方法需要两个参数，当前的文件名和新文件名。
# 你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
import os
# rename 可以修改文件夹 文件 名称
# 只要使用了open函数，就一定记得close掉
# os.rename("C:\\Users\\Administrator\\Desktop\\123456.txt","C:\\Users\\Administrator\\Desktop\\1234567.txt")
os.remove("C:\\Users\\Administrator\\Desktop\\123456.txt")
# Python里的目录：
# os模块的mkdir()方法在当前目录下创建新的目录们
# 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
# getcwd()方法显示当前的工作目录。
# rmdir()方法删除目录，目录名称以参数传递。
print("==============")
# os.mkdir("C:\\Users\\Administrator\\Desktop\\test\\")
# os.rmdir("C:\\Users\\Administrator\\Desktop\\test\\")
print("==============")
print(os.getcwd())
# 将当前目录改为"D:\\github\\bootPython\\python\\01base\\"
os.chdir("D:\\github\\bootPython\\python\\01base\\")

# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# 把内存的对象写入到文件

import pickle
data1={"1":"a","2":"b"}
list1=[1,2,3]
output = open("C:\\Users\\Administrator\\Desktop\\111.txt","wb")

pickle.dump(data1,output)

pickle.dump(list1,output)

output.close()

import pprint
# 从序列化的文件读取
input1 = open("C:\\Users\\Administrator\\Desktop\\111.txt","rb")

data2=pickle.load(input1)
pprint.pprint(data1)

data3=pickle.load(input1)
pprint.pprint(data3)

input1.close()

