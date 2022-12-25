from dsa_courses.jayWengorw.sort.BubbleSort import bubbleSort
from dsa_courses.jayWengorw.sort.SelectionSort import selectionSort
from dsa_courses.jayWengorw.sort.InsertionSort import insertionSort
from dsa_courses.jayWengorw.sort.SortableArray import SortableArray
from dsa_courses.jayWengorw.sort.QuickSort import quickSort, quickSelect

array1 = [65, 55, 45, 35, 25, 15, 10]
array2 = [4, 2, 6, 3, 4, 6, 2, 1]
array3 = [0, 5, 2, 1, 6, 3]
print('array1:', array1)
print('array2:', array2)
print('array3:', array3, '\n')

print('bubble-sort:', bubbleSort(array1))
print('bubble-sort:', bubbleSort(array2))
print('bubble-sort:', bubbleSort(array3), '\n')

print('selection-sort', selectionSort(array1))
print('selection-sort', selectionSort(array2))
print('selection-sort', selectionSort(array3), '\n')

print('insertion-sort', insertionSort(array1))
print('insertion-sort', insertionSort(array2))
print('insertion-sort', insertionSort(array3), '\n')

print('quick-sort', quickSort(array1, 0, len(array1) - 1))
print('quick-sort', quickSort(array2, 0, len(array2) - 1))
print('quick-sort', quickSort(array3, 0, len(array3) - 1), '\n')

y1 = [0, 50, 20, 10, 60, 30]
print('array:', y1)
print('quick-sorted:', quickSort(y1, 0, len(y1) - 1))
print('lowest-value at index-1:', quickSelect(y1, 1, 0, len(y1) - 1), '\n')


# qSort = SortableArray(array3)
# qSort.quickSortMethod(0, len(array3) - 1)
# print(qSort.array)
