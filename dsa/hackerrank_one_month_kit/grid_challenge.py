"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of
each row alphabetically, ascending. Determine if the columns are also in ascending
alphabetical order, top to bottom. Return YES if they are or NO if they are not.

EXAMPLE::
grid = ['abc', 'ade', 'efg']
     - a b c
       a d e
       e f g
output = YES; all columns are in alphabetical order
Only elements within the same row can be rearranged.
They cannot be moved to a different row.

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
     - e b a c d  - a b c d e
       f g h i j    f g h i j
       o l m k n    k l m n o
       t r p q s    p q r s t
       x y w u v    u v w x y
output  = YES; the grid can be reordered and still fulfills the conditons

grid = [abc, lmp, qrt]
output = YES

grid = [mpxz, abcd, wlmf]
     - m p x z  - m p x z
       a b c d    a b c d
       w l m f    f l n w
output = NO; columns not in order even when reordered

grid = [abc, hjk, mpq, rtv]
     - a b c
       h j k
       m p q
       r t v
output = YES; already ordered, fulfills condition

Output Format::
For each test case, on a separate line print YES if it is possible to rearrange
the grid alphabetically ascending in both its rows and columns, or NO otherwise.

CONSTRAINTS::
Each string consists of lowercase letters in the range ascii[a-z]

ALGO::
for string in grid
    - sort each string and return a sortedStringList
for i in len(sortedString)
    - if i equals len(sortedString) minus 1; break
    - for j in len(sortedString[i])
        - if letter at sortedString[i][j] <= sortedString[i+1][j], continue
        - else if not less than, return NO
return YES
"""


def gridChallenge(grid):
    """
    ascii of 'a' is 97 and 'z' is 122
    :param grid: an array of string
    """
    sortedString = []
    for value in grid:
        sortedString.append(sorted(value))
    for i in range(len(sortedString)):
        if i == len(sortedString) - 1:
            break
        for j in range(len(sortedString[i])):
            if sortedString[i][j] <= sortedString[i + 1][j]:
                continue
            else:
                return 'NO'
    return 'YES'


grid1 = ['abc', 'ade', 'efg']  # answer is YES
grid2 = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']  # answer is YES
grid3 = ['abc', 'lmp', 'qrt']  # answer is YES
grid4 = ['mpxz', 'abcd', 'wlmf']  # answer is NO

# ..........0......1......2......3
grid5 = ['abc', 'hjk', 'mpq', 'rtv']  # answer is YES
# ........012....012....012....012
# [0][0] and [1][0] .. a and h
# [0][1] and [1][1] .. b and j
# [0][2] and [1][2] .. c and k
# [1][0] and [2][0] .. h and m
# [1][1] and [2][1] .. j and p
# [1][2] and [2][2] .. k and q
# [2][0] and [3][0] .. m and r
# [2][1] and [3][1] .. p and t
# [2][2] and [3][2] .. q and v
# [3][0] and
for a in range(len(grid4)):
    for b in range(len(grid4[a])):
        if a == len(grid4) - 1:
            break
        print(grid4[a][b], grid4[a + 1][b], grid4[a][b] < grid4[a + 1][b])
print('---------------------------------------')

print(gridChallenge(grid5))
