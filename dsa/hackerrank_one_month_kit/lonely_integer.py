"""
Given an array of integers, where all elements but one occur twice,
find the unique element.

input1 = [1,2,3,4,3,2,1]
output1 = 4; occurs once


ALGO::
for int in array:
    - if hashTable.get(int); hashTable[int] +=1
    - else hashTable[int] = 1
for key, value in hashTable.items()
    - if value == 1, return key
"""


def lonelyInteger(array):
    hashTable = {}
    for integer in array:
        if hashTable.get(integer):
            hashTable[integer] += 1
        else:
            hashTable[integer] = 1
    for key, value in hashTable.items():
        if value == 1:
            return key


print(lonelyInteger([1, 2, 3, 4, 3, 2, 1]))
