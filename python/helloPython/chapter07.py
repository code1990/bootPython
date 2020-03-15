# 第7章　用户输入和while循环　　
# 7.1　函数input()的工作原理　　
# 函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# 函数int() 将数字的字符串表示转换为数值表示
age = input("age")
age = int(age)
# 求模运算符 （%）是一个很有用的工具，它将两个数相除并返回余数
print(4 % 3)
# 7.2　while循环简介　
# for 循环用于针对集合中的每个元素都一个代码块，而while 循环不断地运行，直到指定的条件不满足为止。
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# break 语句用于控制程序流程
while True:
    city = input("")
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句，
# 它不像break 语句那样不再执行余下的代码并退出整个循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# 如果程序陷入无限循环，可按Ctrl + C，也可关闭显示程序输出的终端窗口
# 7.3　使用while循环来处理列表和字典　　
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
