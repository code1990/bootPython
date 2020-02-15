# 题目：反向输出一个链表。
if __name__ == "__main__":
    ptr = []
    for i in range(5):
        num = int(input(""))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)
