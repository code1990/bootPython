# Python 二分查找

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


def BinarySearch(sortedList):
    num = int(input("num"))
    counter = 0
    mid = 0

    if num in [sortedList[0], sortedList[len(sortedList) - 1]]:
        print("some")
    else:
        while True:
            mid = len(sortedList)
            if sortedList[mid] == num:
                print("")
                break
            elif sortedList[mid] > num:
                sortedList = sortedList[:(mid + 1)]
            else:
                sortedList = sortedList[mid:]
            print(sortedList, mid)

            counter += 1
            if counter > 1:
                print(counter)
                break


def bin_search(data_list, val):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == val:
            return mid
        elif data_list[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return


arr = [2, 3, 4, 10]
x = 10
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(result)
else:
    print("不再数字组中")
