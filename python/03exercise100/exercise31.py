# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
letter = input("please input")
if letter == "S":
    print("input")
    letter = input("input")
    if letter == "a":
        print("s")
    elif letter == "u":
        print("u")
    else:
        print("error")
elif letter == "f":
    print("f")
elif letter == "M":
    print("M")
elif letter == "T":
    print("input")
    letter = input("")

    if letter == "u":
        print("u")
    elif letter == "h":
        print("h")
    else:
        print("data error")
elif letter == "w":
    print("w")
else:
    print("data error")
