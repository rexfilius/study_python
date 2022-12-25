"""
Write an algorithm that takes an array of numbers and doubles each
of the numbers within the array.
"""


def doubleArray_1(array):
    """O(N) Time and Space"""
    result = []
    for i in range(len(array)):
        result.append(array[i] * 2)
    return result


def doubleArray_2(array):
    """O(N) Time. O(1) Space"""
    for i in range(len(array)):
        array[i] *= 2
    return array


def doubleArray_3(array, index=0):
    """O(N) Time and Space"""
    if index >= len(array):
        return
    array[index] *= 2
    doubleArray_3(array, index + 1)
    return array


a1 = [1, 2, 3, 4, 5]
print(doubleArray_1(a1))
# print(doubleArray_2(a1))
# print(doubleArray_3(a1))