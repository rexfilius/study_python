"""
Hackerland is a one-dimensional city with houses aligned at integral locations
along a road. The Mayor wants to install radio transmitters on the roofs of the
city's houses. Each transmitter has a fixed range meaning it can transmit a signal
to all houses within that number of units distance away.
Given a map of Hackerland and the transmission range, determine the minimum number
of transmitters so that every house is within range of at least one transmitter.
Each transmitter must be installed on top of an existing house.

int x[n]: the locations of houses
int k: the effective range of a transmitter
output = int: the minimum number of transmitters to install
EXAMPLE::
x = [1,2,3,5,9]
k = 1
3 antennae at houses 2 and 5 and 9 provide complete coverage.
There is no house at location 7 to cover both 5 and 9.
Ranges of coverage are [1,2,3] and [5] and [9].
output = 3

x = [1, 2, 3, 4, 5]
k = 1
2 antennae at houses 2 and 4 provide complete coverage.
output = 2

x = [7 2 4 6 5 9 12 11] => [1 2 3 4 5 6 7 8 9 10 11 12]
k = 2
3 antennae at houses 4 and 9 and 12.
output = 3
"""


def radioTransmitters(x, k):
    """x is an array, k is an int"""
    x.sort()
    houseWithRadio = x[0]
    lowestHouseCoveredByRadio = x[0]
    radio = 1
    for num in x:
        if num - houseWithRadio > k:
            radio += 1
            houseWithRadio = num
            lowestHouseCoveredByRadio = num
        elif num - lowestHouseCoveredByRadio <= k:
            houseWithRadio = num
    return radio
