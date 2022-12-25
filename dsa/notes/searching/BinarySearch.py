# BINARY SEARCH

def binarySearch(collection, searchValue):
    """
    Implementation of binary search in an ordered array/list
    Time complexity is O(logN)
    """
    lowerBound = 0
    upperBound = len(collection) - 1
    while lowerBound <= upperBound:
        midPoint = (upperBound + lowerBound) // 2
        valueAtMidPoint = collection[midPoint]
        if searchValue == valueAtMidPoint:
            return midPoint
        elif searchValue < valueAtMidPoint:
            upperBound = midPoint - 1
        elif searchValue > valueAtMidPoint:
            lowerBound = midPoint + 1
    return 0
