"""
Write a function that accepts an array of stock prices and determines whether there
are any three prices that create an upward trend.
Assume we are to find a single instance even if there are more.

input1 = [22, 25, 21, 18, 19.6, 17, 16, 20.5]
output = True; [18, 19.6, 20.5]

input2 = [50, 51.25, 48.4, 49, 47.2, 48, 46.9]
output = False

input3 = [5, 2, 8, 4, 3, 7]
output = True; [2, 3, 7]
"""


def tripleTrend(array):
    """Uses Greedy Approach. O(N) Time"""
    lowestPrice = array[0]
    middlePrice = float('inf')  # or math.inf
    for price in array:
        if price <= lowestPrice:
            lowestPrice = price
        elif price <= middlePrice:
            middlePrice = price
        else:
            return True
    return False


input1 = [22, 25, 21, 18, 19.6, 17, 16, 20.5]  # True; [18, 19.6, 20.5]
input2 = [50, 51.25, 48.4, 49, 47.2, 48, 46.9]  # False
input3 = [5, 2, 8, 4, 3, 7]  # True; [2, 3, 7]

print(tripleTrend(input3))