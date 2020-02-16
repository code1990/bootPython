# Python 判断字符串是否存在子字符串
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("不存在")
    else:
        print("存在")


string = "hello python"
sub_str = "python"
print(check(string, sub_str))

if sub_str in string:
    print("in")
else:
    print("not in")
