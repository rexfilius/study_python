"""
You have an array containing several values, reorder the data
so that the same values are grouped together(in any order).

input1 = ["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]
ouput = ["c", "c", "c", "a", "a", "a", "d", "d", "d", "b", "b", "b"]
        OR ["d", "d", "d", "c", "c", "c", "a", "a", "a", "b", "b", "b"]
        OR ["b", "b", "b", "c", "c", "c", "a", "a", "a", "d", "d", "d"]

Any classic sorting algorithm would solve this, but we can go a different way.
"""


def groupArraySort(array):
    """
    This algorithm takes just O(N) time, which is a significant optimization
    over the O(N log N) that sorting would have taken.
    """
    hashTable = {}
    newArray = []
    for value in array:
        if hashTable.get(value):
            hashTable[value] += 1
        else:
            hashTable[value] = 1
    for value, count in hashTable.items():
        for _ in range(count):
            newArray.append(value)
    return newArray


c4 = ["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]
print(groupArraySort(c4))
