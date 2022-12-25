"""
Write a function that returns the intersection of two arrays. The intersection
is a third array that contains all values contained within the first two arrays.
For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
input1 = [1,2,3,4,5]
input2 = [0,2,4,6,8]
output = [2,4], a new array
"""
from time import time


def findIntersection(array1, array2):
    result = []
    for value in array1:
        for element in array2:
            if value == element:
                result.append(element)
                break
    return result


def findIntersection2(array1, array2):
    """this is O(N), I guess, better than findIntersection()"""
    result = []
    hashTable = {}
    for value in array1:
        hashTable[value] = True
    for element in array2:
        if element in hashTable.keys():
            result.append(element)
    return result


# input1 = [1, 2, 3, 4, 5]
# input2 = [0, 2, 4, 6, 8]
# print(findIntersection(input2, input1))
# print(findIntersection2(input2, input1), '\n')

# biglist1 = [x for x in range(1, 10001)]
# biglist2 = [x for x in range(1, 10001, 3)]
# print(findIntersection(biglist1, biglist2))
# print(findIntersection2(biglist1, biglist2), '\n')
