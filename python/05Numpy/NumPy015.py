# NumPy 字符串函数
# 以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作。 它们基于 Python 内置库中的标准字符串函数。
# 这些函数在字符数组类（numpy.char）中定义。
# add()	对两个数组的逐个字符串元素进行连接
# multiply()	返回按元素多重连接后的字符串
# center()	居中字符串
# capitalize()	将字符串第一个字母转换为大写
# title()	将字符串的每个单词的第一个字母转换为大写
# lower()	数组元素转换为小写
# upper()	数组元素转换为大写
# split()	指定分隔符对字符串进行分割，并返回数组列表
# splitlines()	返回元素中的行列表，以换行符分割
# strip()	移除元素开头或者结尾处的特定字符
# join()	通过指定分隔符来连接数组中的元素
# replace()	使用新字符串替换字符串中的所有子字符串
# decode()	数组元素依次调用str.decode
# encode()	数组元素依次调用str.encode

# numpy.char.add()
# numpy.char.add() 函数依次对两个数组的元素进行字符串连接。
import numpy as np

print(np.char.add(["hello", "python"]))
print(np.char.add(["hello", "python"], ["hello", "world"]))

# numpy.char.multiply()
# numpy.char.multiply() 函数执行多重连接。
print(np.char.multiply("hello", 3))

# numpy.char.center()
# numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充。
print(np.char.center("hello", 20, fillchar="*"))

# numpy.char.capitalize()
# numpy.char.capitalize() 函数将字符串的第一个字母转换为大写：
import numpy as np

print(np.char.capitalize("hello"))

# numpy.char.title()
# numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写：
print(np.char.title("i like python"))

# numpy.char.lower()
# numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower。
print(np.char.lower("Hello"))
print(np.char.lower(["Hello", "Python"]))

# numpy.char.upper()
# numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper。
print(np.char.upper(["hello", "python"]))
print(np.char.upper("hello"))

# numpy.char.split()
# numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。
print(np.char.split(" I like python"))
print(np.char.split("www.baidu.com", sep="."))

# numpy.char.splitlines()
# numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组。
print(np.char.splitlines("I\nlike"))
print(np.char.splitlines("I\rlike"))
# \n，\r，\r\n 都可用作换行符

# numpy.char.strip()
# numpy.char.strip() 函数用于移除开头或结尾处的特定字符。
print(np.char.strip("ashoea", "a"))
print(np.char.strip(["admin", "aa", "abc"], "a"))

# numpy.char.join()
# numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
print(np.char.join(":", "java"))
print(np.char.join([":", "-"], ["java", "scala"]))

# numpy.char.replace()
# numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
print(np.char.replace("I like python", "th", "ht"))

# numpy.char.encode()
# numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。
# 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
a = np.char.encode("python", "cp500")
print(a)
# numpy.char.decode()
# numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
print(np.char.decode(a, "cp500"))
