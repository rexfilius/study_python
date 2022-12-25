"""
Watson gives Sherlock an array of integers. His challenge is to find an element of
the array such that the sum of all elements to the left is equal to the sum of
all elements to the right.
You will be given arrays of integers and must determine whether there is an element
that meets the criterion. If there is, return YES. Otherwise, return NO.

EXAMPLE::
array = [5,6,8,11]
output = YES => 8 at index 2 => sum at left of 8 equals sum at right of 8

array = [1]
output = YES => 1 at index 0 => sum at left and right equals 0

array = [1,2,3]
output = NO => no element satisfies the criteria

array = [1,2,3,3]
output = YES => 3 at index 2 => sum at left and right of index 2 equals 3

array = [1,1,4,1,1]
output = YES => 4 at index 2 => sum at left anf right equals to 2

array = [2,0,0,0]
output = YES => 2 at index 0

array = [0,0,2,0]
output = YES => 2 at index 2

ALGO::
if len(array) == 1; return YES
for i in range(len(array)):
    - if i == 0 and sum(array[i+1:]) == 0; return YES
    - if sum(array[:i]) == sum(array[i+1:]); return YES
return NO
"""


def balancedSums(array):
    """DOES NOT WORK WELL WITH LARGE ARRAY"""
    if len(array) == 0:
        return 'NO'
    if len(array) == 1:
        return 'YES'
    for index in range(len(array)):
        sumAfter = sum(array[index + 1:])
        sumBefore = sum(array[:index])
        if index == 0 and sumAfter == 0:
            return 'YES'
        if sumBefore == sumAfter:
            return 'YES'
    return 'NO'


def balancedSums_2(array):
    """WORKS WELL WITH LARGE ARRAY"""
    left = 0
    right = sum(array)
    for item in array:
        right -= item
        if left == right:
            return "YES"
        left += item
    return "NO"


array1 = [5, 6, 8, 11]  # YES
array2 = [1]  # YES
array3 = [1, 2, 3]  # NO
array4 = [1, 2, 3, 3]  # YES
array5 = [1, 1, 4, 1, 1]  # YES
array6 = [2, 0, 0, 0]  # YES
array7 = [0, 0, 2, 0]  # YES

print(balancedSums(array7))
