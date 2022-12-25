"""
Python supports a form of multiple inheritance as well.
A class definition with multiple base classes looks like this:

>>> class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    <statement-N>

For most purposes, in the simplest cases, you can think of the search for attributes
inherited from a parent class as depth-first, left-to-right, not searching twice in the
same class where there is an overlap in the hierarchy. Thus, if an attribute is
not found in DerivedClassName, it is searched for in Base1, then (recursively) in
the base classes of Base1, and if it was not found there, it was searched for in Base2,
and so on.
"""