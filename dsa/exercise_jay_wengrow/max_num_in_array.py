"""
Function that finds the greatest number from an array
"""


# UNNECESSARY RECURSIVE CALLS!!!
def maxRecursive(array):
    """gets called 15 times. so unnecessary"""
    print('RECURSION!!')
    if len(array) == 1:
        return array[0]
    if array[0] > maxRecursive(array[1:len(array)]):
        return array[0]
    else:
        return maxRecursive(array[1:len(array)])


# UNNECESSARY RECURSIVE CALLS!!! but better than previous
def maxRecursive2(array: list):
    """gets called 4 times. O(N) time"""
    print('RECURSION!!')
    if len(array) == 1:
        return array[0]
    maxOfRemainder = maxRecursive2(array[1:len(array)])
    if array[0] > maxOfRemainder:
        return array[0]
    else:
        return maxOfRemainder


d3 = [1, 2, 3, 4]
print(maxRecursive(d3), '\n')
print(maxRecursive2(d3))
