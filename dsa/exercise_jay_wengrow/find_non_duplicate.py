"""
Write a function that returns the first non-duplicated character in a string.
e.g. the string, "minimum" has two characters that only exist once — "n" & "u",
so your function should return the "n", since it occurs first.
"""


def findFirstNonDuplicate(string):
    hashTable = {}
    for char in string:
        if char in hashTable.keys():
            hashTable[char] += 1
        else:
            hashTable[char] = 1
    print(hashTable)
    for element in string:
        if hashTable[element] == 1:
            return element


def findNonDuplicate(collection):
    hashTable = {}
    duplicates = []
    for value in collection:
        if value in hashTable.keys():
            hashTable[value] += 1
        else:
            hashTable[value] = 1
    for element in collection:
        if hashTable[element] == 1:
            duplicates.append(element)
    return duplicates


print(findFirstNonDuplicate('minimum'))  # answer = n
print(findNonDuplicate('minimum'))  # answer = n,u
