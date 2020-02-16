# Python 计算列表元素之和
total = 0
list1 = [11, 13, 15]
for ele in range(0, len(list1)):
    total = total + list1[ele]

print("total", total)
total = 0
while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print(total)


def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


from functools import reduce

sum = reduce(lambda x, y: x + y, list1)
print(sum)

print(sum(list1))
