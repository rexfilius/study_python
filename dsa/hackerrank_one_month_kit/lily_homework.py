"""
COPIED FROM HACKERRANK DISCUSSIONS ... I QUITE UNDERSTAND IT

ALGO::
The most beautiful array is going to be the sorted array, either in ascending or descending order.
So you need to find how many swaps it takes to sort the array both ways.
https://www.youtube.com/watch?v=-2_c4lG7k_M
You make an array of objects that store the value and index of the original array,
and then sort it by values. From there, you make the swaps back to the original order using the stored
index values.
Since we're finding the minimum swaps, you do this twice: once for ascending and once for descending.
"""


def countSwaps(arr, d):
    index, swaps = 0, 0
    print('array to check swaps', arr)
    while index < len(arr):
        loc = d[arr[index]]  # loc is = map-value of number in dict
        print('loc', loc)
        if loc == index:
            index += 1
            continue
        arr[index], arr[loc] = arr[loc], arr[index]
        swaps += 1
    print('array after swaps', arr)
    return swaps


def lilyHomework(arr):
    sortedArray = sorted(arr)
    forward = {value: index for index, value in enumerate(sortedArray)}
    backward = {value: index for index, value in enumerate(reversed(sortedArray))}
    print('forward', forward)
    print('backward', backward)
    return min(countSwaps(arr.copy(), forward), countSwaps(arr.copy(), backward))


print(lilyHomework([7, 15, 12, 3]))
