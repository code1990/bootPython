# 题目：将一个数组逆序输出。
if __name__ == "__main__":
    a = [1, 2, 3, 4]
    N = len(a)
    print(a)
    for i in range(len(a) // 2):
        a[i], a[N - i - 1] = a[N - i - 1], a[i]
        print(a)
