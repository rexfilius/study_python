"""
Write a function that finds the 'missing number' from an array of integers.
That is, the array is expected to have all integers from 0 up
to the array's length, but one is missing.
input1 = [5, 2, 4, 1, 0] = 0 to 5
output1 = 3
input2 = [9, 3, 2, 5, 6, 7, 1, 0, 4] = 0 to 9
output2 = 8
"""


def findMissingNumber(array):
    """
    array = [5,2,4,1,0]
    sort the array [0,1,2,4,5]
    numbers = 0 to len(array) = [0,1,2,3,4,5]
    loop through sorted array
    if numbers[i] != sortedArray[i] return numbers[i]
    """
    numbers = []
    for i in range(0, len(array) + 1):
        numbers.append(i)
    array.sort()
    for index, value in enumerate(array):
        if numbers[index] != value:
            return numbers[index]


def findMissingNumber2(collection):
    """
    If we presort the array, we can then expect each number to be at its own index.
    That is, the 0 should be at index 0, the 1 should be at index 1, and so on.
    We can then iterate through the array looking for a number that doesn't equal
    the index. Once we find it, we know that we just skipped over the missing number:
    """
    collection.sort()
    for index in range(len(collection)):
        if collection[index] != index:
            return index
    return None


n1 = [5, 2, 4, 1, 0]
n2 = [9, 3, 2, 5, 6, 7, 1, 0, 4]
print(findMissingNumber(n1))
print(findMissingNumber(n2))
print(findMissingNumber2(n1))
print(findMissingNumber2(n2))
print('--------------------')


# ANOTHER VARIANT OF findMissingNumber()
# Write a function that accepts an array of distinct integers from 0 up to N.
# However, the array will be missing one integer, return the missing one.
# input1 = [2, 3, 0, 6, 1, 5] = 0,1,2,3,4,5,6
# output1 = 4; missing integer
# input2 = [8, 2, 3, 9, 4, 7, 5, 0, 6] = 0,1,2,3,4,5,6,7,8,9
# output2 = 1; missing integer
def findMissingInteger(array):
    """O(N) Time"""
    fullSum = 0
    for num in range(1, len(array) + 1):
        fullSum += num
    actualSum = 0
    for n in array:
        actualSum += n
    # Difference between the two sums will be the missing number.
    return fullSum - actualSum


print(findMissingInteger([8, 2, 3, 9, 4, 7, 5, 0, 6]))
