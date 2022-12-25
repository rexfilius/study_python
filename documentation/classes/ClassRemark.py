# If the same attribute name occurs in both an instance and in a class,
# then attribute lookup prioritizes the instance
class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)  # ans = storage west

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)  # ans = storage east
print()

"""
Data attributes may be referenced by methods as well as by ordinary users ("clients") 
of an object. In other words, classes are not usable to implement pure abstract data
types. In fact, nothing in Python makes it possible to enforce data hiding — 
it is all based upon convention.

Clients should use data attributes with care — clients may mess up invariants 
maintained by the methods by stamping on their data attributes. Note that clients may
add data attributes of their own to an instance object without affecting the validity
of the methods, as long as name conflicts are avoided — 
again, a naming convention can save a lot of headaches here.

NOTE: Often, the first argument of a method is called self. This is nothing more than
a convention: the name self has absolutely no special meaning to Python. Note, however,
that by not following the convention your code may be less readable to other 
Python programmers.
"""