def twoNumberProducts(array):
    """
    Accepts an array of numbers and returns the product of every
    combination of two numbers.
    given: [1, 2, 3, 4, 5]
    return: [2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
    explain: [1x2,1x3,1x4,1x5,2x3,2x4,2x5,3x4,3x5,4x5]
    Time Complexity is O(N^2).
    """
    products = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            products.append(array[i] * array[j])
    return products


def twoNumberProductsM(array1, array2):
    """
    Compute the product of every number from one array by every number
    of a second array
    given: [1,2,3] and [10,100,1000]
    return: [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]
    explain: [1x10,1x100,1x1000,2x10,2x100,2x1000,3x10,3x100,3x1000]
    Time complexity is O(N*M)
    """
    products = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            products.append(array1[i] * array2[j])
    return products


a1 = [1, 2, 3, 4, 5]
a2 = [1, 2, 3]
a3 = [10, 100, 1000]

print(twoNumberProducts(a1), '\n')
print(twoNumberProductsM(a2, a3))
