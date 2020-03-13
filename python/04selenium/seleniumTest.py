from selenium import webdriver
# import datetime
# pip install selenium
# 一定要指明 executable_path='C:\driver\chromedriver.exe'
# 否则无法启动
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import xlsxwriter
df = pd.read_excel('D:\Documents\Downloads\Keyword Tool Export - fastener.xlsx')
driver = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
list=[]
print("bing关键字url提取>>>>>>>>begin")
for value in df.values:

    driver.get('https://cn.bing.com/?toHttps=1&redig=03D715212F154444AA84620A4607807C')

    input = driver.find_element_by_id("sb_form_q")

    input.send_keys(value)

    driver.find_element_by_id("sb_form_go").submit()

    print(driver.current_url)
    list.append(driver.current_url)
    # print(value)


print("bing关键字url提取>>>>>>>>end")
driver.quit()
print("bing关键字url数据导出>>>>>>>>end")
path = 'D:\\app\\'
name = list[0]
book = xlsxwriter.Workbook(path+name+'_link.xlsx')
sheet1 = book.add_worksheet()
for index in range(len(list)):
    value=list[index]
    sheet1.write(index, 0, value)
    print(value)
book.close()
print("bing关键字url数据导出>>>>>>>>begin")
print("邮件发送>>>>>>>>begin")
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1242903602@qq.com"  # 用户名
mail_pass = "hskqaqrkvtjmbada"  # 口令

sender = '1242903602@qq.com'
receivers = ['961902118@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText(name+"关键字地址提取完成", 'plain', 'utf-8')
message['From'] = Header(name+"关键字", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
print("邮件发送>>>>>>>>end")
# print(len(list))