# 第五章 Python 条件语句
a = 1
while a < 7:
    if (a % 2 == 0):
        print(a, "is even")
    else:
        print(a, "is odd")
    a += 1

flag = False
name = "luren"
if name == "python":
    flag = True
    print("welcome boss")
else:
    print(name)

number = 5
if number == 3:
    print("boss")
elif number == 2:
    print("user")
elif number == 1:
    print("worker")
elif number < 0:
    print("error")
else:
    print("roadman")

if number > 0 and number <= 10:
    print("hello")
else:
    print("python")

if number < 0 or number > 10:
    print("hello")
else:
    print("python")

if (number >= 0 and number <= 5) or (number >= 10 and number <= 15):
    print("hello")
else:
    print("python")

var = 100
if (var == 100): print("var==100")
print("goodbye")
