# Python 实现秒表功能
import time

print("ctrl+c")
while True:
    input("in")
    starttime = time.time()
    print("begin")
    try:
        while True:
            print(round((time.time() - starttime), 0))
    except KeyboardInterrupt:
        print("end")
        endtime = time.time()
        print(round((time.time() - endtime), 0))
        break
