def hasDuplicateValue(collection):
    collection.sort()
    for index in range(len(collection)):
        if collection[index] == collection[index + 1]:
            return True
    return False  # no duplicates in array


d3 = [5, 9, 3, 2, 4, 5, 6]
print(hasDuplicateValue(d3))
