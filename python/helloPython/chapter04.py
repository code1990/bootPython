# 第4章　操作列表　　
# 4.1　遍历整个列表　　
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 4.2　避免缩进错误　
# Python根据缩进来判断代码行与前一个代码行的关系。　
# 4.3　创建数值列表　　
# Python函数range() 让你能够轻松地生成一系列的数字。
# 函数range() 让Python从你指定的第一个值开始数，并在到达你指定的第二个值 后停止，因此输出不包含第二个值（这里为5）
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [value ** 2 for value in range(1, 11)]
print(squares)
# 4.4　使用列表的一部分
# 你还可以处理列表的部分元素——Python称之为切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# 如果你没有指定第一个索引，Python将自动从列表开头开始
print(players[:4])
# 要让切片终止于列表末尾，也可使用类似的语法
print(players[2:])
for player in players[:3]:
    print(player.title())
# 复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:] ）
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
# 4.5　元组　　
# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。
dimensions = (200, 50)
print(dimensions[0])
# 遍历
for dimension in dimensions:
    print(dimension)
# 修改
dimensions = (400, 100)
print(dimensions)

# 4.6　设置代码格式　　
