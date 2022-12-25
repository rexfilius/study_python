"""
Use recursion to write a function that accepts an array of numbers
and returns a new array containing just the even numbers.

i1 = [1,2,3,4,5,6]
output = [2,4,6]
"""


def selectEvenNumbers(array):
    if len(array) == 0:
        return []
    if array[0] % 2 == 0:
        return [array[0]] + selectEvenNumbers(array[1:len(array)])
    else:
        return selectEvenNumbers(array[1:len(array)])


print(selectEvenNumbers([1, 2, 3, 4, 5, 6]))
