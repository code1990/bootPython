# Python 输出指定范围内的素数
lower = int(input("small"))
upper = int(input("big"))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
