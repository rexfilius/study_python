"""
Another sorting method, the counting sort, does not require comparison. Instead,
you create an integer array whose index range covers the entire range of values
in your array to sort. Each time a value occurs in the original array, you increment
the counter at that index. At the end, run through your counting array,
printing the value of each non-zero valued index that number of times.

NOTE
For this exercise, always return a frequency array with 100 elements.

CHALLENGE
Given a list of integers, count and return the number of times each value appears
as an array of integers.

ALGO:: FAILED
variables - hashTable, array
for number in integers:
    - if hashTable.get(number), hashTable[number] +=1
    - else hashtable[number] = 0
for number in integers:
    - array.append(hashTable[number])
@return array
"""


def countingSort(array):
    """Got this solution from HackerRank discussions"""
    # maximum = max(arr)
    # arr1 = range(maximum + 1)
    result = [0] * 100
    for number in array:
        result[number] += 1
    return result


def countingSort_2(array):
    """DID NOT WORK"""
    hashTable = {}
    newArray = []
    for number in array:
        if hashTable.get(number):
            hashTable[number] += 1
        else:
            hashTable[number] = 0
    for number in array:
        newArray.append(hashTable[number])
    return newArray
