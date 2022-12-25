# Any function object that is a class attribute defines a method for instances
# of that class. It is not necessary that the function definition is textually
# enclosed in the class definition: assigning a function object to a local
# variable in the class is also ok.
# Note that this practice usually only serves to confuse the reader of a program.
def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# Now f, g and h are all attributes of class C that refer to function objects,
# and consequently they are all methods of instances of C — h being exactly
# equivalent to g


# Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)