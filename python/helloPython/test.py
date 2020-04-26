file_name = "https://www.etsy.com/market/wood_rasps"
file_list = file_name.split("://")
print(len(file_list))
print(file_list[0] + "://" + file_list[1].split("/")[0])

# 使用普通列表过滤
# def filterForLi(li):
#     info = ">>>>>使用普通过滤列表<<<<<"
#     # print(info)
#     out_data = [element for element in li if element not in() isinstance(element,int)] #int类型没有长度，所以需要首先排除
#     print(out_data)


# 定义一个列表
li = [1, 1, 2, 2, 3, 3, 4, 5, 4, 5, "apple", "banana", "orange", "apple", "banana", "orange", "juice"]
# 分别调用两个函数:结果应该一样才准确
# 普通过滤
# filterForLi(li)
simple_url_str = ""
dict1 = {}
for index in range(len(li)):
    url = li[index]
    dict1[url] = url
#     if simple_url_str == "":
#         simple_url_str = str(url) + ","
#     else:
#         if simple_url_str.find()
#             simple_url_str += str(url) + ","
#     if url in
# print(simple_url_str)
# for index in range(len(li)):
#     if simple_url_str
for key in dict1.keys():
    print(key)
with open(r"F:\Crawl website\过滤.txt", "r", encoding='utf-8') as f:
    data = f.readline()
    print(data)
import time

print(time.time())
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime("YYYYMMDD HH:mm:ss (%Y%m%d %H:%M:%S)"))
print(time.strftime("%Y%m%d%H%M%S"))
less_list = []
url_dict = {"1": "1", "2": "2", "3": "3"}
filter_list = [1, 2, 4]
for i in filter_list:
    print(i)
for key in url_dict.keys():
    for index in range(len(filter_list)):
        filter_info = filter_list[index]
        if key.find(str(filter_info)) < 0:
            break
        else:
            less_list.append(key)
print(less_list)
print("https://www.senga-eng.com/".count("."))
import re

file_name = "2020-4-18-19-33-23-37197186839351-bent bolts - Yahoo Search Resu-采集的数据-后羿采集器"
result_list = re.findall('[a-zA-Z0-9]+', file_name)
result_list = re.findall('[a-zA-Z]+', file_name)
print(result_list)
# for c in file_name.split("-"):
#     if c.isalpha():
#         print(c)

filter_list = []
with open(r'F:\Crawl website\过滤.txt', "r", encoding='utf-8') as f:
    filter_list = f.readlines()
filter_str = ""
for str in filter_list:
    filter_str += str.replace('\n', '') + ","
print(filter_str)
