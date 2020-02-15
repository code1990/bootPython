# 题目：列表使用实例。
testList = [10086, "中国移动", [1, 2, 3, 4]]
# 列表的长度
print(len(testList))
# 到列表结尾
print(testList[1:])
# 向列表添加元素
testList.append("new here")
print(len(testList))
print(len(testList[-1]))
# 弹出列表的一个一个元素
print(testList.pop())
print(testList)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix]
print(col2)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
print(col2even)
