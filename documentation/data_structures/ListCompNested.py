# The initial expression in a list comprehension can be any arbitrary expression,
# including another list comprehension.

# Consider the code below of a 3x4 matrix implemented as a list of 3 lists of length 4.
matrix_sample = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# The list comprehension below will transpose rows and columns
transpose_1 = [[row[i] for row in matrix_sample] for i in range(4)]
print(transpose_1)

# another way to write the matrix transposition
transpose_2 = []
for i in range(4):
    transpose_2.append([row[i] for row in matrix_sample])

print(transpose_2)

# another way to write the matrix transposition
transpose_3 = []
for i in range(4):
    transposed_row = []
    for row in matrix_sample:
        transposed_row.append(row[i])
    transpose_3.append(transposed_row)

print(transpose_3)

# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for this 'matrix transpose' use case
transpose_4 = list(zip(*matrix_sample))
print(transpose_4)
