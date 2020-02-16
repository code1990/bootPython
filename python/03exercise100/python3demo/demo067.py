# Python 线性查找
def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


def lineSearch(list):
    num = int(input("num"))
    counter = 0
    null = 0

    for i in list:
        if i == num:
            print(num, counter)
        else:
            null += 1
        counter += 1

    if null == counter:
        print("do not find it")


def linearSearch(num=50):
    import random
    random.seed(888)
    data = []
    for i in range(15):
        data.append(random.randint(1, 100))
    data.sort()
    print(data)
    for i in range(0, len(data)):
        if data[i] == num:
            print(i)
            break
        else:
            print("no")
