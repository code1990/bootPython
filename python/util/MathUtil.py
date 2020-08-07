import math

"""
数学工具类
"""

"""
计算平均值
"""
def get_avg(data_list):
    return sum(data_list) / len(data_list)


"""
方差是各个数据与平均数之差的平方的平均数
"""
def get_vari(data_list):
    avg = get_avg(data_list)
    square_data_list = []
    for i in data_list:
        square_data_list.append((i - avg) * (i - avg))
    return sum(square_data_list) / len(square_data_list)


"""
标准差 方差开根号 反映的是一维数组的离散程度
"""
def get_std_dev(data_list):
    return math.sqrt(get_vari(data_list))


"""
协方差是对2组数据进行统计的，反映的是2组数据之间的相关性
"""
def get_cov(data_list1, data_list2):
    avg1 = get_avg(data_list1)
    avg2 = get_avg(data_list2)
    temp_data_list = []
    for i in range(0, len(data_list1)):
        temp_data_list.append((data_list1[i] - avg1) * (data_list2[i] - avg2))
    return sum(temp_data_list) / len(temp_data_list)
