"""
There is a collection of input strings and a collection of query strings. For each
query string, determine how many times it occurs in the list of input strings.
Return an array of the results.

Case 1
strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc]
-> 2 instances of 'ab', 1 of 'abc', 0 of 'bc'
output = [2,1,0]

ALGO::
Convert strings to map, map-key = string value, map-value = number of occurence
for value in strings
    - if hashTable.get(value), hashTable[value] +=1
    - else hashTable[value] = 1
for value in queries
    - if hashTable.get(value), array.append(hashTable[value])
    - else array.append(0)
"""


def matchingStrings(strings, queries):
    result = []  # an array of the number of each query in strings
    hashTable = {}
    for value in strings:
        if hashTable.get(value):
            hashTable[value] += 1
        else:
            hashTable[value] = 1
    for value in queries:
        if hashTable.get(value):
            result.append(hashTable[value])
        else:
            result.append(0)
    return result


print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))  # [2,1,0]
print(matchingStrings(['def', 'de', 'fgh'], ['de', 'lmn', 'fgh']))  # [1,0,1]
