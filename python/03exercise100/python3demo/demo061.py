# Python 合并字典
# 实例 1 : 使用 update() 方法，第二个参数合并第一个参数
def Merge(dict1, dict2):
    return dict2.update(dict1)


def Merge2(dict1, dict2):
    result = {**dict1, **dict2}
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(Merge(dict1, dict2))
print(Merge2(dict1, dict2))
# 实例 2 : 使用 **，函数将参数以字典的形式导入
