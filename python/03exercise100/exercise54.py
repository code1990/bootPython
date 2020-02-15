# 取一个整数a从右端开始的4〜7位。
if __name__ == "__main__":
    a = int(input("num"))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print(a, b)
