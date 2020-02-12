# Python 日期和时间
# Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

import time
# 获取当前的时间戳
ticks = time.time()
print(ticks)

# 什么是时间元组？
# 很多Python函数用一个元组装起来的9组数字处理时间:
# 上述也就是struct_time元组。这种结构具有如下属性：struct_time 具体的解释如下
localtime = time.localtime(ticks)
print(localtime)
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=12, tm_hour=11, tm_min=59, tm_sec=13, tm_wday=2, tm_yday=43, tm_isdst=0)

# 获取格式化的时间
# 最简单的获取可读的时间模式的函数是asctime():
localtime=time.asctime(time.localtime(ticks))
print(localtime)#Wed Feb 12 12:04:06 2020
# 格式化日期
# 我们可以使用 time 模块的 strftime 方法来格式化日期，：
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))




# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar
cal = calendar.month(2020,1)
# 打印出一月份的日历
print(cal)

# Time 模块
# Time 模块包含了以下内置函数，既有时间处理的，也有转换时间格式的


# 日历（Calendar）模块
# 此模块的函数都是日历相关的，例如打印某月的字符月历。


# 其他相关模块和函数
# 在Python中，其他处理日期和时间的模块还有：
#
# datetime模块
# pytz模块
# dateutil模块
