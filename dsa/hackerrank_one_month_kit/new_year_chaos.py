"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions, but they
still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order.
Print the number of bribes, or, if anyone has bribed more than two people,
print 'Too chaotic'.

EXAMPLE::
q = [1,2,3,5,4,6,7,8] => original is [1,2,3,4,5,6,7,8]
5 bribed 4. only 1 bribe happened
output = print 1

q = [4,1,2,3] => original is [1,2,3,4]
4 bribed 3 and 2 and 1. 3 bribes happened
output = print 'Too chaotic'

q = [2,1,5,3,4] => original is [1,2,3,4,5]
5 bribes 4 and 3. 2 bribes 1. 3 bribes happened
output = print 'Too chaotic'

q = [1,2,5,3,4,7,8,6] => original is [1,2,3,4,5,6,7,8]
5 bribed 4 and 3. 6 bribed 7 and 8. 4 bribes happened
output = print 'Too chaotic'
"""


def minimumBribes(q):
    """Gotten from HackerRank discussions"""
    bribes = 0
    for i in range(len(q)):
        if q[i] - i > 3:
            print("Too chaotic")
            return
        j = i - 1
        while i and q[i] < q[j]:
            q[i], q[j] = q[j], q[i]
            i, j = i - 1, j - 1
            bribes += 1
    print(bribes)


print(minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]))
