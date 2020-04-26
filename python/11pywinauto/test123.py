user_page = 373
for i in range(user_page):
    print(i+1)
    break
kw_path = 'C:\\Users\\admin\\Desktop\\searchkw.txt'
f2 = open(kw_path,"r")
lines = f2.readlines()
print(type(lines))
for index in range(len(lines)):
    print(lines[index], end='')
# f = open("./image/abc.txt")
# for line2 in open("./image/abc.txt"):
#     print
#     line2