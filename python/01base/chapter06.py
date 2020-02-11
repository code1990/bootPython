# 第六章 Python 循环语句

# while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
# for 循环	重复执行语句
# 嵌套循环	你可以在while循环体中嵌套for循环


# break 语句	在语句块执行过程中终止循环，并且跳出整个循环
# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
# pass 语句	pass是空语句，是为了保持程序结构的完整性。


# 八皇后问题
# 在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，
# 即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。
def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur + 1)


queen([None] * 8)


#找出序列数组的索引
def deduplication(self,nums):
    for i in range(len(nums)):
        if nums[i]==self:
            return i
    i=0
    for x in nums:
        if self>x:
            i+=1
    return i

print(deduplication(5,[1,3,5,6]))