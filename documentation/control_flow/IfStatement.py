# There can be zero or more elif parts, and the else part is optional. The keyword
# 'elif' is short for 'else if', and is useful to avoid excessive indentation.
# An if … elif … elif … sequence is a substitute for the switch or case statements
# found in other languages.
number = int(input('Please enter an integer: '))
if number < 0:
    print('Negative integer')
elif number == 0:
    print('Integer is zero')
elif number == 1:
    print('Integer is 1')
else:
    print('Integer is greater than 1')
