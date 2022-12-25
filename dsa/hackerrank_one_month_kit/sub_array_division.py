"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares
has an integer on it. Lily decides to share a contiguous segment of the bar
selected such that:
1. The length of the segment matches Ron's birth month, and,
2. The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

EXAMPLE::
s = [2,2,1,3,2]
d = 4 (birth day)
m = 2 (birth month)
Lily wants to find segments summing to Ron's birth day, d = 4, with a length equalling
his birth month, m = 2. In this case, there are two segments meeting her criteria
output = [2,2] and [1,3]
@return int: the number of ways the bar can be divided i.e. the number of sub-arrays

CONSTRAINTS::
1 <= d <= 31
1 <= m <= 12


REPHRASE::
Given an array of integers, a firstInt, and a secondInt.
Get the sub-arrays where its length must be equal to secondInt,
and each of the sub-arrays sum must be equal to firstInt.
Return the number of the sub arrays.
input1 = [2,2,1,3,2] = array
         d = 4 = firstInt, sub-array sum
         m = 2 = secondInt, sub-array length
output1 = 2; [2,2] and [1,3]

input2 = [1,2,1,3,2]
         d = 3 = firstInt, sub-array sum
         m = 2 = secondInt, sub-array length
output2 = 2; [1,2] and [1,2]

input3 = [1,1,1,1,1,1]
         d = 3 = firstInt, sub-array sum
         m = 2 = secondInt, sub-array length
output3 = 0

input4 = [4]
         d = 4 = firstInt, sub-array sum
         m = 1 = secondInt, sub-array length
output4 = 1; [4]

ALGO::
parameters - array, firstInt(subArray-sum), secondInt(subArray-length)
variables - count
for index, number in enumerate(array):
    - if sum(array[index : m+index]) == firstInt, count++,
"""


def birthday(sArray, dInt, mInt):
    """
    sub-array-sum must be equal to dInt
    sub-array-length must be equal to mInt
    """
    if 1 > dInt > 31:
        return None
    if 1 > mInt > 12:
        return None
    count = 0
    for index, number in enumerate(sArray):
        if sum(sArray[index:mInt + index]) == dInt:
            count += 1
    return count


def subArrayDivision(array, subSum, subLength):
    count = 0
    for index, number in enumerate(array):
        if sum(array[index: subLength + index]) == subSum:
            count += 1
    return count


are = [1, 2, 3, 4, 5]
print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
