"""
Needle and Haystack are strings. For example, if the needle is "def" and the
haystack is "abcdefghi", the needle is contained somewhere in the haystack,
as "def" is a substring of "abcdefghi". However, if the needle is "dd", it cannot
be found in the haystack of "abcdefghi".
"""


def findNeedle(needle, haystack):
    """Returns True if needle is found, otherwise False"""
    foundNeedle = None
    needleIndex = 0
    haystackIndex = 0
    while haystackIndex < len(haystack):
        if needle[needleIndex] == haystack[haystackIndex]:
            foundNeedle = True
        while needleIndex < len(needle):
            if needle[needleIndex] != haystack[haystackIndex + needleIndex]:
                foundNeedle = False
                break
            needleIndex += 1
        if foundNeedle:
            needleIndex = 0
            return True
        haystackIndex += 1
    return False


print(findNeedle('def', 'abcdefghi'))
