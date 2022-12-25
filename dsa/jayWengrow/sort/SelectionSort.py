def selectionSort(collection):
    """Implementation of Selection Sort.
    Time complexity is O(N^2) - though, quite faster than _ sort"""
    for i in range(len(collection)):
        lowestNumberIndex = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[lowestNumberIndex]:
                lowestNumberIndex = j
        if lowestNumberIndex != i:
            collection[i], collection[lowestNumberIndex] \
                = collection[lowestNumberIndex], collection[i]
    return collection
