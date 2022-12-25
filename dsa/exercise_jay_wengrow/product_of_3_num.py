"""
Given an array of positive numbers, write a function that returns the greatest
product of any three numbers.

array = [2,5,6,7,3,4]
sorted = [2,3,4,5,6,7]

Solution = If we sort the numbers, we know that the three greatest numbers
will be at the end of the array, and we can just multiply them together.
"""


def productOfThree(collection):
    collection.sort()
    return collection[len(collection) - 1] * collection[len(collection) - 2] \
           * collection[len(collection) - 3]


e3 = [2, 5, 6, 7, 3, 4]
print(productOfThree(e3))
