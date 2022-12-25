"""
Write a function that accepts an array of numbers and return true or false depending
on whether there are any two numbers in the array that add up to 10
(or another given number). Assume there will never be duplicate numbers in the array.

input1 = [2, 0, 4, 1, 7, 9]
output1 = True. 1+9=10

input2 = [2, 0, 4, 5, 3, 9]
output2 = False. no two numbers equal 10
"""


def twoSum(array):
    """O(N^2) Time."""
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if i != j and array[i] + array[j] == 10:
                return True
    return False


def twoSum_2(array):
    """O(N) Time"""
    hashTable = {}
    for i in range(len(array)):
        # Check if the hash table contains a key which, when added
        # to the current number, would add up to 10:
        if (10 - array[i]) in hashTable.keys():
            return True
        hashTable[array[i]] = True
    return False


t1 = [2, 0, 4, 1, 7, 9]  # True
t2 = [2, 0, 4, 5, 3, 9]  # False

print(twoSum_2(t1))
