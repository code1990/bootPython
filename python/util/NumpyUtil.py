import numpy as np

"""
numpy工具类
"""

"""
计算平均值
"""
def get_avg(data_list):
    return np.mean(data_list)


"""
方差是各个数据与平均数之差的平方的平均数
"""
def get_vari(data_list):
    return np.var(data_list)


"""
标准差 方差开根号 反映的是一维数组的离散程度
"""
def get_std_dev(data_list):
    return np.std(data_list, ddof = 0)


"""
协方差是对2组数据进行统计的，反映的是2组数据之间的相关性
"""
def get_cov(data_list1, data_list2):
    return np.cov(data_list1, data_list2, ddof=0)[1][0]

# #中位数
# np.median(nums)
# 求众数方法一：
# import numpy as np
# #bincount（）：统计非负整数的个数，不能统计浮点数
# counts = np.bincount(nums)
# #返回众数
# np.argmax(counts)