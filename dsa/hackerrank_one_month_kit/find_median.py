"""
The median of a list of numbers is essentially its middle element after sorting.
The same number of elements occur after it as before
Given a list of numbers with an odd number of elements, find the median

input1 = [5,3,1,2,4]
sorted = [1,2,3,4,5]
output1 = 3; median

input2 = [0,1,2,4,6,5,3]
sorted = [0,1,2,3,4,5,6]
output2 = 3; median

ALGO::
parameter = array of integers
sort the array
medianINdex = arraylength / 2
median = array[medianIndex]
@return median
"""


def findMedian(arr):
    arr.sort()
    medianIndex = len(arr) // 2
    return arr[medianIndex]
