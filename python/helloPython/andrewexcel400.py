import xlrd
import os
import time
import re

# print("1>>>>>>>>>>>>>>>读取目录下的所有的文件")
root_path = r'C:\Users\admin\Desktop\新建文件夹 (3)'
excel_path = r'C:\Users\xiala\Desktop\123'
filter_path = r'C:\Users\admin\Desktop\新建文件夹 (3)\过滤.txt'
# 列出指定目录下的所有文件
all_file_list = os.listdir(excel_path)
# print(len(all_file_list))
all_list = []
for file_name in all_file_list:
    file_path = excel_path + "\\" + file_name
    if file_path.find(".xls") > 0 or file_path.find(".xlsx") > 0:
        book = xlrd.open_workbook(file_path)
        sheet = book.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            url_info =""
            for index in range(9):
                url_info += str(sheet.cell_value(row, index).strip())+"\t"
            if url_info.find("债") > 0 or url_info.find("ETF") > 0 or url_info.find("FOF") > 0:
                continue
            # print(url_info.replace("(", "\t"))
            print(url_info)
            # if url_info == '':
            #     continue
            # all_list.append(url_info)
# print("2>>>>>>>>>>>>>>>遍历所有的文件,读取所有的文件内容>>>>>>end")
# print(len(all_list))
# print("3>>>>>>>>>>>>>>>处理网址获取一级域名信息")
# url_simple_list = []
# for url_info in all_list:
#     file_list = url_info.split("://")
#     simple_url = ""
#     if len(file_list) == 2:
#         if file_list[1].find("/") > 0:
#             simple_url = file_list[0] + "://" + file_list[1].split("/")[0]
#         else:
#             simple_url = file_list[0] + "://" + file_list[1]
#     url_simple_list.append(simple_url)
# # print(len(url_simple_list))
# # print("4>>>>>>>>>>>>>>>网址去重")
# # # 利用字典的key唯一特性实现数据过滤
# url_dict = {}
# url_dict_2 = {}
# for url_info in url_simple_list:
#     url_dict[url_info] = url_info
#     if (url_dict_2.get(url_info, -1) == -1):
#         url_dict_2[url_info] = 1
#     else:
#         url_dict_2[url_info] = url_dict_2[url_info] + 1
# # print("5>>>>>>>>>>>>>>>网址过滤")
# filter_list = []
# with open(filter_path, "r", encoding='utf-8') as f:
#     filter_list = f.readlines()
#     f.close()
# filter_str = ""
# for str1 in filter_list:
#     filter_str += str1.replace('\n', '') + ","
# filter_str = filter_str.lower()
# # # 遍历过滤库 与简化后的地址实现过滤
# less_list = []
# for key in url_dict.keys():
#     flag = False
#     for tmp in key.split("."):
#         if filter_str.find(tmp) > 0:
#             flag = True
#             break
#     if not flag:
#         less_list.append(key)
# # print(len(less_list))
# with open(root_path + "\\A.txt", "w", encoding='utf-8') as f:
#     for response in less_list:
#         f.write(response + '\n')
#     f.close()
# count = 0
# # print(type(sorted(url_dict_2, reverse=True)))
# # 按照value排序
# url_dict_list = sorted(url_dict_2.items(),key = lambda x:x[1],reverse = True)
# # print(url_dict_2)
# with open(root_path + "\\B.txt", "w", encoding='utf-8') as f:
#     for url_tuple in url_dict_list:
#         # print(type(url_tuple))
#         if url_tuple[1] >= 2:
#             f.write(url_tuple[0] + "\t" + str(url_tuple[1]) + '\n')
#             count = count + 1
#     f.close()
# print("文件总数:" + str(len(all_file_list)))
# print("网址总数:" + str(len(all_list)))
# print("被过滤总数:" + str(count))
# print("去除重复后总数:" + str(len(less_list)))
# print("6>>>>>>>>>>>>>>>过滤文件保存begin")
# result_list = re.findall('[a-zA-Z]+', file_name)
# tmp_name = ""
# for result in result_list:
# 	if result == "xls" or result == "xlsx" or result == "txt":
# 		continue
# 	tmp_name += result + " "
# ctime = time.strftime("%Y%m%d%H%M%S")
# final_name = tmp_name + ctime
# with open(excel_path + "\\" + final_name + ".txt", "w", encoding='utf-8') as f:
# 	for response in less_list:
# 		f.write(response + '\n')
# 	f.close()
# print("6>>>>>>>>>>>>>>>过滤文件保存ok")
# print("文件总记录数:", len(all_list))
# print("文件过滤后记录数:", len(less_list))
# print("")
