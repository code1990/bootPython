#Python 计算三角形的面积
a = float(input("a"))
b = float(input("b"))
c = float(input("c"))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(area)
