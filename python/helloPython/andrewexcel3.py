import xlrd
import os
import time
import re

print("1>>>>>>>>>>>>>>>读取目录下的所有的文件")
excel_path = 'F:\\Crawl website'
filter_path = 'F:\\Crawl website\\过滤.txt'
# 列出指定目录下的所有文件
file_list = os.listdir(excel_path)
print(file_list)
print("2>>>>>>>>>>>>>>>遍历所有的文件,读取所有的文件内容>>>>>>begin")
for file_name in file_list:
    file_path = excel_path + "\\" + file_name
    # 依次打开目录下的所有xls或者xlsx文件
    if file_path.find(".xls") > 0 or file_path.find(".xlsx") > 0:
        print("2.1>>>>>>>>>>>>>>>读取文件" + file_path)
        book = xlrd.open_workbook(file_path)
        sheet = book.sheet_by_index(0)
        all_list = []
        for row in range(1, sheet.nrows):
            url_info = sheet.cell_value(row, 1)
            all_list.append(url_info)
        print("2>>>>>>>>>>>>>>>遍历所有的文件,读取所有的文件内容>>>>>>end")
        print("3>>>>>>>>>>>>>>>处理网址获取一级域名信息")
        url_simple_list = []
        for url_info in all_list:
            file_list = url_info.split("://")
            simple_url = ""
            if len(file_list) == 2:
                if file_list[1].find("/") > 0:
                    simple_url = file_list[0] + "://" + file_list[1].split("/")[0]
                else:
                    simple_url = file_list[0] + "://" + file_list[1]
            url_simple_list.append(simple_url)
        print("4>>>>>>>>>>>>>>>网址去重")
        # 利用字典的key唯一特性实现数据过滤
        url_dict = {}
        for url_info in url_simple_list:
            url_dict[url_info] = url_info
        print("5>>>>>>>>>>>>>>>网址过滤")
        filter_list = []
        with open(filter_path, "r", encoding='utf-8') as f:
            filter_list = f.readlines()
            f.close()
        filter_str = ""
        for str in filter_list:
            filter_str += str.replace('\n', '') + ","
        filter_str = filter_str.lower()
        # 遍历过滤库 与简化后的地址实现过滤
        less_list = []
        for key in url_dict.keys():
            flag = False
            for tmp in key.split("."):
                if filter_str.find(tmp) > 0:
                    flag = True
                    break
            if not flag:
                less_list.append(key)
        print("6>>>>>>>>>>>>>>>过滤文件保存begin")
        result_list = re.findall('[a-zA-Z]+', file_name)
        tmp_name = ""
        for result in result_list:
            if result == "xls" or result == "xlsx" or result == "txt":
                continue
            tmp_name += result + " "
        ctime = time.strftime("%Y%m%d")
        final_name = tmp_name + ctime
        with open(excel_path + "\\" + final_name + ".txt", "w", encoding='utf-8') as f:
            for response in less_list:
                f.write(response + '\n')
            f.close()
        print("6>>>>>>>>>>>>>>>过滤文件保存ok")
        print("文件总记录数:", len(all_list))
        print("文件过滤后记录数:", len(less_list))
