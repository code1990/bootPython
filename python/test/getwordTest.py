from util.TxtUtil import TxtUtil
import re

mydict = {}
txt_path = r'C:\Users\admin\Desktop\tmp1.txt'
word_all =[]
counts = {}
for word in TxtUtil.readTxt(txt_path):
    array_word = word.split(' ')
    for s in array_word:
        if s.isnumeric() or re.search(r"\W", s) != None:
            continue
        else:
            word_all.append(s)
for s in word_all:
    counts[s] = counts.get(s, 0) + 1
            # print(s)
        # test_str = re.search(r"\W", s)
        # print(s)
        # print(test_str)
    # print(type(array_word))
print(counts)
# 6、将字典转换为列表
countsList = list(counts.items())

countsList.sort(key=lambda x: x[1], reverse=True)

# 8.输出TOP(20)
for i in range(len(countsList)):
    word, count = countsList[i]
    print(word,':',count)
    # print('{0:<20}{1:>10}'.format(word, count))
#     if i in mydict:
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
# for key, value in mydict.items():
#     print(key, value)
