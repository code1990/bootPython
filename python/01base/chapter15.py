# Python 列表(List)
# 序列是Python中最基本的数据结构。
# 访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1[0])
print(list1[0:2])
# 更新列表
list1.append("google")
print(list1)
# 删除列表元素
del list1[2]
print(list1)
# Python列表脚本操作符
print(len(list1))
print(list1 + [4, 5, 6])
print([1] * 4)
print(3 in [1, 3])
for x in [1, 2, 3]: print(x)
# Python列表截取
l = ["google", "apple", "microsoft"]
print(l[2])
print(l[-2])
print(l[1:])

# Python列表函数&方法
# cmp比较两个列表的元素 3.0 版本开始没这个函数了
print(len([1, 2, 3]))
# max/min 返回list中的最大的元素
print(min([1, 2, 3]))
print(max([1, 2, 3]))
# list将元祖转换为list
print(list((1, 2, 3)))
l.append("tesla")
print(l)
# 统计元素出现的次数 count
print(l.count("tesla"))
# 在尾部追加元素
l.extend(("fackbook", "yahoo"))
print(l)
# index 查找给定元素的索引值
print(l.index("apple"))
# 给定位置插入元素
l.insert(1, "apache")
print(l)
# 移除给定索引位置的元素
l.pop(1)
print(l)
# 移除给定元素
l.remove("yahoo")
print(l)
# reverse 元素翻转
l.reverse()
print(l)
# sort 对list排序
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
ll = [1, 4, 2, 3, 6, 8, 9, 5]
ll.sort(reverse=False)
print(ll)
ll.sort(reverse=True)
print(ll)
