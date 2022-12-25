def mergeSort(collection):
    if len(collection) <= 1:
        return collection

    midPoint = len(collection) // 2
    left = collection[:midPoint]
    right = collection[midPoint:]

    leftSorted, rightSorted = mergeSort(left), mergeSort(right)
    sortedList = merge(leftSorted, rightSorted)
    return sortedList


def merge(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    list1Tail = list1[i:]
    list2Tail = list2[j:]
    return merged + list1Tail + list2Tail


def mergeSortCheck(collection, depth=0):
    print(' ' * depth, f'MergeSort d{depth}:', collection)
    if len(collection) <= 1:
        return collection

    midPoint = len(collection) // 2
    left = collection[:midPoint]
    right = collection[midPoint:]

    leftSorted = mergeSortCheck(left, depth + 1)
    rightSorted = mergeSortCheck(right, depth + 1)
    sortedList = mergeCheck(leftSorted, rightSorted, depth + 1)
    return sortedList


def mergeCheck(list1, list2, depth=0):
    print(' ' * depth, f'Merge d{depth}:', list1, list2)
    i, j, merged = 0, 0, []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    return merged + list1[i:] + list2[j:]
