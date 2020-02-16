# Python 计算列表元素之积
def multiplylist(mylist):
    result = 1
    for x in mylist:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(multiplylist(list1))
print(multiplylist(list2))

from functools import reduce

sum = reduce(lambda x, y: x * y, list1)
print(sum)
