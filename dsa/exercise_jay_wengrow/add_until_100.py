"""
Write a function that accepts an array of numbers and returns the sum, as long as
a particular number doesn't bring the sum above 100. If adding a particular number
will make the sum higher than 100, that number is ignored.
"""


def addUntil100(array):
    if len(array) == 0:
        return 0
    sumOfRemaining = addUntil100(array[1:len(array)])
    if array[0] + sumOfRemaining > 100:
        return sumOfRemaining
    else:
        return array[0] + sumOfRemaining


e3 = [15, 5, 20, 5, 10, 30, 10, 10]
print(addUntil100(e3))
