"""
Two friends like to pool their money and go to the ice cream parlor. They always
choose two distinct flavors, and they spend all of their money.
Given a list of prices for the flavors of ice cream, select the two that will
cost all the money they have.

EXAMPLE::
m = 6
cost = [1,3,4,5,6]
the two flavors that cost 1 and 5 meet the criteria.
output = [1,4] - using 1-based indexing

m = 4
cost = [1,4,5,3,2]
two flavors are 1 and 3
output = [1,4] - using 1-based indexing

m = 4
cost = [2,2,4,3]
two flavors are 2 and 2
output = [1,2] - using 1-based indexing

ALGO::
output = []
for i in 0 to len-2:
    - for j in i+1 to len-1:
        - if arr[i] + arr[j] = m; output.append(i+1), output.append(j+1)
"""


def iceCreamParlor(m, arr):
    output = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == m:
                output.extend([i + 1, j + 1])
                break
    return output


m1, cost1 = 6, [1, 3, 4, 5, 6]  # output [1,4] => indices 0 and 3
m2, cost2 = 4, [1, 4, 5, 3, 2]  # output [1,4] => indices 0 and 3
m3, cost3 = 4, [2, 2, 4, 3]  # output [1,2] => indices 0 and 1
print(iceCreamParlor(m3, cost3))
