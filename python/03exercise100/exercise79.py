# 题目：字符串排序。
if __name__ == "__main__":
    str1 = input("")
    str2 = input("")
    str3 = input("")
    print(str1, str2, str3)

    if str1 > str2: str1, str2 = str2, str1
    if str1 > str3: str1, str3 = str3, str1
    if str2 > str3: str2, str3 = str3, str2

    print(str1, str2, str3)
