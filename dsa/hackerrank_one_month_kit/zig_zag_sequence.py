"""
Given an array of n distinct integers, transform the array into a zigzag sequence
by permuting the array elements. A sequence will be called a zigzag sequence if the
first k elements in the sequence are in increasing order and the last k elements are
in decreasing order, where k=(n+1)/2. You need to find the lexicographically
smallest zigzag sequence of the given array.

EXAMPLE::
array = [2,3,5,1,4] = k is (5+1)/2 => 3
permuted = [1,4,5,3,2]

array = [1 2 3 4 5 6 7] = k is (7+1)/2 => 4
permuted = [1,2,3,7,6,5,4]
"""


def findZigZagSequence(a, n):
    a.sort()
    mid = int(n / 2)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return
