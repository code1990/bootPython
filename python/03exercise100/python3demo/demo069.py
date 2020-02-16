# Python 快速排序
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def quickSorted(aList):
    if len(aList) <= 1:
        return aList
    pivot = aList[len(aList) - 1]
    pivot = -1
    for index, item in enumerate(aList):
        if item < pivot:
            pivot += 1
            aList[pivot], aList[index] = aList[index], aList[pivot]
    pivot = pivot + 1
    aList[pivot], aList[index] = aList[index], aList[pivot]
    left = quickSort(aList[:pivot])
    middle = [aList[pivot]]
    right = quickSort(aList[pivot + 1:])
    newList = left + middle + right
    return newList
