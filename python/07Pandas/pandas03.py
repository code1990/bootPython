# Pandas快速入门
# 测试工作环境是否有安装好了Pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("hello pandas")
# 通过传递值列表来创建一个系列，让Pandas创建一个默认的整数索引
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
dates = pd.date_range("20170101", periods=7)
print(dates)
print("--" * 16)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list("ABCD"))
print(df)
# 通过传递可以转换为类似系列的对象的字典来创建DataFrame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20170102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
# 查看框架的顶部和底部的数据行。
print(df.head())
print(df.tail(3))
# 显示索引，列和底层numpy数据
print(df.index)
print(df.columns)
print(df.values)
# 描述显示数据的快速统计摘要
print(df.describe())
# 调换数据
print(df.T)
# 通过轴排序
print(df.sort_index(axis=1, ascending=False))
# 按值排序
print(df.sort_values(by='B'))
# 选择一列，产生一个系列，相当于df.A
print(df['A'])
# 选择通过[]操作符，选择切片行
print(df[0:3])
print(df['20170102':'20170103'])
# 使用标签获取横截面，参考以下示例程序 -
print(df.loc[dates[0]])
# 通过标签选择多轴，参考以下示例程序 -
print(df.loc[:, ['A', 'B']])
# 显示标签切片，包括两个端点，参考以下示例程序 -
print(df.loc['20170102':'20170104', ['A', 'B']])
# 减少返回对象的尺寸(大小)，参考以下示例程序 -
print(df.loc['20170102', ['A', 'B']])
# 获得标量值，参考以下示例程序 -
print(df.loc[dates[0], 'A'])
# 快速访问标量(等同于先前的方法)，参考以下示例程序 -
print(df.at[dates[0], 'A'])
# 通过传递的整数的位置选择，参考以下示例程序 -
print(df.iloc[3])
# 通过整数切片，类似于numpy/python，参考以下示例程序 -
print(df.iloc[3:5, 0:2])
# 通过整数位置的列表，类似于numpy/python样式，参考以下示例程序 -
print(df.iloc[[1, 2, 4], [0, 2]])
# 明确切片行，参考以下示例程序 -
print(df.iloc[1:3, :])
# 明确切片列，参考以下示例程序 -
print(df.iloc[:, 1:3])
# 要明确获取值，参考以下示例程序 -
print(df.iloc[1, 1])
# 要快速访问标量(等同于先前的方法)，参考以下示例程序 -
print(df.iat[1, 1])
# 使用单列的值来选择数据，参考以下示例程序 -
print(df[df.A > 0])
# 从满足布尔条件的DataFrame中选择值。，参考以下示例程序 -
print(df[df > 0])
# 使用isin()方法进行过滤，参考以下示例程序 -
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2["E"].isin(["two", "three"])])
