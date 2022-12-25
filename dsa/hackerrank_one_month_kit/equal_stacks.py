"""
You have three stacks of cylinders where each cylinder has the same diameter,
but they may vary in height. You can change the height of a stack by removing and
discarding its topmost cylinder any number of times.
Find the maximum possible height of the stacks such that all the stacks are exactly
the same height. This means you must remove zero or more cylinders from the top
of zero or more of the three stacks until they are all the same height, then return
the height.

EXAMPLE:: (note - the lists are stacks, topmost is index 0)
h1 = [1,2,1,1] => sum is 5
h2 = [1,1,2]   => sum is 4
h3 = [1,1]     => sum is 2
remove [1,2] from h1, becomes [1,1]
remove [1,1] from h2, becomes [2]
-> all the stacks now have a height of '2'
output = 2

h1 = [3, 2, 1, 1, 1]  => sum is 8
h2 = [4, 3, 2]        => sum is 9
h3 = [1, 1, 4, 1]     => sum is 7
remove [3] from h1, becomes [2,1,1,1]
remove [4] from h2, becomes [3,2]
remove [1,1] from h3, becomes [4,1]
-> all the stacks now have a height of '5'
output = 5

"""


def equalStacks(h1, h2, h3):
    """Gotten from HackerRank discussions. Well understood"""
    sumh1, sumh2, sumh3 = sum(h1), sum(h2), sum(h3)

    while h1 and h2 and h3:
        if sumh1 == sumh2 & sumh2 == sumh3:
            return sumh1
        minSum = min(sumh1, sumh2, sumh3)
        if sumh1 > minSum:
            sumh1 -= h1.pop(0)
        if sumh2 > minSum:
            sumh2 -= h2.pop(0)
        if sumh3 > minSum:
            sumh3 -= h3.pop(0)
    return 0
