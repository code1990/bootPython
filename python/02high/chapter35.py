# Python SMTP发送邮件
# SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
#
# python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

# Python 发送邮件简单的实例：
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "123@qq.com"
receivers = ["1233@qq.com"]  # 接收邮件
# 三个参数 第一个参数为文本内容 第二个设置文本格式 第三个设置编码
message = MIMEText("python test email", "plain", "utf-8")
message["From"] = Header("test", "utf-8")  # 设置发送者
message["To"] = Header("测试", "utf-8")  # 接受者

subject = "python test 邮件测试"
message["Subject"] = Header(subject, "utf-8")

try:
    smtpObj = smtplib.SMTP("localhost")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送ok")
except smtplib.SMTPException:
    print("error无法发送邮件")

#     使用其他邮件服务商的 SMTP 访问
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方的邮件服务
mail_host = "smtp.xxx.com"
mail_user = "Xxx"
mail_pass = "xxx"

sender = "from@qq.com"
receivers = ["123@qq.com"]

message = MIMEText("python", "plain", "utf-8")
message["From"] = Header("hello python", "utf-8")
message["To"] = Header("test", "utf-8")

subject = "python test"
message["Subject"] = Header(subject, "utf-8")

try:
    smtpObj = smtplib.SMTP
    smtpObj.connect(mail_host, 25)  # 25 为smtp端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送ok")
except smtplib.SMTPException:
    print("error 无法发送邮件")

# 使用Python发送HTML格式的邮件
# Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

# Python 发送带附件的邮件
# 发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

# 在 HTML 文本中添加图片
# 邮件的 HTML 文本中一般邮件服务商添加外链是无效的，正确添加图片的实例如下所示：
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')
msgRoot['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

# 使用第三方 SMTP 服务发送

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '429240967@qq.com'  # 发件人邮箱账号
my_pass = 'xxxxxxxxxx'  # 发件人邮箱密码
my_user = '429240967@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
