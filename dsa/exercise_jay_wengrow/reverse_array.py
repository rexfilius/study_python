def reverseArray(array):
    """Space complexity is O(N)"""
    result = []
    for index in range(len(array) - 1, -1, -1):
        result.append(array[index])
    return result


def reverseArray_2(array):
    for val in reversed(array):
        print(val, end=' ')


def reverseArray_3(array):
    """
    The following implementation uses this algorithm: we swap the first item with
    the last item in place. Then, we swap the second item with the second-to-last
    item in place. We then proceed to swap the third item with the third-to-last
    item in place, and so on. Since everything is done in place, and we don't
    create any new data, this has a space complexity of O(1).
    """
    for index in range(len(array) // 2):
        array[index], array[(len(array) - 1) - index] = \
            array[(len(array) - 1) - index], array[index]
    return array


sd = ['a', 'b', 'c', 'd', 'e']
print(reverseArray(sd))
print(reverseArray_2(sd))
print(reverseArray_3(sd))
