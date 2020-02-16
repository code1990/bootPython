# Python 获取几天前的时间
import time
import datetime

threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
timeStamp = int(time.mktime(threeDayAgo.timetuple()))

otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

# 给定时间戳
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days=3)
print(threeDayAgo)
