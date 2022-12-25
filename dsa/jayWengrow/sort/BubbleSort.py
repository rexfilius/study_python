def bubbleSort(collection):
    """Implementation of bubble sort algorithm
    Time complexity is O(N^2) - Quadratic Time"""
    # keeps track of the rightmost index of the array that hasn't yet been sorted
    unsortedUntilIndex = len(collection) - 1
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(unsortedUntilIndex):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                isSorted = False
        unsortedUntilIndex -= 1
    return collection

