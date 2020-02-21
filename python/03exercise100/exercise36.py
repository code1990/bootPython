# 题目：求100之内的素数。
lower = input("low")
upper = input("high")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
