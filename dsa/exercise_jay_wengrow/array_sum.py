# Write a function called that sums up all the numbers in a given array.
def sumArrayItems(array):
    if len(array) == 1:
        return array[0]
    return array[0] + sum(array[1:len(array)])


ad = [1, 2, 3, 4, 5]
print(sumArrayItems(ad))
