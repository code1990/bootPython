# Python 字符串
# 字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。

# Python 访问字符串中的值

var1 = "hello world"
var2 = "hello python"
print(var1[0])
print(var2[2:5])

# Python 字符串连接
print("输出：", var2[0] + " python")

# Python 转义字符
# \t \n \\


# Python字符串运算符
a = "hello"
b = "python"
print(a + b)
print(a * 2)
print(a[1])
print(a[1:4])

if ("H" not in a):
    print("not in", a)
else:
    print("False")

if ("M" not in a):
    print("M not in", a)
else:
    print("M not in a")

# 移除转义 直接输出
print(r'\n')
print(R'\n')

# Python 字符串格式化
# %s 格式化字符串 %d 格式化整数 %f格式化浮点数
print("my name is %s and weight is %d kg,i have %f dollar" % ("zebra", 20, 1.5))

# Python 三引号
# 可以跨多行注释

# Unicode 字符串
print(u'Hello world')

# python的字符串内建函数
# 字符串的常用方法
# 首字母大写
print("str".capitalize())
# 以a为中心执行填充
print("a".center(9, "*"))  # ****a****
# 统计单词的出现次数
print("hello".count("l"))
varStr = "中国"
print(varStr.encode("UTF-8", 'errorInfo'))
# 暂时没有发现decode方法
# print(varStr.de)
print("Hello".endswith("o"))
# 把\t转换为空格输出
print("this is\tstring example".expandtabs())
# find 查找
print("this".find("s"))
# 格式化字符串 可以指定位置 可以不指定
print("{} {}".format("hello", "world"))
print("{0} {1}".format("hello", "world"))
# 查找字符 不存在报错
print("str".index("s"))
# 都是数字或者都是字母 返回ＴＲＵＥ
print("str".isalnum())
print("%str".isalnum())
# 都是字母
print("str".isalpha())
# 都是数字
print("123".isdigit())
# 都是小写
print("Str".islower())
# 都是数字
print("12.01".isnumeric())
# 都是包含空格
print("123 123".isspace())
# 都是大写
print("Str".isupper())
# 把指定字符串加入到指定的序列当中
print("-".join(("a", "b", "c")))
# 左对齐 指定字符串长度 不够则填充
print("hello".ljust(20, "*"))
# 全部小写
print("HelloPython".lower())
# 截掉左边的空格
print("  str".lstrip())
#  maketrans() 方法用于创建字符映射的转换表
# print("123".maketrans("abc"))
# python3 没有该方法
print(max("str"))
print(min("str"))
# 类似于split
print("123.123".partition("."))
# replace
print("123".replace("1", "8"))
# rfind 类似于find函数
print("str".rfind("s"))
# rindex 类似于index函数
print("str".rindex("s"))
# rpartition
print("str".rpartition("s"))
# rstrip
print("str123 ".rstrip())
# split
print("123@123".split("@"))
# splitlines 按照\n\r\t执行分割
print("ab c\n\nde fg\rkl\r\n".splitlines())
# startwith
print("123".startswith("1"))
# strip 执行左右的strip
print(" 123 ".strip())
# swapcase 翻转大小写
print("Hello".swapcase())
# 标题化
print("hello python, hello world".title())
# translate 按照指定table来执行翻译
# print("11111".translate("abc".maketrans("123")))
# upper 转为大写形式
print("str".upper())
# zfill 给定长度 然后填充0
print("hello".zfill(10))  # 00000hello
