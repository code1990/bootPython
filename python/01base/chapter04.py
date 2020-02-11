# 第四章 运算符

# 算术运算符 +-*/% ** //
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1%2)
# 取整除的整除数 3被2整除的整数
print(3//2)
# 幂运算 ** 多少次方 2的4次方
print(2**4)

# 关系运算符
a=10
b=-21
c=0
if a==b:
    print("a==b")
else:
    print("a!=b")

if a!=b:
    print("a!=b")
else:
    print("false")

if a>b:
    print("a>b")
else:
    print("false")

if a<b:
    print("a<b")
else:
    print("false")

if a>=b:
    print("a>=b")
else:
    print("false")

if a<=b:
    print("a<=b")
else:
    print("false")

# 赋值运算符
c=a+b
print(c)
c=0
# c+=b  c=c+b
c+=b
print(c)
# c*=b c =c * b
c*=b
print(c)
# c/=b c=c/b
c/=b
print(c)
# c%=b c=c%b
c%=b
print(c)
# c **= a 等效于 c = c ** a
c **=2
print(c)
# c //= a 等效于 c = c // a
print(c//2)

# Python位运算符
# & 按位与 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print(a&b)
# 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print(a|b)
# 按位异或运算符：当两对应的二进位相异时，结果为1
print(a^b)
# 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
print(~a)
#  << 右边的数字指定了移动的位数，高位丢弃，低位补0。
print(a<<2)
# >> 右边的数字指定了移动的位数
print(a>>2)


# Python逻辑运算符
if a>10 and b>10:
    print("true")
else:
    print("false")
    
if a>10 or b>10:
    print("true")
else:
    print("false")

if not(a>10 and b>10):
    print("true")
else:
    print("false")


#Python成员运算符
# in	如果在指定的序列中找到值返回 True，否则返回 False。
list = [1,2,3,4,5]
if (a in list):
    print("in===")
else:
    print("not in===")

if(b not in list):
    print("not in")
else:
    print("in")

#Python身份运算符
# is 是判断两个标识符是不是引用自一个对象
# is not 是判断两个标识符是不是引用自不同对象
if (a is b):
    print("a 和 b有相同的标识===")
else:
    print("a 和b 没有相同的标识===")

if(a is not b):
    print("a 和b 没有相同的标识")
else:
    print("false")


# is 用于判断两个变量引用对象是否为同一个(同一块内存空间)，
# == 用于判断引用变量的值是否相等。
aa =[1,2,3]
bb=aa
print(bb is aa)
print(bb == aa)
bb=aa[:]
print(aa[:])#[1, 2, 3]
print(bb is aa)
print(bb == aa)

# Python运算符优先级
# **	指数 (最高优先级)