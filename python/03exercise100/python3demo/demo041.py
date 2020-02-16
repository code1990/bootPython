# Python 将列表中的指定位置的两个元素对调
def swapPositions1(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos1],list[pos2]
    return list
def swapPositions2(list,pos1,pos2):
    first_ele=list.pop(pos1)
    second_ele=list.pop(pos2)

    list.insert(pos1,second_ele)
    list.insert(pos2,first_ele)
    return list

def swapPositions3(list,pos1,pos2):
    get=list[pos1],list[pos2]
    list[pos2],list[pos1]=get
    return list
def reversal(list,n1,n2):
    temp=list[n1]
    list[n1]=list[n2]
    list[n2]=temp
    print(list)


List=[1,2,3,4]
pos1=1
pos2=3
print(swapPositions1(List,pos1-1,pos2-2))
print(swapPositions2(List,pos1-1,pos2-2))
print(swapPositions3(List,pos1-1,pos2-2))
print(reversal(List,pos1-1,pos2-2))

