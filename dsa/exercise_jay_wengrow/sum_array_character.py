"""
Write a function that accepts an array of strings and returns the total number
of characters across all the strings.
input = ["ab", "c", "def", "ghij"]
output = 10
"""


def sumArrayCharacters(array):
    if len(array) == 1:
        return len(array[0])
    return len(array[0]) + sumArrayCharacters(array[1:len(array)])


input1 = ["ab", "c", "def", "ghij"]
input2 = ["abc", "def", "ghi", "jkl", "mno"]
print(sumArrayCharacters(input1))
print(sumArrayCharacters(input2))
