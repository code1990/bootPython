import os
from util.TxtUtil import TxtUtil
# 使用脚本批量把md转docx
# 存在图片的md转换会出现异常 但是正常插入到doc当中
path = r'F:\github\mem\6月前\老吕逻辑要点精编'
desktop =r'C:\Users\admin\Desktop\md.txt'
files = os.listdir(path)
if not os.path.exists(path+"\\doc"):
	os.mkdir(path+"\\doc")
path_list=[]
for file_name in files:
	if file_name.find(".md")>0:
		docx_name = file_name.replace(".md", ".docx")
		cmd = 'pandoc '+path+'\\'+file_name+' -s -o '+path+'\\doc\\'+docx_name
		path_list.append(cmd)
		print(cmd)
TxtUtil.writeTxt(desktop,path_list)