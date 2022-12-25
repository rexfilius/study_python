"""
We define subsequence as any subset of an array.
We define a subarray as a contiguous subsequence in an array.
Given an array, find the maximum possible sum among:
1. all nonempty subarrays.
2. all nonempty subsequences.
Print the two values as space-separated integers on one line.
Note that empty subarrays/subsequences should not be considered.

EXAMPLE::
array = [-1,2,3,-4,5,10]
max sub-array sum = [2,3,-4,5,10] = 16
max sub-sequence sum = [2,3] and [5,10] = 20

array = [2, -1, 2, 3, 4, -5]
max sub-array sum = [2,-1,2,3,4] = 10
max sub-sequence sum = [2, 2, 3, 4] = 11

array = [-2, -3, -1, -4, -6]
max sub-array sum = = -1
max sub-sequence sum = = -1
"""


def maxSubArray(arr):
    currentSum = 0
    greatestSum = 0
    for number in arr:
        if currentSum + number < 0:
            currentSum = 0
        else:
            currentSum += number
        if currentSum > greatestSum:
            greatestSum = currentSum
    return greatestSum


def maxSubArray_2(arr):
    """Works, but not for all cases"""
    currentSum = 0
    subArraySum = 0
    subSequenceSum = 0
    for number in arr:
        if number > 0:
            subSequenceSum += number
        if currentSum + number < 0:
            currentSum = 0
        else:
            currentSum += number
        if currentSum > subArraySum:
            subArraySum = currentSum
    print(subArraySum, '', subSequenceSum)


def maxSubArray_3(arr):
    maxSA = arr[0]
    maxSS = arr[0]
    maxx = arr[0]
    for i in range(1, len(arr)):
        maxx = max(maxx + arr[i], arr[i])
        maxSA = max(maxSA, maxx)
        maxSS = max(max(maxSS, arr[i]), maxSS + arr[i])
    print(maxSA, '', maxSS)


def maxSubArray_4(arr):
    if all([x <= 0 for x in arr]):
        return max(arr), max(arr)
    max_suba = 0  # max subarray sum
    max_subs = sum([x for x in arr if x > 0])  # max subsequence sum
    s = 0
    for num in arr:
        s += num
        max_suba = max(max_suba, s)
        if s < 0:
            s = 0
    return max_suba, max_subs


a1 = [-1, 2, 3, -4, 5, 10]  # 16 20
a2 = [2, -1, 2, 3, 4, -5]  # 10 11
a3 = [-2, -3, -1, -4, -6]  # -1 -1
maxSubArray_3(a1)
