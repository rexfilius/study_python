"""
Write a function that sorts temperature readings from lowest to highest.
Note - the decimal point never goes beyond the tenths place.
O(N) Time is a faster algorithm than the classic O(nlogN) because we are dealing
with a finite number of values.
"""


def sortTemperatures(array):
    """
    We're sorting a finite number of values. Specifically, there are only 21 types
    of temperature readings that we may find in this array, from: 97.0 to 99.0
    O(N) Time.
    """
    hashTable = {}
    for temp in array:
        if hashTable.get(temp):
            hashTable[temp] += 1
        else:
            hashTable[temp] = 1
    sortedArray = []
    # Multiply the temperature by 10 on the outset so that we can increment the
    # temperature by a whole number during the loop,
    # and avoid floating-point math errors:
    temperature = 970
    while temperature <= 990:
        if hashTable.get(temperature / 10.0):
            for n in range(hashTable[temperature / 10.0]):
                sortedArray.append(temperature / 10.0)
        temperature += 1
    return sortedArray


t = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
print(sortTemperatures(t))
