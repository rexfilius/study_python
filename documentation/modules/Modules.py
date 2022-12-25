"""
If you quit from the Python interpreter and enter it again, the definitions you
have made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the
input for the interpreter and running it with that file as input instead.
This is known as "creating a script".

As your program gets longer, you may want to split it into several files for easier
maintenance. You may also want to use a handy function that you've written in several
programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use them in
a script or in an interactive instance of the interpreter. Such a file is called
a module; definitions from a module can be imported into other modules or into the
main module (the collection of variables that you have access to in a script
executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the
module name with the suffix ".py" appended. Within a module, the module's name
(as a string) is available as the value of the global variable "__name__"
"""

# Importing a module. This does not enter the names of the functions defined in
# fibonacci directly in the current symbol table; it only enters the module name
# fibonacci there. Using the module name you can access the functions:
import fibonacci

fibonacci.fib(1000)
print(fibonacci.fib2(100))
print(fibonacci.__name__)

# If you intend to use a function often you can assign it to a local name:
fib_reuse = fibonacci.fib
fib_reuse(1000)
