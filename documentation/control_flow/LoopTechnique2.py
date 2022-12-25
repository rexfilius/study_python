"""
The conditions used in 'while' and 'if' statements can contain any operators,
not just comparisons.

The comparison operators 'in' and 'not in' check whether a value occurs (does not occur)
in a sequence.

The operators 'is' and 'is not' compare whether two objects are really the same object.

All comparison operators have the same priority, which is lower than that of all
numerical operators.

Comparisons can be chained. e.g. a < b == c tests whether a is less than b
and moreover b equals c.

Comparisons may be combined using the Boolean operators 'and' and 'or', and the outcome
of a comparison (or of any other Boolean expression) may be negated with 'not'.
These have lower priorities than comparison operators; between them, 'not' has
the highest priority and or the lowest, so that A and not B or C is equivalent to
(A and (not B)) or C.
As always, parentheses can be used to express the desired composition.

The Boolean operators 'and' and 'or' are so-called short-circuit operators:
their arguments are evaluated from left to right, and evaluation stops as soon as
the outcome is determined. e.g. if A and C are true but B is false, A and B and C
does not evaluate the expression C. When used as a general value and not as a Boolean,
the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression
to a variable. e.g
"""
str1, str2, str3 = '', 'Trondheim', 'Hammer Dance'
non_null = str1 or str2 or str3
print(non_null)

"""
NOTE: In Python, unlike C, assignment inside expressions must be done explicitly 
with the 'walrus operator :=' This avoids a common class of problems encountered in 
C programs: typing = in an expression when == was intended.
"""
