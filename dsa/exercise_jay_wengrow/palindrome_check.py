"""
A palindrome is a word or phrase that reads the same both forward and backward.
e.g. racecar, kayak, deified
"""


def isPalindrome(string):
    """Time complexity is O(N)"""
    leftIndex = 0
    rightIndex = len(string) - 1
    while leftIndex < len(string) // 2:
        if string[leftIndex] != string[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True


print(isPalindrome('racecar'))
print(isPalindrome('kayak'))
print(isPalindrome('deified'))
print(isPalindrome('nurses'))
