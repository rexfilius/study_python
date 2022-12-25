# IDENTITY OPERATORS
# Identity operators are used to compare the objects, not if they are equal, but if
# they are actually the same object, with the same memory location
zz = 43
yy = zz
# is - Returns True if both variables are the same object
print(yy is zz)
# is not - Returns True if both variables are not the same object
print(yy is not zz)
print()

# MEMBERSHIP OPERATORS - are used to test if a sequence is presented in an object.
offenders = ['Ricky', 'Ziggy', 'Harley']
# in - Returns True if a sequence with the specified value is present in the object
print('Ricky' in offenders)
# not in - True if a sequence with the specified value is not present in the object
print('Ricky' not in offenders)

"""
BITWISE OPERATORS - are used to compare (binary) numbers:
-> & AND
Sets each bit to 1 if both bits are 1
-> | OR	
Sets each bit to 1 if one of two bits is 1
-> ^ XOR
Sets each bit to 1 if only one of two bits is 1
-> ~ NOT
Inverts all the bits
-> << Zero fill left shift	
Shift left by pushing zeros in from the right and let the leftmost bits fall off
-> >> Signed right shift	
Shift right by pushing copies of the leftmost bit in from the left, 
and let the rightmost bits fall off
"""
