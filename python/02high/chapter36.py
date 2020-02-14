# Python 多线程
# 多线程类似于同时执行多个不同程序

# 开始学习Python线程
# Python中使用线程有两种方式：函数或者用类来包装线程对象。
#
# 函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:

def test_thread():
    import _thread
    import time

    # 为线程定义一个函数
    def print_time(thredName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s:%s" % (thredName, time.ctime(time.time())))

    # 创建2个线程
    try:
        _thread.start_new_thread(print_time, ("thread-1", 2,))
        _thread.start_new_thread(print_time, ("thread-1", 2,))
    except:
        print("error 无法启动线程")

    while 1:
        pass


# 线程模块
# Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
#
# _thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
#
# threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
#
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
#
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

# 使用 threading 模块创建线程
# 我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")

# 线程同步
# 使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，
# 对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。

threadLock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程:" + self.name)
        #         获取锁 用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        #         释放锁
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threads=[]
# 创建新线程
thread1= MyThread(1,"thread-1",1)
thread2= MyThread(1,"thread-2",1)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
    print("退出主线程")

# 线程优先级队列（ Queue）
# Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
#
# 这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
#
# Queue 模块中的常用方法:
#
# Queue.qsize() 返回队列的大小
# Queue.empty() 如果队列为空，返回True,反之False
# Queue.full() 如果队列满了，返回True,反之False
# Queue.full 与 maxsize 大小对应
# Queue.get([block[, timeout]])获取队列，timeout等待时间
# Queue.get_nowait() 相当Queue.get(False)
# Queue.put(item) 写入队列，timeout等待时间
# Queue.put_nowait(item) 相当Queue.put(item, False)
# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作
import queue
exitFlag=0
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
class myThread(threading.Thread):
    def __init__(self,threadId,name,q):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.name=name
        self.q=q

    def run(self):
        print("开启线程"+self.name)
        process_data(self.name,self.q)
        print_time("退出线程"+self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)


# 创建新线程
for tName in threadList:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    thread.append(thread)
    threadID+=1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag=1

# 等待所有的线程完成
for t in threads:
    t.join()
print("主线程退出")
