# Python 判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
    except(TypeError, ValueError):
        pass

    return False

print(is_number("foo"))
print(is_number("123"))
print(is_number("1.3"))