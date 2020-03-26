
from selenium import webdriver
import xlrd
import datetime
import xlwt
import smtplib
import xlsxwriter
from email.mime.text import MIMEText
from email.header import Header

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
list=[]
print("google关键字url提取>>>>>>>>begin")
f = xlrd.open_workbook('D:\Keyword Tool bolts inc.xlsx')
table = f.sheets()[0]
value = table.col_values(0,)
start_time = datetime.datetime.now()
name=""
for i in range(len(value)):

    driver.get('https://www.google.com.hk/')

    input = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    if(name==""):
        name=value[i]
    input.send_keys(value[i])
    # print("111111111",value[i])
    driver.find_element_by_name("btnK").submit()

    print(driver.current_url)
    list.append(driver.current_url)

delta_time = datetime.datetime.now() - start_time
print(delta_time)

print("google关键字url提取>>>>>>>>end")
driver.quit()
print("google关键字url数据导出>>>>>>>>end")
path = 'D:\\'
book = xlsxwriter.Workbook(path+name+'_link.xlsx')
sheet1 = book.add_worksheet()
for index in range(len(list)):
    value=list[index]
    sheet1.write(index, 0, value)
    print(value)
book.close()
print("google关键字url数据导出>>>>>>>>begin")
print("邮件发送>>>>>>>>begin")
# 第三方 SMTP服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1242903602@qq.com"  # 用户名
mail_pass = "hskqaqrkvtjmbada"  # 口令

sender = '1242903602@qq.com'
receivers = ['961902118@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
content = "采集url数量:"+str(len(list))+"\n开始时间:"+str(start_time)+"\n总共用时:"+str(delta_time)
print(content)
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header(name+"关键字", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = (name+'采集任务已完成')
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