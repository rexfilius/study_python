# Implementation of Insertion Sort.
# Time complexity is O(N^2).
def insertionSort(arr):
    if len(arr) == 1:
        return arr
    for index in range(1, len(arr)):
        tempValue = arr[index]
        position = index - 1
        while position >= 0:
            if arr[position] > tempValue:
                arr[position + 1] = arr[position]
                position -= 1
            else:
                break
        arr[position + 1] = tempValue
    return arr
