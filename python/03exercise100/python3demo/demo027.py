# Python 使用递归斐波那契数列
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


num = int(input("num"))
if num < 0:
    print("error")
else:
    print("")
    for i in range(num):
        print(recur_fibo(i))
