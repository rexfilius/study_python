import math

# Manual String Formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x * x * x).rjust(4))
print()

# There is another method - str.zfill() - which pads a numeric string on the left
# with zeros. It understands about plus and minus signs.
fill_1 = '12'.zfill(5)
print(fill_1)  # ans = 00012
fill_2 = '-3.14'.zfill(7)
print(fill_2)  # ans = -003.14
fill_3 = '3.14159265359'.zfill(5)
print(fill_3)  # ans = 3.14159265359
print()

# Old string formatting
# The % operator can also be used for string formatting. Given 'string' % values,
# instances of % in string are replaced with zero or more elements of values.
# This operation is commonly known as string interpolation.
print('The value of pi is approximately %5.3f.' % math.pi)
