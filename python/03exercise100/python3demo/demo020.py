# Python 阿姆斯特朗数
num = int(input("num"))
sum = 0
n = len(str(num))

temp = sum
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print(num)
else:
    print(num)
