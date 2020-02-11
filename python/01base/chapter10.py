# Python break 语句
# break语句用来终止循环语句

for letter in "python":
    if letter == "h":
        break
    print("当前的字母是", letter)

var = 10
while var > 0:
    print("当前的变量是", var)
    var = var - 1
    if var == 5:
        break

print("goodbye")