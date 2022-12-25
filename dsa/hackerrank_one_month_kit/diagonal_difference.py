"""
Given a square matrix, calculate the absolute difference between
the sums of its diagonals.

matrix - 1 2 3
         4 5 6
         9 8 9
left-to-right diagonal = 1+5+9 = 15
right-to-left diagonal = 3+5+9 = 17
absolute difference = |15-17| = 2

ALGO::
Get the left-to-right diagonal , and sum the values
Get the right-to-left diagonal, and sum the values
return abs(left-to-right minus right-to-left)
"""


def diagonalDifference(array):
    """
    This didn't work with all the hidden test cases in HackerRank,
    because it is handling only a 3x3 matrix.
    """
    leftToRight = array[0][0] + array[1][1] + array[2][2]
    rightToLeft = array[0][2] + array[1][1] + array[2][0]
    difference = leftToRight - rightToLeft
    return abs(difference)


def diagonalDifference_2(array):
    """This worked with all the hidden test cases in HackerRank"""
    length = len(array)
    leftToRight = 0
    rightToLeft = 0
    for i in range(length):
        leftToRight += array[i][i]
        rightToLeft += array[i][length - i - 1]
    return abs(leftToRight - rightToLeft)


matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]  # square matrix
print(matrix[0][0], matrix[1][1], matrix[2][2])  # left-to-right diagonal
print(matrix[0][2], matrix[1][1], matrix[2][0], '\n')  # right-to-left diagonal

print(diagonalDifference_2(matrix), '\n')
