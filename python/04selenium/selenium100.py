from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
# import time
# import xlrd
import os
import time
import re
import xlwt

# 定义根目录
root_dir = r'F:\spider'
# 定义关键字目录
kw_dir = r'F:\spider\kw'
# 定义关键字结果目录
rs_dir = r'F:\spider\result'
# 定义过滤文件路径
filter_path = 'F:\\spider\\过滤.txt'
# 定义最大的点击次数
page_size = 50
# 定义浏览器的安装路径
br_path = r'F:\soft\chrome-win32\chrome.exe'
# 定义浏览器的驱动位置
dr_path = r'C:\driver\chromedriver68.exe'

print(">>>>>1.浏览器参数配置")
options = Options()
# 添加随机的浏览器UserAgent
# ua = UserAgent()
# options.add_argument('user-agent=' + ua.random)
# 指定浏览器的安装路径
options.binary_location = br_path
# 设置浏览器的驱动
driver = webdriver.Chrome(chrome_options=options, executable_path=dr_path)

print(">>>>>2.读取搜索关键字")
# 列出指定目录下的所有文件
kw_ok_list = []
for file_name in os.listdir(kw_dir):
	file_path = kw_dir + "\\" + file_name
	# 依次打开目录下的所有xls或者xlsx文件
	if file_path.find(".txt") > 0:
		kw_ok_list.append(file_path)
f = open(kw_ok_list[0], "r", encoding='utf-8', errors='ignore')
kw_list = f.readlines()
print(kw_list)
main_url = 'https://duckduckgo.com/?q=' + kw_list[0]
driver.get(main_url + kw_list[0])
click_size = 1
while True:
	all_html = driver.page_source
	js = "window.scrollTo(0, 1000000);"
	driver.execute_script(js)
	click_id = 'rld-' + str(click_size)
	print(click_size)
	if all_html.find(str(click_id)) > 0 and click_size < 50:
		driver.find_element_by_id(click_id).find_element_by_tag_name('a').click()
		time.sleep(3)
		click_size = click_size + 1
	else:
		list_h2 = driver.find_elements_by_tag_name('h2')
		all_list = []
		path = rs_dir + "\\" + kw_list[0].replace(' &ia=web\n', '') + '.txt'
		for element in list_h2:
			a_html = element.get_attribute('innerHTML')
			if a_html.find('result__a') > 0:
				result = element.find_element_by_class_name('result__a').get_attribute('href')
				print(result)
				all_list.append(result)
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
		ctime = time.strftime("%Y%m%d%H%M%S")
		final_name = tmp_name + ctime
		with open(rs_dir + "\\" + final_name + ".txt", "w", encoding='utf-8') as f:
			for response in less_list:
				f.write(response + '\n')
			f.close()
		print("6>>>>>>>>>>>>>>>过滤文件保存ok")
		print("文件总记录数:", len(all_list))
		print("文件过滤后记录数:", len(less_list))
		print("")
		break

driver.quit()
