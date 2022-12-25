"""
A '100-Sum Array' meets the following criteria:
1. Its first and last numbers add up to 100.
2. Its second and second-to-last numbers add up to 100.
3. Its third and third-to-last numbers add up to 100, and so on.
"""


def hundredSum(array):
    """
    This function returns true if the array is a "100-Sum Array"
    and false if it is not. Time complexity is O(N).
    """
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex < len(array) // 2:
        if array[leftIndex] + array[rightIndex] != 100:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True


s1 = [50, 40, 10, 5, 95, 90, 60, 50]
print(hundredSum(s1))
