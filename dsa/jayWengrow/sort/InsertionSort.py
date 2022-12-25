def insertionSort(collection):
    """Implementation of insertion sort.
    Time complexity is O(N^2)"""
    for index in range(1, len(collection)):
        tempValue = collection[index]
        position = index - 1
        while position >= 0:
            if collection[position] > tempValue:
                collection[position + 1] = collection[position]
                position -= 1
            else:
                break
        collection[position + 1] = tempValue
    return collection

