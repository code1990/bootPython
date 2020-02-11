# Python pass 语句
# Python pass 是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句。
for letter in "python":
    if letter == 'h':
        pass
        print("这是pass代码块")
    print("当前的字母是", letter)
print("goodbye")

# pass 便是占据一个位置，因为如果定义一个空函数程序会报错
def nullFunction(n):
    pass