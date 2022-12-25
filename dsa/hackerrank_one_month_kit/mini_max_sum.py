"""
Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers. Then print the respective
minimum and maximum values as a single line of two space-separated long integers.

input1 = [1,3,5,7,9]
output1 = min-sum = 1+3+5+7 = 16
          max-sum = 3+5+7+9 = 24

input2 = [1,2,3,4,5]
output2 = min is 10, max is 14
explain: 1+2+3+4 = 10
         1+2+3+5 = 11
         1+2+4+5 = 12
         1+3+4+5 = 13
         2+3+4+5 = 14

input3 = [3,4,5,6,7]
output3 = min is 18, max is 22
explain: 3+4+5+6 = 18
         3+4+5+7 = 19
         3+4+6+7 = 20
         3+5+6+7 = 21
         4+5+6+7 = 22

ALGO::
sort the array in ascending order
minValue = array[0]+array[1]+array[2]+array[3]
maxValue = array[1]+array[2]+array[3]+array[4]
"""


def miniMaxSum(array):
    array.sort()
    minValue = array[0] + array[1] + array[2] + array[3]
    maxValue = array[1] + array[2] + array[3] + array[4]
    print(minValue, maxValue)


miniMaxSum([3, 4, 5, 6, 7])
