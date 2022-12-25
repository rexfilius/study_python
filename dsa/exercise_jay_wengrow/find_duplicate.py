"""
Write a function that accepts an array of strings and returns the first duplicate
value it finds. e.g. if the array is [a, b, c, d, c, e, f], the function should
return "c", since it’s duplicated within the array.
(You can assume that there's one pair of duplicates within the array)
"""


def findFirstDuplicate(collection):
    for i in range(len(collection)):
        for j in range(i + 1, len(collection)):
            if collection[i] == collection[j]:
                return collection[i]


def findFirstDuplicate2(collection):
    """O(N) time, better than findFirstDuplicate()"""
    hashTable = {}
    for value in collection:
        if value in hashTable.keys():
            return value
        else:
            hashTable[value] = True


def findDuplicates(collection):
    hashTable = {}
    duplicates = set()
    for value in collection:
        if value in hashTable.keys():
            hashTable[value] += 1
        else:
            hashTable[value] = 1
    for value in collection:
        if hashTable[value] == 2:
            duplicates.add(value)
    return duplicates


a1 = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
print(findFirstDuplicate(a1))
print(findFirstDuplicate2(a1))
print(findDuplicates(a1))
