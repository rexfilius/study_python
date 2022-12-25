"""
Write a function that accepts an array of numbers and returns the largest sum
that could be computed from any "contiguous-subsection" of the array.
Assume the array contains at least one positive number.

input1 = [3, -4, 4, -3, 5, -9]
output1 = 6 -> [4, -3, 5]
"""


def maxSumInArray(array):
    """O(N) Time and O(1) Space.
    Greedy algorithm approach"""
    currentSum = 0
    greatestSum = 0
    for number in array:
        if currentSum + number < 0:
            currentSum = 0
        else:
            currentSum += number
        if currentSum > greatestSum:
            greatestSum = currentSum
    return greatestSum


p1 = [3, -4, 4, -3, 5, -9]
print(maxSumInArray(p1))  # answer is 6; [4,-3,5]

p2 = [1, 1, 0, -3, 5]
print(maxSumInArray(p2))  # answer is 5; [5]

p3 = [5, -2, 3, -8, 4]
print(maxSumInArray(p3))  # answer is 6; [5,-2,3]

p4 = [2, -3, 1, 2, -1]
print(maxSumInArray(p4))  # answer is 3; [1,2]

p5 = [5, -8, 2, 1, 0]
print(maxSumInArray(p5))  # answer is 5; [5]

print(maxSumInArray([-1, 2, 3, -4, 5, 10]))  # answer is 16; [2,3,-4,5,10]

print(maxSumInArray([2, -1, 2, 3, 4, -5]))  # answer is 10; [2,-1,2,3,4]
