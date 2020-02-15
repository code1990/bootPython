# Python 简单计算器实现
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num1 = int(input("num1"))
num2 = int(input("num2"))
choice = input("choice")

if choice == "1":
    print(add(num1, num2))
elif choice == "2":
    print(subtract(num1, num2))
elif choice == "3":
    print(multiply(num1, num2))
elif choice == "4":
    print(divide(num1, num2))
else:
    print("error")
