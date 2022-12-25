"""
Write a function that accepts an array of unsorted integers and returns
the length of the longest consecutive sequence among them.
The sequence is formed by integers that increase by 1.

input1 = [10, 5, 12, 3, 55, 30, 4, 11, 2]
output1 = 4; 2-3-4-5

input2 = [19, 13, 15, 12, 18, 14, 17, 11]
output2 = 5; 11-12-13-14-15
"""


def longestSequence(array):
    hashTable = {}
    greatestSequenceLength = 0
    for num in array:
        hashTable[num] = True
    for number in array:
        if not hashTable.get(number - 1):
            currentSequenceLength = 1
            currentNumber = number
            while hashTable.get(currentNumber + 1):
                currentNumber += 1
                currentSequenceLength += 1
                if currentSequenceLength > greatestSequenceLength:
                    greatestSequenceLength = currentSequenceLength
    return greatestSequenceLength


s1 = [10, 5, 12, 3, 55, 30, 4, 11, 2]  # answer is 4
s2 = [19, 13, 15, 12, 18, 14, 17, 11]  # answer is 5
print(longestSequence(s2))
