# Python continue 语句
# Python continue 语句跳出本次循环，而break跳出整个循环。

for letter in "python":
    if letter == "h":
        continue
    print("当前的字母是", letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print("当前的变量是", var)

print("goodbye")

var = 10
while var > 0:
    var = var - 1
    if var == 5 or var == 8:
        continue
    print("当前的变量是", var)
print("goodbye")

n = 10
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
print("goodbye")
