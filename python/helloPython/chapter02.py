# 第2章　变量和简单数据类型　　
# 2.1　运行hello_world.py时发生的情况　　
print("Hello Python world!")
# 2.2　变量　　
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
# 2.2.1　变量的命名和使用
#
# 请务必牢记下述有关变量的规则。
#
#   变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，
#   例如，可将变量命名为message_1，但不能将其命名为1_message。
#
#   变量名不能包含空格，但可使用下划线来分隔其中的单词。
#   例如，变量名greeting_message可行，但变量名greeting message会引发错误。
#
#   不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，
#   如print （请参见附录A.4）。
#
# 变量名应既简短又具有描述性。
# 例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
#
#   慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

# 2.3　字符串　　
"This is a string."
'This is also a string.'
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# 要确保字符串末尾没有空白，可使用方法rstrip()
print('python '.rstrip())
# 你还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip() 和strip()
print(' python'.lstrip())
print(' python '.strip())
# 2.4　数字　　24
# 可对整数执行加（+ ）减（- ）乘（* ）除（/ ）运算
print(1+2)
print(1-2)
print(1*2)
print(1%2)
# Python使用两个乘号表示乘方运算
print(2**2)
print(2**3)
# Python还支持运算次序
print(2*2+1)
# Python将带小数点的数字都称为浮点数
# 结果包含的小数位数可能是不确定
print(0.02+0.01)
# 可调用函数str() ， 它让Python将非字符串值表示为字符串
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
# 在Python 2中，整数除法的结果只包含整数部分，小数部分被删除
print(3/2)
print(3.0/2)
# 2.5　注释　　
# 注释用井号（# ）标识
# 编写注释的主要目的是阐述代码要做什么，以及是如何做的。
# 2.6　Python之禅　　
