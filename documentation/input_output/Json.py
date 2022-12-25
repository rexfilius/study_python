"""
Strings can easily be written to and read from a file. Numbers take a bit more effort,
since the read() method only returns strings, which will have to be passed to a function
like int(), which takes a string like '123' and returns its numeric value 123.

When you want to save more complex data types like nested lists and dictionaries,
parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data
types to files, Python allows you to use the popular data interchange format called
JSON (JavaScript Object Notation).

The standard module called json can take Python data hierarchies, and convert them to
string representations; this process is called SERIALIZING. Reconstructing the data
from the string representation is called DESERIALIZING. Between serializing and
deserializing, the string representing the object may have been stored in a file or
data, or sent over a network connection to some distant machine.
"""

# If you have an object x, you can view its JSON string representation
# with a simple line of code
import json

xx = [1, 'simple', 'list']
xx_json = json.dumps(xx)
print(xx_json)