# Python 元组
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
t1 = ("python", "java", 1, 2)
print(t1)
# 创建空数组
t2 = ()
# 创建包含一个元素的数组
t3 = (12,)

# 访问元组
print(t1[0])
print(t1[1:2])
# 修改元组
# 修改元祖的方式是非法的
# t1[0]="scala"

# 删除元组
del t3

# 元组运算符
# 获取元祖的长度
print(len(t1))
# 连接
print((1, 2, 3) + (4, 5, 6))
# 复制
print((1,) * 5)
# 元素是否存在
print(1 in (1, 2, 3))
# 元素迭代
for x in (1, 2, 3): print(x)
# 元组索引，截取

t5 = (1, 2, 3)
print(t5[2])
print(t5[-1])
print(t5[1:])

# 无关闭分隔符
# 任意无符号的对象，以逗号隔开，默认为元组


# 元组内置函数
# cmp元素移除
print(t5)
print(len(t5))
# max min
print(max(t5))
print(min(t5))
print(tuple([1, 2, 3, 4, 5, 6]))
