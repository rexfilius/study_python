def partition(collection, leftPointer, rightPointer):
    pivotIndex = rightPointer
    pivot = collection[pivotIndex]
    rightPointer -= 1
    while True:
        while collection[leftPointer] < pivot:
            leftPointer += 1
        while collection[rightPointer] > pivot:
            rightPointer -= 1
        if leftPointer >= rightPointer:
            break
        else:
            collection[leftPointer], collection[rightPointer] = \
                collection[rightPointer], collection[leftPointer]
            leftPointer += 1
    collection[leftPointer], collection[pivotIndex] = \
        collection[pivotIndex], collection[leftPointer]
    return leftPointer


def quickSort(collection, leftIndex, rightIndex):
    """O(NlogN) time"""
    if rightIndex - leftIndex <= 0:
        return
    pivotIndex = partition(collection, leftIndex, rightIndex)
    quickSort(collection, leftIndex, pivotIndex - 1)
    quickSort(collection, pivotIndex + 1, rightIndex)
    return collection


"""
QUICK-SELECT::
Say you have an array in random order, and you don't need to sort it, but you 
do want to know the 10th-lowest value in the array, or the 5th-highest. 
This can be useful if we had a lot of test grades and want to know what the 
25th percentile was, or if we want to find the median grade.

One way to solve this would be to sort the entire array and then jump to the
appropriate index. A better way is QuickSelect - hybrid of QuickSort & BinarySearch.

One of the beautiful things about Quickselect is that we can find the correct 
value without having to sort the entire array.

With Quicksort, each time we half the array, we need to repartition every single
element again (in their subarray form), giving us O(N log N). 
With Quickselect, on the other hand, each time we cut the array in half, we only
have to partition the one half we cared about - the half in which we know our
value is to be found.
"""


def quickSelect(collection, kth_index, leftIdx, rightIdx):
    """Returns the value at the kth_index without having to
    sort the whole array. O(N) time"""
    if rightIdx - leftIdx <= 0:
        return collection[leftIdx]
    pivotIdx = partition(collection, leftIdx, rightIdx)

    if kth_index < pivotIdx:
        return quickSelect(collection, kth_index, leftIdx, pivotIdx - 1)
    elif kth_index > pivotIdx:
        return quickSelect(collection, kth_index, pivotIdx + 1, rightIdx)
    else:
        return collection[pivotIdx]  # kLowestValue == pivotIdx
