# LINEAR SEARCH

def linearSearch(collection, searchValue):
    """
    Implementation of linear search on an ordered array/list.
    Time complexity is O(N)
    """
    for index, element in enumerate(collection):
        if element == searchValue:
            return index
        elif element > searchValue:
            break
    return 0
