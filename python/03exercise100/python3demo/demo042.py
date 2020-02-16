# Python 翻转列表
def Reverse1(list):
    return [ele for ele in reversed(list)]


def Reverse2(list):
    list.reverse()
    return list


def Reverse3(list):
    new_list = list[::-1]
    return new_list


list = [10, 11, 12, 13, 14, 15]
print(Reverse1(list))
print(Reverse2(list))
print(Reverse3(list))
