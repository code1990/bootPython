# 第10章　文件和异常　　162
# 10.1　从文件中读取数据　　
# 读取整个文件
with open('pi_digits.txt') as file_object:
    # 在Windows系统中，在文件路径中使用反斜杠（\ ）而不是斜杠（/ ）
    contents = file_object.read()
    print(contents)
# 3　逐行读取
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)
# 4　创建一个包含文件各行内容的列表
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

# 10.2　写入文件　　169
# 1　写入空文件
filename = 'programming.txt'
# 调用open() 时需要提供另一个实参，告诉Python你要写入打开的文件
with open(filename, 'w') as file_object:
    # 函数write() 不会在你写入的文本末尾添加换行符
    file_object.write("I love programming.")

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# 如果你要给文件添加内容，而不是覆盖原有的内容，可以附加模式 打开文件。
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 10.3　异常　　172
# Python使用被称为异常 的特殊对象来管理程序执行期间发生的错误。
# try-except 代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
# 处理ZeroDivisionError 异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 依赖于try 代码块成功执行的代码都应放到else 代码块中：
while True:

    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 处理FileNotFoundError 异常
try:
    with open('alice.txt') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file 'alice.txt' does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print(num_words)


# 使用多个文件
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# Python有一个pass 语句，可在代码块中使用它来让Python 什么都不要做
def count_words(filename):
    try:
        print(filename)
    except FileNotFoundError:
        pass
    else:
        print(filename)


# 10.4　存储数据　　180
# 使用json.dump() 和json.load()
import json

# 使用json.dump() 来存储这组数字
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# 使用json.load() 将这个列表读取到内存中
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)
# 2　保存和读取用户生成的数据
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")


# 将代码划分为一系列完成具体工作的函数。这样的过程被称为重构 。重构让代码更清晰、更易于理 解、更容易扩展。
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")


greet_user()
