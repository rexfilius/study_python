"""
Write three different implementations of a function that finds the
greatest number within an array. Write one function that is O(N^2),
one that is O(N log N), and one that is O(N).
"""


def greatestNumber(array):
    """maybe O(nLogN) time"""
    array.sort()
    return array[-1]


def greatestNumber2(array):
    """maybe O(N) time"""
    gNumber = array[0]
    for number in array:
        if number > gNumber:
            gNumber = number
    return gNumber


def greatestNumber3(array):
    """maybe O(N^2) time"""
    for val in array:
        isGreatestNumber = True
        for j in array:
            if j > val:
                isGreatestNumber = False
        if isGreatestNumber:
            return val


def greatestNumber4(array):
    """Greedy algorithm approach. O(N) Time."""
    greatestNum = array[0]
    for number in array:
        if number > greatestNum:
            greatestNum = number
    return greatestNum


d4 = [13, 15, 19, 10, 17]
print(greatestNumber(d4))
print(greatestNumber2(d4))
print(greatestNumber3(d4))
print(greatestNumber4(d4))
