# Python CGI编程
# CGI(Common Gateway Interface)，通用网关接口，它是一段程序，运行在服务器上如：HTTP 服务器，提供同客户端 HTML 页面的接口。

# 在你进行 CGI 编程前，确保您的 Web 服务器支持 CGI 及已经配置了 CGI 的处理程序。

# 简单的url实例：GET方法
# 使用POST方法传递数据
import cgi, cgitb

form = cgi.FieldStorage
site_name = form.getvalue("name")
site_url = form.getvalue("url")

# cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据 ，
# 当下次客户访问脚本时取回数据信息，从而达到身份判别的功能，cookie 常用在身份校验中。
# cookie的语法
# http cookie的发送是通过http头部来实现的，他早于文件的传递，头部set-cookie的语法如下：
# #保存 cookie 到变量
import urllib.request
import http.cookiejar
cookie = http.cookiejar.CookieJar()
handler= urllib.request.HTTPCookieProcessor(cookie)
opener= urllib.request.build_opener(handler)
response=opener.open("https://www.baidu.com")

for item in cookie:
    print("%s=%s" %(item.name,item.value))


# 文件上传实例
# import cgi, os
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

# 或文件名
fileitem = form["filename"]

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open("/tmp/" + fn, "wb").write(fileitem.file.read())
    message = "文件" + fn + "上传成功"
else:
    message = "文件没有上传"

#     文件下载对话框
# 打开文件
fo = open("foo.txt", "rb")
str = fo.read()
print(str)
# 关闭文件
fo.close()
