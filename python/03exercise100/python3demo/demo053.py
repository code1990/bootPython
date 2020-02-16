# Python 判断字符串长度
print(len("hello python"))


def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


print(findLen("hello python"))


def length(src):
    count = 0
    all_str = src[count:]
    for x in all_str:
        count += 1
    print(count)


length("hello python")
