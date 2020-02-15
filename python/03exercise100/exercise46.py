# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
TRUE=1
FALSE=0
def SQ(x):
    return x*x
print("数字小于50则程序结束")
again=1
while again:
    num=int(input("输入数字\n"))
    print("结果",SQ(num))
    if SQ(num)>=50:
        again=TRUE
    else:
        again=FALSE
print(again)
