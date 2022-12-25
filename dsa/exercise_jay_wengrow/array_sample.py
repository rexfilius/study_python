def arraySample(collection):
    """a function that takes a small sample of an array.
    Time complexity is O(1)"""
    first = collection[0]
    middle = collection[len(collection) // 2]
    last = collection[-1]
    return [first, middle, last]


arr1 = [1, 2, 3, 4, 5]
print(arraySample(arr1))
