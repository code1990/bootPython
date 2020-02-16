# Python 复制列表
def clone_list(li1):
    li_copy=li1[:]
    return li_copy

li1=[1,2,3,4]
li2=clone_list(li1)
print(li1)
print(li2)