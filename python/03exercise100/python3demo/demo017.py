# Python 阶乘实例
num = int(input("num"))
fac = 1
if num < 0:
    print("error")
elif num == 0:
    print("0的阶乘是1")
else:
    for i in range(1, num + 1):
        fac = fac * i
    print(num, fac)
