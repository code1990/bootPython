# Python 文件 IO
# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("123")

with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)
