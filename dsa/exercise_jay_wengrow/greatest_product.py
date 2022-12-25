"""
Write a function that accepts an array of numbers and computes the highest product
of any two numbers in the array. The array can contain negative numbers.

input1 = [5, -10, -6, 9, 4]
output = 60; -10 x -6
"""
import math


def greatestProduct(array):
    greatestNum = -math.inf
    secondToGreatesrNum = -math.inf
    lowestNum = math.inf
    secondToLowestNum = math.inf

    for number in array:
        if number >= greatestNum:
            secondToGreatesrNum = greatestNum
            greatestNum = number
        elif number > secondToGreatesrNum:
            secondToGreatesrNum = number
        if number <= lowestNum:
            secondToLowestNum = lowestNum
            lowestNum = number
        elif lowestNum < number < secondToLowestNum:
            # number > lowestNum and number < secondToLowestNum
            secondToLowestNum = number

    greatestProductFromTwoHighest = greatestNum * secondToGreatesrNum
    greatestProductFromTwoLowest = lowestNum * secondToLowestNum
    if greatestProductFromTwoHighest > greatestProductFromTwoLowest:
        return greatestProductFromTwoHighest
    else:
        return greatestProductFromTwoLowest


print(greatestProduct([5, -10, -6, 9, 4]))
