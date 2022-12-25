from dsa.notes.heap.HeapMin import HeapMin
from dsa.notes.heap.HeapMax import HeapMax


# HEAP-SORT
# create a min-heap
# add all array elements to the heap
# remove the root node in the min-heap and then add to the new array
# in that way, the array is sorted in ascending order
# -> for descending order, the process is reverse
def heapSortAscend(arr):
    minHeap = HeapMin()
    result = []
    for number in arr:
        minHeap.insert(number)
    for i in range(minHeap.size()):
        result.append(minHeap.remove())
    return result


def heapSortDescend(a):
    maxHeap = HeapMax()
    result = []
    for num in a:
        maxHeap.insert(num)
    for i in range(maxHeap.size()):
        result.append(maxHeap.remove())
    return result
