# Python 正则表达式
# re 模块使 Python 语言拥有全部的正则表达式功能。

# re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
import re

print(re.match("www", "www.baidu.com"))  # 在起始位置匹配
print(re.match("com", "www.baidu.com"))  ## 不在起始位置匹配

line = "cats are smarter than logs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1)", matchObj.group(1))
    print("matchObj.group(2)", matchObj.group(2))
else:
    print("No match!")

# re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group():", searchObj.group())
    print("searchObj.group(1):", searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("Nothing found!")

# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group():", matchObj.group())
else:
    print("no match!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> searchObj.group()", matchObj.group())
else:
    print("no match!")

# 检索和替换
# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)


# repl 参数是一个函数
# 以下实例中将字符串中的匹配的数字乘以 2：

# # 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
print(pattern.match("one12twothree34four"))  ## 查找头部，没有匹配

print(pattern.match('one12twothree34four', 2, 10))  ## 从'e'的位置开始匹配，没有匹配
m = pattern.match('one12twothree34four', 3, 10)
print(m)  # 从'1'的位置开始匹配，正好匹配

print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.match("hello world wide web")
print(m)

print(m.group(0))  # 返回匹配成功的整个子串
print(m.span(0))  # 返回匹配成功的整个子串的索引
print(m.group(1))  # 返回第一个分组匹配成功的子串
print(m.span(1))  # 返回第一个分组匹配成功的子串的索引
print(m.group(2))  # 返回第二个分组匹配成功的子串
print(m.span(2))  # 返回第二个分组匹配成功的子串
print(m.groups())  # 等价于 (m.group(1), m.group(2), ...)
# print(m.group(3))  # 不存在第三个分组

# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#
# 注意： match 和 search 是匹配一次 findall 匹配所有。

pattern=re.compile("r\d+") #查找数字
result1=pattern.findall("123 google")
result2=pattern.findall("123google")
print(result1)
print(result2)

# re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r"\d+","12abc123")
for match in it:
    print(match.group())
# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下
print(re.split("\W+","hello python java"))
print(re.split("\W+","hello python java",1))
print(re.split("a*","hello world"))

# 正则表达式对象
# re.RegexObject
# re.compile() 返回 RegexObject 对象。
#
# re.MatchObject
# group() 返回被 RE 匹配的字符串。
#
# start() 返回匹配开始的位置
# end() 返回匹配结束的位置
# span() 返回一个元组包含匹配 (开始,结束) 的位置

s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())
