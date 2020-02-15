# Python 最大公约数算法
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


num1 = int(input("num1"))
num2 = int(input("num2"))

print(hcf(num1, num2))
