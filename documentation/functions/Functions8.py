# Small anonymous functions can be created with the lambda keyword.
# Lambda functions can be used wherever function objects are required.
# They are syntactically restricted to a single expression.
# Semantically, they are just syntactic sugar for a normal function definition.
# Like nested function definitions, lambda functions can reference variables
# from the containing scope
def make_incrementor(n):
    return lambda x: x + n


increase_number = make_incrementor(42)
print(increase_number(0))
print(increase_number(1))

# The above example uses a lambda expression to return a function.
# Another use is to pass a small function as an argument.
number_pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
number_pairs.sort(key=lambda pair: pair[1])
print(number_pairs)
print()


# FUNCTION ANNOTATIONS are completely optional metadata information about the types
# used by user-defined functions (see PEP 3107 and PEP 484 for more information).
# ANNOTATIONS are stored in the __annotations__ attribute of the function as a
# dictionary and have no effect on any other part of the function.
# PARAMETER ANNOTATIONS are defined by a colon after the parameter name,
# followed by an expression evaluating to the value of the annotation.
# RETURN ANNOTATIONS are defined by a literal "->", followed by an expression,
# between the parameter list and the colon denoting the end of the def statement.

# The function below has a required argument, an optional argument,
# and the return value annotated
def make_something(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", make_something.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


make_something('bread')
