import os
import time

# 定义根目录
root_dir = r'F:\spider'
# 定义关键字结果目录
rs_dir = r'F:\spider\result'
# 每1000条写入一个文件
file_size = 1000
# 合并文件夹的目录
mg_dir = root_dir + "\\merge"
if not os.path.exists(mg_dir):
	os.makedirs(mg_dir)
print(">>>>>0.删除过滤文件")
for file_name in os.listdir(mg_dir):
	file_path = mg_dir + "\\" + file_name
	os.remove(file_path)
print(">>>>>1.读取过滤后的文件内容")
# 列出指定目录下的所有文件
kw_list = []
for file_name in os.listdir(rs_dir):
	file_path = rs_dir + "\\" + file_name
	# 依次打开目录下的所有xls或者xlsx文件
	if file_path.find(".txt") > 0:
		# kw_ok_list.append(file_path)
		f = open(file_path, "r", encoding='utf-8', errors='ignore')
		kw_list.extend(f.readlines())
print(">>>>>2.过滤重复开始")

# 利用字典的key唯一特性实现数据过滤
url_dict = {}
for kw in kw_list:
	url_dict[kw] = kw
less_list = []
all_list = []
for key in url_dict.keys():
	all_list.append(key)
if len(all_list) < file_size:
	ctime = time.strftime("%Y%m%d%H%M%S")
	path = mg_dir + "\\" + ctime + '.txt'
	with open(path, "w", encoding='utf-8') as f:
		for response in all_list:
			f.write(response)
		f.close()
else:
	file_list = []
	for index in range(len(all_list)):
		key = all_list[index]
		if index == len(all_list) - 1:
			file_list.append(key)
			ctime = time.strftime("%Y%m%d%H%M%S")
			path = mg_dir + "\\" + ctime + '.txt'
			with open(path, "w", encoding='utf-8') as f:
				for response in file_list:
					f.write(response)
				f.close()
		else:
			if (index + 1) % file_size == 0:
				ctime = time.strftime("%Y%m%d%H%M%S")
				path = mg_dir + "\\" + ctime + '.txt'
				with open(path, "w", encoding='utf-8') as f:
					for response in file_list:
						f.write(response + '\n')
					f.close()
				file_list = []
			else:
				file_list.append(key)
