"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than
value k. To do this, two cookies with the least sweetness are repeatedly mixed.
This creates a special combined cookie with:
sweetness = (1 x least sweet cookie + 2 x 2nd least sweet cookie).
This occurs until all the cookies have a sweetness >= k.
Given the sweetness of a number of cookies, determine the minimum number of
operations required. If it is not possible, return -1.

EXAMPLE::
k = 9
A = [2,7,3,6,4,6]
-- smallest values are 2 and 3
-- 1x2 + 2x3 = 8, remove 2 and 3, return 8 to array
A = [8,7,6,4,6]
-- smallest values are 4 and 6
-- 1x4 + 2x6 = 16, remove 4 and 6, return 16 to array
A = [16,8,7,6]
-- smallest values are 6 and 7
-- 1x6 + 2x7 = 20, remove 6 and 7, return 20 to array
A = [20,16,8]
-- smalles values are 8 and 16
-- 1x8 + 2x16 = 40, remove 8 and 16, return 40 to array
A = [40,20]
answer = 4, it took 4 iterations

k = 7
A = [1, 2, 3, 9, 10, 12]
-- smallest values are 1 and 2
-- 1x1 + 2x2 = 5, remove 1 and 2, return 5 to array
A = [5,3,9,10,12]
-- smallest values are 3 and 5
-- 1x3 + 2x5 = 13, remove 3 and 5, return 13 to array
A = [13,9,10,12]
answer = 2, it took two iterations

k = 90 answer is 5
A = [13 47 74 12 89 74 18 38]; sorted = [12 13 18 38 47 74 74 89]
-- smallest are 12 and 13
-- 1x12 + 2x13 = 38, remove 12 and 13, return 38 to array
A = [18 38 38 47 74 74 89]
-- smallest are 18 and 38
-- 1x18 + 2x38 = 94, remove 18 and 38, return 94 to array
A = [38 47 74 74 89 94]
-- smalles are 38 and 47
-- 1x38 + 2x47 = 132
A = [74 74 89 94 132]
-- smallest are 74 and 74
-- 1x74 + 2x74 = 222
A = [89 94 132 222]
-- smallest are 89 and 94
-- 1x89 + 2x94 = 277
A = [132 222 277]
answer = 5, it took 5 iterations

ALGO
parameters - k is an int, A is an array of int
variables - iterations = 0
sort the array A
if A[0] > k, return -1
for i in range(len(A)):
    - if A[0] > k, break out of loop
    - else::
        - get smallest value at A[0] and A[1]
        - replacement = 1xA[0] + 2xA[1]
        - A.pop(0 and 1)
        - A.append(replacement)
        - iterations += 1

"""
import heapq


def cookies(k, A: list):
    """Did not pass all the test cases"""
    iterations = 0
    A.sort()
    for i in range(len(A)):
        if A[0] > k:
            return iterations
        replacement = (1 * A[0]) + (2 * A[1])
        A = A[2:]
        A.append(replacement)
        iterations += 1
    return -1


def cookies_2(k, A):
    """Worked for all test cases. Uses a Heap"""
    heapq.heapify(A)
    count = 0
    while A[0] < k and len(A) > 1:
        h1 = heapq.heappop(A)
        h2 = heapq.heappop(A)
        heapq.heappush(A, h1 + h2 * 2)
        count += 1
    if A[0] >= k:
        return count
    else:
        return -1


k1, a1 = 9, [2, 7, 3, 6, 4, 6]
k2, a2 = 7, [1, 2, 3, 9, 10, 12]
k3, a3 = 90, [13, 47, 74, 12, 89, 74, 18, 38]
print(cookies(k1, a1))

# a3 = a3[2:]
# a3.append(400)
# print(a3)
