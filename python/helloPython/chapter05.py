# 第5章　if语句　　64
# 5.1　一个简单示例　　64
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    # 最简单的条件测试检查变量的值是否与特定值相等
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# 5.2　条件测试　　65
# 在Python中检查是否相等时区分大小写，例如，两个大小写不同的值会被视为不相等：
# 要判断两个值是否不等，可结合使用惊叹号和等号（!= ）
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
# 关键字and 将两个条件测试合而为一；如果每个测试都通过了，整个表达式就为True ；如果至少有一个测试没有通过，整个表达式就 为False
# 关键字or 也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用or 的表达式才为False
# 要判断特定的值是否已包含在列表中，可使用关键字in
# 确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# 与条件表达式一样，布尔表达式的结果要么为True ，要么为False
# 5.3　if语句　　
# 最简单的if 语句只有一个测试和一个操作
age = 19
if age >= 18:
    print("You are old enough to vote!")
# if-else 语句块类似于简单的if 语句，但 其中的else 语句让你能够指定条件测试未通过时要执行的操作。
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
# if-elif-else 结构中的一个代码块，它依次检查每个条件测试，直到遇到通过 了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# 可根据需要使用任意数量的elif 代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# Python并不要求if-elif 结构后面必须有else 代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，Python就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的 条件。
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# 5.4　使用if语句处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
# 在for 循环中包含一条if 语句
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
# 5.5　设置if语句的格式　　80
