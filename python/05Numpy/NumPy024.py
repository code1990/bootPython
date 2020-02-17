# NumPy IO
# Numpy 可以读写磁盘上的文本数据或二进制数据。
#
# NumPy 为 ndarray 对象引入了一个简单的文件格式：npy。
#
# npy 文件用于存储重建 ndarray 所需的数据、图形、dtype 和其他信息。
#
# 常用的 IO 函数有：
#
# load() 和 save() 函数是读写文件数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npy 的文件中。
# savze() 函数用于将多个数组写入文件，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npz 的文件中。
# loadtxt() 和 savetxt() 函数处理正常的文本文件(.txt 等)

# numpy.save()
# numpy.save() 函数将数组保存到以 .npy 为扩展名的文件中。

# np.savez
# numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中。

# savetxt()
# savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。

