# 循环创建文件
import os
# path = "D:\\\\github\\\\bootPython\\\\python\\\\02high\\\\"
path = "C:\\Users\\Administrator\\Desktop\\test\\"
for i in range(10,100):
    name = path+"exercise"+str(i)+".py"
    print(name)
    # open方法可以创建一个文件
    file = open(name,"w")
