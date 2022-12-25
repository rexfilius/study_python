"""
Categories of operators in Python::
Arithmetic operators. Assignment operators. Comparison operators.
Logical operators. Identity operators. Membership operators. Bitwise operators.
"""
# ARITHMETIC OPERATORS
print(2 + 5)  # addition
print(5 - 2)  # subtraction
print(2 * 5)  # multiplication
print(5 / 2)  # division, result is a floating-point number
print(5 // 2)  # floor division, result is an integer number
print(5 % 2)  # modulus, result is remainder after division
print(5 ** 2)  # exponent i.e 5 raised to power of 2
print()

# ASSIGNMENT OPERATORS
x_men = 72
x_men += 3
x_men -= 1
x_men *= 5
x_men /= 2
x_men //= 4
x_men %= 4
x_men **= 10
print(x_men)
# x_men &= 4
# x_men |= 8
# x_men ^= 18
# x_men >>= 4
# x_men <<= 7
print()

# COMPARISON OPERATORS
sea = 23
land = 42
print(sea == land)  # equal
print(sea != land)  # not equal
print(sea > land)  # greater than
print(sea < land)  # less than
print(sea >= land)  # greater than or equal to
print(sea <= land)  # less than or equal to
print()

"""
LOGICAL OPERATORS
-> and
Returns True if both statements are true.
e.g. x < 5 and x < 10
-> or
Returns True if one of the statements is true.
e.g x < 5 or x < 4
-> not
Reverse the result, returns False if the result is true.
e.g. not(x < 5 and x < 10)
"""
