# Numbers: the operators +, -, *, / work just like in most other languages,
# parentheses () - can be used for grouping
an_addition = 2 + 2
print(f"2 + 2 = {an_addition}")

a_division = 8 / 5  # always returns a floating point number
print(f"8 / 5 = {a_division}")

# Integer numbers have type 'int', the ones with fractional part have type 'float'
# Division (/) always returns a float. To do floor division and get an integer result
# (discarding any fractional result) you can use the // operator.
# to calculate the remainder you can use '%'
floor_division = 17 // 3
print(f"17 // 3 = {floor_division}")

remainder_division = 17 % 3
print(f"17 % 3 = {remainder_division}")

# With Python, it is possible to use the ** operator to calculate powers
power_of_5 = 5 ** 2
print(f"5 raised to power 2 = {power_of_5}")

# The equal sign (=) is used to assign a value to a variable
width = 30
height = 40
print(f"Area is width x height = {width * height}")

# There is full support for floating point; operators with mixed type operands
# convert the integer operand to floating point:
random_math = 4 * 3.75 - 1
print(f"4 * 3.75 - 1 = {random_math}")

# In addition to int and float, Python supports other types of numbers,
# such as Decimal and Fraction. Python also has built-in support for complex numbers,
# and uses the 'j' or 'J' suffix to indicate the imaginary part (e.g. 3+5j).
