# Python 质数判断
num = int(input("num"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("no")
            break
    else:
        print("是质数")
else:
    print("不是质数")
