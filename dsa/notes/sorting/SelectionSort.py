# Implementation of Selection Sort.
# Time complexity is O(N^2).
def selectionSort(arr):
    if len(arr) == 1:
        return arr
    for i in range(len(arr)):
        lowestNumIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowestNumIndex]:
                lowestNumIndex = j
        if lowestNumIndex != i:
            arr[i], arr[lowestNumIndex] = arr[lowestNumIndex], arr[i]
    return arr
