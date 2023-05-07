# There are (at least) two distinguishable kinds of errors:
# [1] syntax errors. [2] exceptions.
# Syntax errors, also known as parsing errors, are perhaps the most common kind of
# complaint you get while you are still learning Python.
# Even if a statement or expression is syntactically correct, it may cause an error
# when an attempt is made to execute it. Errors detected during execution are called
# exceptions and are not unconditionally fatal. Most exceptions are not handled by
# programs, however, and result in error messages.

# Handling Exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        print(f"Your number is {x}")
        break
    except ValueError:
        print('"Oops! That was not a valid number. Try again...')


# The try statement works as follows:
# First, the try clause (the statement between the try & except keywords)
# is executed.
# If no exception occurs, the except clause is skipped and execution
# of the try statement is finished.
# If an exception occurs during execution of the try clause, the rest of the clause
# is skipped. Then if its type matches the exception named after the except keyword,
# the except clause is executed, and then execution continues after the try statement.
# If an exception occurs which does not match the exception named in the except clause,
# it is passed on to outer try statements; if no handler is found,
# it is an unhandled exception and execution stops with a message.
