"""
Programs may name their own exceptions by creating a new exception class. Exceptions
should typically be derived from the Exception class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are
usually kept simple, often only offering a number of attributes that allow information
about the error to be extracted by handlers for the exception.

When creating a module that can raise several distinct errors, a common practice is to
create a base class for exceptions defined by that module, and subclass that to create
specific exception classes for different error conditions.

Most exceptions are defined with names that end in 'Error', similar to the naming of
the standard exceptions. Many standard modules define their own exceptions to report
errors that may occur in functions they define.
"""


class SomeError(Exception):
    """Base class for exceptions in this module."""
    pass


class SomeInputError(SomeError):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class SomeTransitionError(SomeError):
    """Raised when an operation attempts a state transition that's not allowed
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
