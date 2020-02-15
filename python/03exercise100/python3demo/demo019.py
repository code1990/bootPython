# Python 斐波那契数列
num = int(input("num"))
n1 = 0
n2 = 1
count = 2

if num <= 0:
    print("error")
elif num == 1:
    print(n1)
else:
    print(n1, ",", n2, end=" , ")
    while count < num:
        nth = n1 + n2
        print(nth, end=",")
        n1 = n2
        n2 = nth
        count += 1
