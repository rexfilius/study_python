"""
Determine whether one array is a subset of another array
1. [b,d,f] is a subset of [a,b,c,d,e,f]
2. [b,d,f,h] is not a subset of [a,b,c,d,e,f]
"""


def isSubset(array1, array2):
    """Using nested loops. Time complexity is O(N*M)"""
    largerArray: list
    smallerArray: list
    if len(array1) > len(array2):
        largerArray, smallerArray = array1, array2
    else:
        largerArray, smallerArray = array2, array1

    for i in range(len(smallerArray)):
        foundMatch = False
        for j in range(len(largerArray)):
            if smallerArray[i] == largerArray[j]:
                foundMatch = True
                break
        if foundMatch is False:
            return False
    return True


def isSubset2(array1, array2):
    """Much more efficient than isSubset function
    Time complexity is O(N)"""
    largerArray: list
    smallerArray: list
    hashTable = {}
    if len(array1) > len(array2):
        largerArray, smallerArray = array1, array2
    else:
        largerArray, smallerArray = array2, array1

    for value in largerArray:
        hashTable[value] = True
    for value in smallerArray:
        if value not in hashTable.keys():
            return False
    return True  # this point, all in smallArray are contained in largerArray


y1 = ['a', 'b', 'c', 'd', 'e', 'f']
y2 = ['b', 'd', 'f']
y3 = ['b', 'd', 'f', 'h']

print(isSubset(y2, y1))
print(isSubset(y3, y1), '\n')

print(isSubset2(y2, y1))
print(isSubset2(y3, y1))

# mapp = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# print(5 not in mapp.keys())

