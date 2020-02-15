# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def reduceNum(n):
    print(n, end='')
    if not isinstance(n, int) or n <= 0:
        print("请输入一个正确的数字")
    elif n in [1]:
        print(n)
    while n not in [1]:
        # 因为 python3 中取消了 range 函数，而把 xrange 函数重命名为 range，所以现在直接用 range 函数即可。
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index
                if n == 1:
                    print(index, end='')
                else:
                    print(index, end='')
                break


reduceNum(90)
print()
reduceNum(100)
