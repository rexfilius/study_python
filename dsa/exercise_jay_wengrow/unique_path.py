"""
Say you have a grid of rows and columns. Write a function that accepts a number
of rows and a number of columns, and calculates the number of possible "shortest"
paths from the upper-leftmost square to the lower-rightmost square.
"""


def uniquePaths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return uniquePaths(rows - 1, columns) + uniquePaths(rows, columns - 1)


def uniquePaths2(rows, columns, memo=dict()):
    """Using memoization to improve efficiency
    CODE NOT WORKING => memo[[rows, columns]]"""
    if rows == 1 or columns == 1:
        return 1
    if not memo[[rows, columns]]:
        memo[[rows, columns]] = uniquePaths2(rows - 1, columns, memo) + \
                                uniquePaths2(rows, columns - 1, memo)
    return memo[[rows, columns]]


print(uniquePaths2(3, 7))
