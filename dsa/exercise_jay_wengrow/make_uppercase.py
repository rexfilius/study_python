def makeUppercase(array):
    """
    Function that accepts an array of strings and returns
    an array of those strings in ALL CAPS.
    Space complexity of O(N).
    """
    newArray = []
    for value in array:
        newArray.append(value.upper())
    return newArray


def makeUpperCase2(array):
    """Space complexity of O(1). More efficient than previous"""
    for index, value in enumerate(array):
        array[index] = value.upper()
    return array


namesArray = ["tuvi", "leah", "shaya", "rami"]
print(makeUppercase(namesArray))
print(makeUpperCase2(namesArray))
