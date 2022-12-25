"""
The raise statement allows an optional from which enables chaining exceptions

# exc must be exception instance or None.
>>> raise RuntimeError from exc

This can be useful when you are transforming exceptions
>>> def func():
...     raise IOError
...
>>> try:
...     func()
... except IOError as exc:
...     raise RuntimeError('Failed to open database') from exc

Exception chaining happens automatically when an exception is raised inside an except
or finally section. Exception chaining can be disabled by using 'from None' idiom
>>> try:
...    open('database.sqlite')
... except OSError:
...    raise RuntimeError from None
"""