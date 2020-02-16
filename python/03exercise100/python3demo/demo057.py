# Python 对字符串切片及翻转
def rotate(input, d):
    Lfirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0:len(input) - d]
    Rsecond = input[len(input) - d:]

    print(Lsecond + Lfirst)
    print(Rsecond + Rfirst)


def rotate2(input):
    print(input)
    input = input[::-1]
    print(input)


if __name__ == '__main__':
    string = "hello"
    d = 2
    rotate(string, d)
    rotate2(string)
