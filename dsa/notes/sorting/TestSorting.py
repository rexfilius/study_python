from dsa_notes.dsa.sorting.BubbleSort import bubbleSort
from dsa_notes.dsa.sorting.InsertionSort import insertionSort
from dsa_notes.dsa.sorting.SelectionSort import selectionSort
from dsa_notes.dsa.sorting.HeapSort import heapSortAscend, heapSortDescend

array1 = [65, 55, 45, 35, 25, 15, 10]
array2 = [4, 2, 6, 3, 4, 6, 2, 1]
array3 = [0, 5, 2, 1, 6, 3]
array4 = [4, 5, 8, 9, 1, 6, 7, 3, 2]
print('array1:', array1)
print('array2:', array2)
print('array3:', array3)
print('array4:', array4, '\n')

print('bubble-sort:', bubbleSort(array1))
print('bubble-sort:', bubbleSort(array2))
print('bubble-sort:', bubbleSort(array3))
print('bubble-sort:', bubbleSort(array4), '\n')

print('insertion-sort:', insertionSort(array1))
print('insertion-sort:', insertionSort(array2))
print('insertion-sort:', insertionSort(array3))
print('insertion-sort:', insertionSort(array4), '\n')

print('selection-sort:', selectionSort(array1))
print('selection-sort:', selectionSort(array2))
print('selection-sort:', selectionSort(array3))
print('selection-sort:', selectionSort(array4), '\n')

# print('heap-sort-ascend:', heapSortAscend(array1))
# print('heap-sort-ascend:', heapSortAscend(array2))
# print('heap-sort-ascend:', heapSortAscend(array3))
# print('heap-sort-ascend:', heapSortAscend(array4), '\n')
#
# print('heap-sort-descend:', heapSortDescend(array1))
# print('heap-sort-descend:', heapSortDescend(array2))
# print('heap-sort-descend:', heapSortDescend(array3))
# print('heap-sort-descend:', heapSortDescend(array4), '\n')
