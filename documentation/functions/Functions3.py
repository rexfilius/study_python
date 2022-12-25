# NOTE: For Default Argument Values in functions, The default value is evaluated
# only once. This makes a difference when the default is a mutable object such
# as a list, dictionary, or instances of most classes.
# e.g. the function below accumulates the arguments passed to it on subsequent calls.
def random_func(a, aList=[]):
    aList.append(a)
    return aList


print(random_func(1))
print(random_func(2))
print(random_func(3))


# If you don't want the default to be shared between subsequent calls,
# you can write the function like this instead.
def random_func_2(a, aList=None):
    if aList is None:
        aList = []
    aList.append(a)
    return aList


print(random_func_2(1))
print(random_func_2(2))
print(random_func_2(3))
