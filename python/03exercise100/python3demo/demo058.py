# Python 按键(key)或值(value)对字典进行排序
def dictionairy():
    key_value = {}
    key_value[1] = 22
    key_value[2] = 2
    key_value[3] = 11
    key_value[4] = 11
    key_value[5] = 22

    for i in sorted(key_value):
        print(i, key_value[i], end=" ")

#     采取lambada的方式去实现
#     print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))


if __name__ == '__main__':
    dictionairy()

