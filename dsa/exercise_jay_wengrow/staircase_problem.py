"""
Say we have a staircase of N steps, and a person has the ability to climb one,
two, or three steps at a time. How many possible 'paths' can someone take to reach
the top? Write a function that will calculate this for N steps.
"""


def numberOfPaths(nSteps):
    if nSteps < 0:
        return 0
    if nSteps == 1 or nSteps == 0:
        return 1
    return numberOfPaths(nSteps - 1) + \
           numberOfPaths(nSteps - 2) + numberOfPaths(nSteps - 3)


print(numberOfPaths(0))
print(numberOfPaths(1))
print(numberOfPaths(2))
print(numberOfPaths(3))
