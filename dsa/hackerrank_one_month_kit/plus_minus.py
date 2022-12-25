"""
Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with
places after the decimal.

input=[1,1,0,-1,-1]
output = 2-positive = 2/5 = 0.400000
         2-negative = 2/5 = 0.400000
         1-zero = 1/5 = 0.200000

input2 = -4 3 -9 0 4 1
output2 = 3-positive = 3/6 = 0.500000
          2-negative = 2/6 = 0.333333
          1-zero = 1/6 = 0.166667

ALGO::
get the length of array
variables- posCount, negCount, zeroCount
loop through array:
    - if number is postive, >0, posCount+=1
    - if number is negative, <0, negCount+=1
    - if number equal to 0, zeroCount +=1
posCountRatio = posCount / array.length
negCountRatio = negCount / array.length
zeroCountRatio = zeroCount / array.length
"""


def plusMinus(array):
    arrayLength = len(array)
    positiveCount, negativeCount, zeroCount = 0, 0, 0
    for number in array:
        if number > 0:
            positiveCount += 1
        elif number < 0:
            negativeCount += 1
        elif number == 0:
            zeroCount += 1
    posCountRatio = positiveCount / arrayLength
    negCountRatio = negativeCount / arrayLength
    zeroCountRatio = zeroCount / arrayLength
    print('{:.6f}'.format(posCountRatio))
    print('{:.6f}'.format(negCountRatio))
    print('{:.6f}'.format(zeroCountRatio))


plusMinus([1, 1, 0, -1, -1])
