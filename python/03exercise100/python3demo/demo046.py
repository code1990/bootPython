# Python 计算元素在列表中出现的次数
def countX(list, x):
    count = 0
    for ele in list:
        if (ele == x):
            count = count + 1
    return count


list = [1, 2, 3, 4]
x = 2
print(countX(list, x))
