"""
Write a function that accepts two arrays of integers; then finds one number from
each array that can be swapped to cause the two array sums to be equal.
The function won't perform the swap, but will return the two indexes that
would be swapped.

array1 = [5,3,2,9,1] = sum is 20
array2 = [1,12,5] = sum is 18
=> swap 2 from array1 and 1 from array2
array1 = [5,3,1,9,1] = sum is 19
array2 = [2,12,5] = sum is 19
"""


def sumSwap(array1, array2):
    hashTable = {}
    sum1 = 0
    sum2 = 0
    for index, number in enumerate(array1):
        sum1 += number
        hashTable[number] = index
    for num in array2:
        sum2 += num
    shiftAmount = (sum1 - sum2) // 2
    for i, num in enumerate(array2):
        if (num + shiftAmount) in hashTable.keys():
            return [hashTable[num + shiftAmount], i]
    return None


r1 = [5, 3, 2, 9, 1]  # sum1 = 20
r2 = [1, 12, 5]  # sum2 = 18 ... shiftAmount = 1
print(sumSwap(r1, r2), '\n')  # answer = [2,0] indexes to be swapped

r3 = [5, 3, 3, 7]
r4 = [4, 1, 1, 6]
print(sumSwap(r3, r4), '\n')  # answer = [3,0] indexes to be swapped

r5 = [1, 2, 3, 4, 5]
r6 = [6, 7, 8]
print(sumSwap(r5, r6), '\n')  # answer = [2,0] indexes to be swapped

r7 = [10, 15, 20]
r8 = [5, 30]
print(sumSwap(r7, r8), '\n')  # answer = [0,0] indexes to be swapped
