import xlrd
import os
import time

print("1>>>>>>>>>>>>>>>读取目录下的所有的文件")
excel_path = 'F:\\Crawl website'
filter_path = 'F:\\Crawl website\\过滤.txt'
# 列出指定目录下的所有文件
file_list = os.listdir(excel_path)
print(file_list)
print("2>>>>>>>>>>>>>>>遍历所有的文件,读取所有的文件内容>>>>>>begin")
all_list = []
for file_name in file_list:
    file_path = excel_path + "\\" + file_name
    # 依次打开目录下的所有xls或者xlsx文件
    if file_path.find(".xls") > 0 or file_path.find(".xlsx") > 0:
        print("2.1>>>>>>>>>>>>>>>读取文件" + file_path)
        book = xlrd.open_workbook(file_path)
        print(type(book))
        sheet = book.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            url_info = sheet.cell_value(row, 1)
            print(url_info)
            all_list.append(url_info)
print("2>>>>>>>>>>>>>>>遍历所有的文件,读取所有的文件内容>>>>>>end")
print("3>>>>>>>>>>>>>>>处理网址获取一级域名信息")
url_simple_list = []
for url_info in all_list:
    print(url_info)
    file_list = url_info.split("://")
    simple_url = file_list[0] + "://" + file_list[1].split("/")[0]
    url_simple_list.append(simple_url)
print("4>>>>>>>>>>>>>>>网址去重")
# 利用字典的key唯一特性实现数据过滤
url_dict = {}
for url_info in url_simple_list:
    if url_info.find(".edu")>0 or url_info.find(".org")>0:
        continue
    url_dict[url_info] = url_info
print("5>>>>>>>>>>>>>>>网址过滤")
filter_str = ""
with open(filter_path, "r", encoding='utf-8') as f:
    filter_str += f.readline() + ","
# 遍历过滤库 与简化后的地址实现过滤
less_list = []
for key in url_dict.keys():
    index = key.count(".")
    if index == 1:
        domain = key.split(".")[index - 1].split("//")[1]
    elif index == 3:
        domain = key.split(".")[index - 2]
    else:
        domain = key.split(".")[index - 1]
        if len(domain) <= 3:
            domain = key.split(".")[0].split("//")[1]
    if filter_str.find(domain)<0:
        less_list.append(key)
print("6>>>>>>>>>>>>>>>过滤文件保存begin")
ctime = time.strftime("%Y%m%d%H%M%S")
with open(excel_path+"\\ok"+str(ctime)+".txt","w") as f:
    for response in less_list:
        f.write(response + '\n')
print("6>>>>>>>>>>>>>>>过滤文件保存ok")

