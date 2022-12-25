def quickSort(collection, start=0, end=None):
    if end is None:
        # collection = list(collection)  # this line isn't needed, no need for copy
        end = len(collection) - 1
    if start < end:
        pivot = partition(collection, start, end)
        quickSort(collection, start, pivot - 1)
        quickSort(collection, pivot + 1, end)
    return collection


def partition(collection, start=0, end=None):
    """Uses the last element in the list as the pivot"""
    if end is None:
        end = len(collection) - 1

    leftPointer, rightPointer = start, end - 1
    while rightPointer > leftPointer:
        # increment left pointer if number is <= to pivot
        if collection[leftPointer] <= collection[end]:
            leftPointer += 1
        # increment right pointer if number is > than pivot
        elif collection[rightPointer] > collection[end]:
            rightPointer -= 1
        # two out-of-place elements found, swap them
        else:
            collection[leftPointer], collection[rightPointer] = \
                collection[rightPointer], collection[leftPointer]

    # place the pivot between the two parts
    if collection[leftPointer] > collection[end]:
        collection[leftPointer], collection[end] = \
            collection[end], collection[leftPointer]
        return leftPointer
    else:
        return end
