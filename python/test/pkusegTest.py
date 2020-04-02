import pkuseg
if __name__ == '__main__':
    # freeze_support()
    pkuseg.test(r'C:\Users\admin\Desktop\tmp.txt', r'C:\Users\admin\Desktop\tmp1.txt', nthread=20)
#对input.txt的文件分词输出到output.txt中，使用默认模型和词典，开20个进程