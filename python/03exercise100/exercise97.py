# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
if __name__ == "__main__":
    from sys import stdout

    filename = input("请输入文件名\n")
    fp = open(filename, "w")
    ch = input("请输入字符串\n")
    while ch != "#":
        fp.write(ch)
        stdout.write(ch)
        ch = input("")
    fp.close()
