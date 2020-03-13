import pandas as pd
# list=[" ","https://www.mcmaster.com/fasteners","https://www.homedepot.com/b/Hardware-Fasteners/N-5yc1vZc255"]
urlList=[]
excelname="C:\\Users\\Administrator\\Desktop\\fasteners_link.xlsx"
df = pd.read_excel(excelname)
for value in df.values:
    print(value[1])
    if(isinstance(value[1],str)):
        urlList.append(value[1])
    # print(type(value[1]))
    # for row in value:
    #     print(type(row))
    # break
filename=excelname.replace("xlsx","txt")
# print(filename)
def getSimpleUrl(str):
    print("111111111",str)
    index = str.rindex("/")
    str = str[0:index]
    # print(str)
    if str.count(".") == 2 or str.count(".") == 1:
        return str
    index = str.rindex(".")
    head = str[0:index]
    end = str[index + 1:len(str)]
    index = end.index("/")
    end = end[0:index]
    return head+"."+end
responses=[]
for value in urlList:
    value=value.strip()
    if(value!="" and len(value.split("."))==3):
        value = getSimpleUrl(value)
        # value = getSimpleUrl(value)
        responses.append(value)
responses=list(set(responses))
with open(filename, 'a') as f:
    for response in responses:
        f.write(response + '\n')
print("文件写入结束")