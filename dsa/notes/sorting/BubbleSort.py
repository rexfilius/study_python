# Implementation of bubble sort algorithm
# Time complexity is O(N^2) - Quadratic Time
def bubbleSort(arr):
    if len(arr) == 1:
        return arr
    lastIndex = len(arr) - 1
    _sorted = False
    while not _sorted:
        _sorted = True
        for index in range(lastIndex):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                _sorted = False
        lastIndex -= 1
    return arr
