# 循环创建文件
import os
# path = "D:\\\\github\\\\bootPython\\\\python\\\\02high\\\\"
path = "C:\\Users\\Administrator\\Desktop\\test\\"
for i in range(1,30):
    string=str(i)
    if i<=9:
        string="0"+str(i)
    name = path+"Vuejs"+string+".html"
    print(name)
    # print(string)
    # open方法可以创建一个文件
    file = open(name,"w")
