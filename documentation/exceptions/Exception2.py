"""
A try statement may have more than one except clause, to specify handlers
for different exceptions. At most one handler will be executed. Handlers only
handle exceptions that occur in the corresponding try clause, not in other
handlers of the same try statement. An except clause may name multiple
exceptions as a parenthesized tuple.

... except (RuntimeError, TypeError, NameError):
...     pass
"""


# A class in an except clause is compatible with an exception if it is the same class
# or a base class thereof (but not the other way around — an except clause listing a
# derived class is not compatible with a base class).
# e.g the code below will print B, C, D in that order.
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

"""
Note that if the except clauses were reversed (with except B first), it would have 
printed B, B, B — the first matching except clause is triggered.
"""
