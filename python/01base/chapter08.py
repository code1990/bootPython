# Python for 循环语句

for letter in "python":
    print("当前字母是", letter)

fruits = ["banana", "apple", "orange"]
for fruit in fruits:
    print("当前的水果是", fruit)

print("goodbye")

for index in range(len(fruits)):
    print("当前的水果是", fruits[index])

print("goodbye")

# 循环使用 else 语句
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d == %d * %d" % (num, i, j))
            break
    else:
        print(num, "是一个质数")
