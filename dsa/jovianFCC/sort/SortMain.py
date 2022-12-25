import time
import random
from algoFreeCodeCamp.courseJovian.sort.Sort import bubbleSort, insertSort
from algoFreeCodeCamp.courseJovian.sort.Sort2 import mergeSort, mergeSortCheck
from algoFreeCodeCamp.courseJovian.sort.Sort3 import quickSort

n1 = [4, 2, 6, 3, 4, 6, 2, 1]  # sorted = [1, 2, 2, 3, 4, 4, 6, 6]
n2 = [1, 5, 6, 2, 0, 11, 3]

print('bubble sort', bubbleSort(n1))
print('insert sort', insertSort(n1))
print('merge sort', mergeSort(n1))
print('quick sort', quickSort(n1))
# print()
# print('', mergeSortCheck(numList))

# TESTING SORTING WITH A LARGE LIST
# item = range(10000)
# bigList = random.sample(item, k=len(item))
# print('list', bigList)
# startTime = time.time()
# print('sort', mergeSort(bigList))
# print("--- %s seconds ---" % (time.time() - startTime))
