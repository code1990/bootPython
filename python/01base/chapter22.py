# Python File(文件) 方法
# 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
import sys

# 打开一个文件
file = open("C:\\Users\\Administrator\\Desktop\\111.txt","w+")
# 写入文件内容
file.write("hello python 123")
# 写入一个序列
file.writelines(["1", "2", "3"])
# 刷新
file.flush()
# 返回文件当前位置
print(file.tell())
# 设置文件当前位置
file.seek(0, 0)
# 返回一个整型的文件描述符
print(file.fileno())
# 文件连接到一个终端设备返回 True
print(file.isatty())
# 返回文件下一行
# file.next()
# 从文件读取指定的字节数
file1 = open("C:\\Users\\Administrator\\Desktop\\111.txt","r+")
print(file1.read(1))
# 读取整行
print(file1.readline())
# 读取所有行并返回列表
print(file1.readlines())
#截取文件
print(file1.truncate(10))
file.close()
file1.close()
