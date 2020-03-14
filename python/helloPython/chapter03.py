# 第3章　列表简介　　
# 3.1　列表是什么　　
# 列表 由一系列按特定顺序排列的元素组成。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可
print(bicycles[0])
print(bicycles[0].title())
# 在Python中，第一个列表元素的索引为0，而不是1
# 通过将索引指定为-1 ，可让Python返回最后一个列表元素
print(bicycles[-1])
# 3.2　修改、添加和删除元素　　
# 修改列表元素的语法与访问列表元素的语法类似。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
# 在列表中添加新元素时，最简单的方式是将元素附加到列表末尾。
motorcycles.append('ducati')
# 使用方法insert() 可在列表的任何位置添加新元素。
motorcycles.insert(0, 'ducati')
# 如果知道要删除的元素在列表中的位置，可使用del 语句。
del motorcycles[0]
# 方法pop() 可删除列表末尾的元素，并让你能够接着使用它
popped_motorcycle = motorcycles.pop()
print(motorcycles)
# 你可以使用pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
owned = motorcycles.pop(0)
print(owned)
# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；
# 如果你要在删除元 素后还能继续使用它，就使用方法pop() 。
# 如果你只知道要删除的元素的值，可使用方法remove()
motorcycles.remove('ducati')
# 3.3　组织列表　　
# Python方法sort() 让你能够较为轻松地对列表进行排序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted() 。
print(sorted(cars))
# 要反转列表元素的排列顺序，可使用方法reverse()
cars.reverse()
print(cars)
# 使用函数len() 可快速获悉列表的长度
print(len(cars))
# 3.4　使用列表时避免索引错误　　
