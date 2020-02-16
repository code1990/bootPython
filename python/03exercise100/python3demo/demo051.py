# Python 移除字符串中的指定位置字符
test_str = "hello python"

new_str = ""
for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print(new_str)
print(test_str.replace(test_str[3], "", 1))


def ff(str, num):
    return str[:num] + str[num + 1:]


str = "hello python"
print(ff(str, 2))
print(ff(str, 4))
