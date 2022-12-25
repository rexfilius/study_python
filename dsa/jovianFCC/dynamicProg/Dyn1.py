"""
Write a function to find the length of the longest common subsequence between
two sequences e.g. given the strings 'serendipitous' and 'precipitation', the
longest common subsequence is 'reipito' and its length is 7.
- A sequence is a group of items with a deterministic ordering. Lists, tuples,
and ranges are common sequence types in Python.
- A subsequence is a sequence obtained by deleting zero or more elements from
another sequence. e.g. 'edpt' is a subsequence of serendipitous
"""


# lcs = lengthOfCommonSubsequence
# time complexity = O(2^m+n)
def lcsRecursive(sequence1, sequence2, index1=0, index2=0):
    if index1 == len(sequence1) or index2 == len(sequence2):
        return 0
    elif sequence1[index1] == sequence2[index2]:
        return 1 + lcsRecursive(sequence1, sequence2, index1 + 1, index2 + 1)
    else:
        option1 = lcsRecursive(sequence1, sequence2, index1 + 1, index2)
        option2 = lcsRecursive(sequence1, sequence2, index1, index2 + 1)
        return max(option1, option2)


# downside to memoization is recursive calls
def lcsMemoize(sequence1, sequence2):
    memo = {}

    def recurse(index1=0, index2=0):
        key = (index1, index2)
        if key in memo:
            return memo[key]
        elif index1 == len(sequence1) or index2 == len(sequence2):
            memo[key] = 0
        elif sequence1[index1] == sequence2[index2]:
            memo[key] = 1 + recurse(index1 + 1, index2 + 1)
        else:
            memo[key] = max(recurse(index1 + 1, index2), recurse(index1, index2 + 1))
        return memo[key]

    return recurse(0, 0)
    # END OF FUNCTION - lcsMemoize()


def lcsDynamic(sequence1, sequence2):
    n1, n2 = len(sequence1), len(sequence2)
    table = [[0 for x in range(n2 + 1)] for x in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if sequence1[i] == sequence2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
    return table[-1][-1]
