# 第8章　函数　　114
# 8.1　定义函数　　114
# 打印问候语的简单函数，名为greet_user()
def greet_user():
    print("Hello!")


greet_user()


# 向函数传递信息
def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('jesse')


# 在函数greet_user() 的定义中，变量username 是一个形参 ——函数完成其工作所需的一项信息。
# 在代码greet_user('jesse') 中，值'jesse' 是一个实参 。
# 8.2　传递实参　　116
# 向函数传递实参的方式很多，可使用位置实参 ，这要求实参的顺序与形参的顺序相同；也可使用关键 字实参 ，其中每个实参都由变量名和值组成；还可使用列表和字典。
# 最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# 你可以根据需要调用函数任意次
# 使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料
# 关键字实参 是传递给函数的名称—值对
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 编写函数时，可给每个形参指定默认值
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')


# 8.3　返回值　　121
# 函数返回的值被称为返回值 。在函数中，可使用return 语句将值返回到调用函数的代码行。
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# 返回字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


# 8.4　传递列表　　126
# 将列表传递给函数后，函数就能直接访问其内容
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()


# 禁止函数修改列表
# 切片表示法[:] 创建列表的副本
# function_name(list_name[:])

# 8.5　传递任意数量的实参　　130
# Python允许函数从调用语句中收集任意数量的实参
def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch ")
    for topping in toppings:
        print("- " + topping)


#形参**user_info 中的两个星号让Python创建一个名为user_info 的 空字典，并将收到的所有名称—值对都封装到这个字典中
def build_profile(first, last, **user_info):
    profile = {}

# 8.6　将函数存储在模块中　　133
# 将函数存储在被称为模块 的独立文件中， 再将模块导入 到主程序中。import 语句允许在当前运行的程序文件中使用模块中的代码。
# 1　导入整个模块
# import pizza
# 2　导入特定的函数
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2
# 3　使用as 给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名
# from module_name import function_name as fn
# 4　使用as 给模块指定别名
# import module_name as mn
# 5　导入模块中的所有函数
# 使用星号（* ）运算符可让Python导入模块中的所有函数
# from pizza import *
# 8.7　函数编写指南　　136
