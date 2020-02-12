# Python 字典(Dictionary)
# 字典是另一种可变容器模型，且可存储任意类型对象。
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
# 访问字典里的值

print(dict1["a"])
# 修改字典

dict1["a"] = 100
print(dict1)

# 删除字典元素


# 字典键的特性
# 1）不允许同一个键出现两次
# 2）键必须不可变，所以可以用数字，字符串或元组充当


# 字典内置函数&方法
# cmp python3移除
print(len(dict1))
print(str(dict1))
print(type(dict1))
dict2 = {"a": 100}
# clear
dict2.clear()
# 字典的浅复制
print(dict1.copy())
# 创建一个新字典
dict2 = dict.fromkeys((1, 2, 3), 10)
print(dict2)
# get
print(dict1.get("a", "123"))
# has_key== __contains__
print(dict1.__contains__("a"))
# items
# 遍历字典列表
for key, values in dict1.items():
    print(key, values)

#     keys
for key in dict1.keys():
    print(key)

#     values
for value in dict1.values():
    print(value)

# update 追加一个字典进来
dict1.update({"d": 4})
print(dict1)
# pop 删除给定的key 返回value 无则返回默认值
print(dict1.pop("a", "123"))
# setdefault 设置默认的
dict1.setdefault("e", "123")
print(dict1)
# popitem 返回字典中最后一对key和value 并删除它
print(dict1.popitem())
print(dict1)
