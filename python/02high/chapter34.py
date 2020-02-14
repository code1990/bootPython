# Python 网络编程
# Python 提供了两个级别访问的网络服务。：
#
# 低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
# 高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

# 什么是 Socket?
# Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求

# socket()函数
# Socket 对象(内建)方法

# 服务端
# 我们使用 socket 模块的 socket 函数来创建一个 socket 对象。socket 对象可以通过调用其他函数来设置一个 socket 服务。

# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()
# 获取本地主机名
host = socket.gethostbyname()
# 设置端口号
port = 12345
# 绑定端口
s.bind((host, port))
# 等待客户端连接
s.listen(5)

while True:
    # 建立客户端连接
    c, addr = s.accept()
    print("连接地址", addr)
    # 发送内容
    s.send("hello python")
    # 关闭连接
    c.close()

# 客户端
# 接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 12345。
import socket

c = socket.socket()
chost = socket.gethostbyname()
cport = 12345
c.connect((chost, cport))
print(c.recv(1024))
c.close()

# 第一个终端执行 server.py 文件：
# 第二个终端执行 client.py 文件：

# Python Internet 模块
# 以下列出了 Python 网络编程的一些重要模块：
# HTTP	网页访问	80	httplib, urllib, xmlrpclib
# NNTP	阅读和张贴新闻文章，俗称为"帖子"	119	nntplib
# FTP	文件传输	20	ftplib, urllib
# SMTP	发送邮件	25	smtplib
# POP3	接收邮件	110	poplib
# IMAP4	获取邮件	143	imaplib
# Telnet	命令行	23	telnetlib
# Gopher	信息查找	70	gopherlib, urllib

# 上述事例的简单修改
import sys

reload(sys)
sys.setdefaultencoding("utf8")
# 建立一个服务端
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind("localhost", 9000)  ##绑定要监听的端口
server.listen(5)  # 开始监听 表示可以使用五个链接排队
while True:
    conn, addr = server.accept()
    print(conn, addr)
    while True:
        data = conn.recv(1024)
        print("recive", data.decode())
        conn.send(data.upper())
    conn.close()

import sys

reload(sys)
sys.setdefaultencoding("utf8")
# 建立一个客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))
while True:
    msg = "hello python"
    client.send(msg.encode("utf-8"))
    data = client.recv(2014)
    print(data.decode())
client.close()
