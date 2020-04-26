import xlrd
import os

path = 'F:\\Crawl website'
dir = os.listdir(path) # 列出指定目录下的所有文件
# print('-----------------当前目录下的所有文件如下-----------------')
print(dir)
name = [] # 存放修改后的文件名的列表
excel_path = 'F:/Crawl website/'  # 指定打开excel的目录，特别是和上面的path区别，多了一个斜杠，表示在这个目录下
old_name = []


for i in range(len(dir)):
    count = 0
    x = dir[i]
    old_name.append(x)
    for m in range(len(old_name)):
        x = old_name[m].split('-')
        # print(x)
        x1 = x[7] + x[8] + x[0] + x[1] +x[2] # 取出关键词+搜索引擎+日期组成名称
    name.append(x1) # 列表追加
# print(name)
    print('开始读取第'+str(dir[i])+'个文件数据')
    bk = xlrd.open_workbook(excel_path+dir[i]) # 依次打开目录下的所有文件
    # print(bk)
    sheet = bk.sheet_by_index(0)
    urllist = []
    for j in range(1,sheet.nrows):
        # print(sheet.cell_value(j,1))
        # with open (r'C:\Users\Administrator\Desktop\过滤.txt')as f:
        #     fs = f.readlines()
        #     b = [n[:-1] for n in fs]
        web1 = sheet.cell_value(j,1)
        # print(web1)
        # for c in b:
        #     if c not in web1:
        web = web1.split('/') #以斜杠作为分隔符，分割出网址
         # print(web)
        if len(web) < 3:
            continue
        else:
            website = web[0] + '//' + web[1] + web[2]  # 取协议和一级域名
            # print(website)
            urllist.append(website)
    newlist = []
    for m in urllist:
        if m not in newlist:
            newlist.append(m)
    list1 = []
    count = 0
    for index in range(len(newlist)):
        file = open(excel_path + str(name[i]) + '.txt', 'a+',encoding='utf-8')  # 创建一个以关键词和搜索引擎加时间组成名称的文本文件，并以追加的形式打开
        file.write(newlist[index] + '\n')  # 写入一行换行
        count += 1
    print('--------------当前文件有数据总数: ', str(sheet.nrows)+'\n','-----------'+excel_path + str(name[i]) + '.txt'+'共写入'+str(count)+' 行数据-----')
    file.close()
