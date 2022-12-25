"""
Given a list of integers, arr, and a single integer k. Create an array of length k
from elements of arr such that its unfairness is minimized. Call that array arr'.
Unfairness of an array is calculated as - max(arr') minus min(arr') -
- max denotes the largest integer in arr'; min denotes the smallest integer in arr'
Note: integers in arr may not be unique
@return - the minimum possible unfairness

EXAMPLE::
arr = [1,4,7,2]
k = 2
pick any two elements, say arr' = [4,7]
unfairness = max(4,7) - min(4,7) = 7 - 4 = 3
Testing for all pairs, the solution [1,2] provides the minimum unfairness.

"""


def maxMin(k, array):
    """gotten from HackerRank discussions"""
    k -= 1
    array.sort()
    return min(array[i + k] - array[i] for i in range(len(array) - k))
