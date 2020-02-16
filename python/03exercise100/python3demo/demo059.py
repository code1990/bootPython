# Python 计算字典值之和

def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum


print(returnSum({"1": 100, "2": 200}))
