# Python list 常用操作
# list定义
li = ["java", "python", "scala", "php", "swift"]
print(li[0])
# list负数索引
print(li[-1])
print(li[-3])
print(li)
print(li[1:3])
print(li[1:-1])
print(li[0:3])

# 增加元素
li.append("cpp")
li.insert(2, "csharp")
li.extend(["c", "javascript"])
print(li)

# list搜索
print(li.index("python"))
print(li.index("c"))
print()

# list删除
li.remove("csharp")
li.pop()

# list运算符
li2 = ["a", "b"]
li = li + li2
print(li)
li += li
print(li)
li = [1, 2] * 3
print(li)

# 7.使用join链接list成为字符串

# 8.list 分割字符串

li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
s.split(";")
s.split(";", 1)
# split 与 join 正好相反, 它将一个字符串分割成多元素 list。

# 9.list 的映射解析

li = [1, 9, 8, 4]
li = [elem * 2 for elem in li]
# 10.dictionary 中的解析

params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
params.keys()
params.values()
params.items()
# 11.list 过滤

li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
