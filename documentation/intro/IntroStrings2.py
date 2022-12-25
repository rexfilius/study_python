# Strings can be indexed (subscripted), with the first character having index 0.
# There is no separate character type; a character is simply a string of size one.
eightLetters = "ABCDEFG"
print(eightLetters[2])  # ans = C

# Indices may also be negative numbers, to start counting from the right.
# Note that since -0 is the same as 0, negative indices start from -1
print(eightLetters[-2])  # ans = F

# In addition to indexing, slicing is also supported. While indexing is used to obtain
# individual characters, slicing allows you to obtain substring.
# Slice indices have useful defaults; an omitted first index defaults to zero,
# an omitted second index defaults to the size of the string being sliced.
print(eightLetters[0:4])  # from position 0 (included) to 4(excluded); ans = ABCD
print(eightLetters[-3:])  # from third-last to the end; ans = EFG

print(eightLetters[:4])  # from position 0 to 4 (excluded); ans = ABCD
print(eightLetters[3:])  # from position 3 (included) to the end; ans = DEFG
print()

# Slicing: Note how the start position is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s:
print(eightLetters[:4])
print(eightLetters[4:])
print(eightLetters[:4] + eightLetters[4:])
print()

# For non-negative indices, the length of a slice is the difference of the indices,
# if both are within bounds. For example, the length of eightLetters[1:3] is 2.
# Attempting to use an index that is too large will result in an error
# print(eightLetters[42])  # IndexError: string index out of range
# However, out of range slice indexes are handled gracefully when used for slicing.
print(eightLetters[4:42])

# Python strings cannot be changed - they are immutable. Therefore, assigning to an
# indexed position in the string results in an error
eight_letter_word = "abcdefg"
# eight_letter_word[3] = 'q'  # TypeError: 'str' object does not support item assignment

# If you need a different string, you should create a new one
ten_letter_word = eight_letter_word[0:] + 'hijk'
print(ten_letter_word)

# The built-in function len() returns the length of a string:
long_word = 'supercalifragilisticexpialidocious'
print(len(long_word))
print()