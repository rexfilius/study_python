def countOnes(outerArray):
    """
    accepts an array of arrays, where the inner arrays contain 1's and 0's. The
    function then returns how many 1’s there are.
    Time complexity is O(N).
    """
    count = 0
    for innerArray in outerArray:
        for number in innerArray:
            if number == 1:
                count += 1
    return count


arr1 = [[0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0]]
print(countOnes(arr1))
