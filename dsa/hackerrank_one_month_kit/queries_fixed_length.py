"""

EXAMPLE::
arr = [2,3,4,5,6]
queries = [2,3]
query of 2 => [2,3] [3,4] [4,5] [5,6]
maximas are => [3,4,5,6] and minimum(maxima) => 3
query of 3 => [2,3,4] [3,4,5] [4,5,6]
maximas are => [4,5,6] and minimum(maxima) => 4
output = [3,4]

arr = [33 11 44 11 55] => [11 11 33 44 55]
queries = [1,2,3,4,5]
q of 1 = [11] [11] [33] [44] [55] = maximas [11 33 44 55] = min is 11
q of 2 = [11,11] [11,33] [33,44] [44,55] = maximas
"""


def fixedQueries(arr, queries):
    """Gotten from HackerRank discussions"""
    answers = []
    for d in queries:
        # find max of first section and initialize minimum
        minimum = maximum = max(arr[:d])
        for i in range(1, len(arr) - d + 1):
            # IF arr[i-1] is max, we need to find the maximum of current section
            if arr[i - 1] == maximum:
                maximum = max(arr[i:i + d])
                # IF the new maximum is less than minimum set to new minimum
                if maximum < minimum:
                    minimum = maximum
        answers.append(minimum)
    return answers
