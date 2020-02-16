# Python 判断元素是否在列表中存在
test_list = [1, 2, 3, 4, 5]
print("in")
for i in test_list:
    if (i == 4):
        print("exist")
print("not in")

if (4 in test_list):
    print("in")

from bisect import bisect_left

test_list_set = [1, 2, 3, 4, 5]
test_list_bisect = [1, 2, 3, 4, 5]

test_list_set = set(test_list_set)
if 4 in test_list_set:
    print("in")

test_list_bisect.sort()
if bisect_left(test_list_bisect, 4):
    print("in")
