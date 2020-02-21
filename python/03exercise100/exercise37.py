# 题目：对10个数进行排序。
if __name__ == '__main__':
    N = 10
    print("number 10")
    l = []
    for i in range(N):
        l.append(int(input("input number")))
    print()
    for i in range(N):
        print(l[i])
    print()

    for i in range(N - 1):
        min = 1
        for j in range(j + 1, N):
            if l[min] > l[j]: min = j
        l[i], l[min] = l[min], l[i]
    print("after")
    for i in range(N):
        print(l[i])
