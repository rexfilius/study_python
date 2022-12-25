def bubbleSort(collection):
    """
    1. Iterate over the list of numbers, starting from the left
    2. Compare each number with the number that follows it
    3. If the number is greater than the one that follows it,
    swap the two elements
    4. Repeat steps 1 to 3 till the list is sorted.
    We'll create a copy of the list inside our function, to avoid changing
    it while sorting.
    """
    nlist = list(collection)
    # 4. Repeat the process 'n-1' times
    for i in range(len(nlist) - 1):
        # print('Iteration', i)  # LOGGING
        # 1. Iterate over the list (except last element)
        for j in range(len(nlist) - 1):
            # 2. Compare the value with the one at the next index, and,
            # 3. swap if value at next is greater than the one in current index
            # (using tuple assignment to swap two elements ina single line of code)
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    # return the sorted list
    return nlist


def insertSort(collection):  # [10, 9, 8, 7, 6]
    nlist = list(collection)
    for i in range(len(nlist)):  # 0 1 2 3 4 5
        current = nlist.pop(i)
        j = i - 1
        while j >= 0 and nlist[j] > current:
            j -= 1
        nlist.insert(j + 1, current)
    return nlist
