def fibonacci_1(n: int):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b
    print()


"""
The keyword def introduces a function definition. It must be followed by the function
name and the parenthesized list of formal parameters. The statements that form the body
of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; this 
string literal is the function's documentation string, or docstring. There are tools 
which use docstrings to automatically produce online or printed documentation, or to 
let the user interactively browse through code; it's good practice to include 
docstrings in code that you write, so make a habit of it.

The execution of a function introduces a new symbol table used for the local variables
of the function. More precisely, all variable assignments in a function store the value
in the local symbol table; whereas variable references first look in the local symbol
table, then in the local symbol tables of enclosing functions, then in the global symbol
table, and finally in the table of built-in names. Thus, global variables and variables
of enclosing functions cannot be directly assigned a value within a function 
(unless, for global variables, named in a global statement, or, for variables of 
enclosing functions, named in a nonlocal statement), although they may be referenced.

The actual parameters (arguments) to a function call are introduced in the local symbol
table of the called function when it is called; thus, arguments are passed using call
by value (where the value is always an object reference, not the value of the object).
When a function calls another function, or calls itself recursively, a new local symbol
table is created for that call.

A function definition associates the function name with the function object in the 
current symbol table. The interpreter recognizes the object pointed to by that name as
a user-defined function. Other names can also point to that same function object and 
can also be used to access the function.

Coming from other languages, you might object that fibonacci_1 is not a function but a
procedure since it doesn't return a value. In fact, even functions without a return 
statement do return a value, albeit a rather boring one. 
This value is called None (it's a built-in name).
"""

# calling a function
fibonacci_1(2000)


# It is simple to write a function that returns a list of the numbers of
# the Fibonacci series, instead of printing it.
def fibonacci_2(n: int):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci_2(2000))

"""
The return statement returns with a value from a function. return without an expression
argument returns None. Falling off the end of a function also returns None.

The statement result.append(a) calls a method of the list object result. A method is a
function that 'belongs' to an object and is named 'obj.methodname', where obj is some 
object (this may be an expression), and methodname is the name of a method that is 
defined by the object's type. Different types define different methods.

Methods of different types may have the same name without causing ambiguity. 
(It is possible to define your own object types and methods, using classes) 
The method append() shown in the example is defined for list objects; it adds a new 
element at the end of the list. 
In this example it is equivalent to result = result + [a], but more efficient.
"""
