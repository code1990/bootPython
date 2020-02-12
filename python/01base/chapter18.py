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

# 返回格林威治西部的夏令时地区的偏移秒数
print(time.altzone)
# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"
print(time.asctime())

# 用以浮点数计算的秒数返回当前的CPU时间//
# print(time.clock())

# 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print(time.ctime())

# 返回格林威治天文时间下的时间元组t
print(time.gmtime())

# 接收时间戳
print(time.localtime())

# 接受时间元组并返回时间戳
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
print(time.mktime(t))

# 推迟调用线程的运行
# time.sleep(1000)

# 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
print("----")
# print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(time.mktime(2009, 2, 17, 17, 3, 38, 1, 48, 0))))

#根据fmt的格式把一个时间字符串解析为时间元组。
print(time.strptime("30 Nov 00", "%d %b %y"))

# 返回当前时间的时间戳
print(time.time())

# 根据环境变量TZ重新初始化时间相关设置。 无返回值
# time.tzset()

# Time模块包含了以下2个非常重要的属性：
print(time.timezone)#当地时区 偏移量
print(time.tzname)#('中国标准时间', '中国夏令时')



# 日历（Calendar）模块
# 获取给定年份 月份 日的日历信息
print(calendar.calendar(2006))

# 返回当前每周起始日期的设置
print("*****")
print(calendar.firstweekday)

# 是否为闰年
print(calendar.isleap(2000))

# 返回在Y1，Y2两年之间的闰年总数。
print(calendar.leapdays(2000,2016))

# 返回一个多行字符串格式的year年month月日历
print(calendar.month(2000,1))

# 返回一个整数的单层嵌套列表
print(calendar.monthcalendar(2000,1))

# 返回两个整数
print(calendar.monthrange(2000,1))

# calendar.prcal() 相当于 print calendar.calendar()。
print(calendar.prcal(2000))

# calendar.prmonth()相当于 print calendar.month() 。
print("=======")
print(calendar.prmonth(2000,1))

# calendar.setfirstweekday(weekday)
# 设置每周的起始日期码。0（星期一）到6（星期日）。
print("*****")
print(calendar.setfirstweekday(0))

# calendar.timegm(tupletime)
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳
import datetime
d = datetime.datetime(2010, 10, 10)
print(calendar.timegm(d.timetuple()))

# 返回给定日期的日期码 calendar.weekday(year,month,day)
print(calendar.weekday(2000,1,1))
# 其他相关模块和函数
# 在Python中，其他处理日期和时间的模块还有：
#
# datetime模块
# pytz模块
# dateutil模块
