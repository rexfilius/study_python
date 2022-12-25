from algoFreeCodeCamp.courseJovian.dynamicProg.Dyn1 \
    import lcsRecursive, lcsMemoize, lcsDynamic

sequence1 = 'serendipitous'
sequence2 = 'precipitation'
sequence3 = [1, 3, 5, 6, 7, 2, 5, 2, 3]
sequence4 = [6, 2, 4, 7, 1, 5, 6, 2, 3]
sequence5 = 'longest'
sequence6 = 'stone'
sequence7 = 'lgst'
sequence8 = 'zxne'
sequence9 = 'dense'
sequence10 = 'condensed'

# print(lcsRecursive(sequence1, sequence2))  # answer = 7
# print(lcsRecursive(sequence3, sequence4))  # answer = 5
# print(lcsRecursive(sequence5, sequence6))  # answer = 3
# print(lcsRecursive(sequence7, sequence8))  # answer = 0
# print(lcsRecursive(sequence9, sequence10))  # answer = 5
# print('empty sequence case:', lcsRecursive('', ''))  # answer = 0
# print('multiple subsequence:', lcsRecursive('abcdef', 'badcfe'))  # answer = 3

# print(lcsMemoize(sequence1, sequence2))  # answer = 7
# print(lcsMemoize(sequence3, sequence4))  # answer = 5
# print(lcsMemoize(sequence5, sequence6))  # answer = 3
# print(lcsMemoize(sequence7, sequence8))  # answer = 0
# print(lcsMemoize(sequence9, sequence10))  # answer = 5
# print('empty sequence case:', lcsMemoize('', ''))  # answer = 0
# print('multiple subsequence:', lcsMemoize('abcdef', 'badcfe'))  # answer = 3
# print()

# Matrix/Table in list form
# n1, n2 = 5, 7
# table = [[0 for _ in range(7)] for _ in range(5)]
# print(table)

print(lcsDynamic(sequence1, sequence2))  # answer = 7
print(lcsDynamic(sequence3, sequence4))  # answer = 5
print(lcsDynamic(sequence5, sequence6))  # answer = 3
print(lcsDynamic(sequence7, sequence8))  # answer = 0
print(lcsDynamic(sequence9, sequence10))  # answer = 5
print('empty sequence case:', lcsDynamic('', ''))  # answer = 0
print('multiple subsequence:', lcsDynamic('abcdef', 'badcfe'))  # answer = 3
print()
