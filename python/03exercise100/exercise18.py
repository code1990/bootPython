# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
tn = 0
sn = []
n = int(input("n=\n"))
a = int(input("a=\n"))
for count in range(n):
    tn = tn + a
    a = a * 10
    sn.append(tn)
    print(tn)
