# Python While 循环语句
a = 1
while a < 10:
    print(a)
    a += 2

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

count = 0
while (count < 9):
    print("this count is ".count)
    count += 1

print("Good bye")

i = 1
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

while True:
    num = 123
    print("your entered:", num)
    break

print("Good bye")

count = 0
while (count < 5):
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")

# 简单语句组
while (True): print("Given flag is really true");
print("good bye")
