str="https://www.buckleguy.com/brass-snap-fasteners"
# array= str.split(".")
# index = str.rindex(".")
# head = str[0:index]
# end = str[index+1:len(str)]
# index = end.index("/")
# end=end[0:index]
# # print(str[0:index])
# print(head+"."+end)

def getSimpleUrl(str):
    index = str.rindex("/")
    str = str[0:index]
    print(str)
    if str.count(".")==2 or str.count(".")==1:
        return str
    index = str.rindex(".")
    head = str[0:index]
    end = str[index + 1:len(str)]
    index = end.index("/")
    end = end[0:index]
    return head+"."+end


print(getSimpleUrl(str))