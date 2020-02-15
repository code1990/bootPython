# 题目：列表排序及连接。
# 程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [2, 3, 4]
    a.sort()
    print(a)

    print(a + b)
    a.extend(b)
    print(a)
