"""
To read a file's contents, call the 'read(size)' function, which reads some quantity
of data and returns it as a string (in text mode) or bytes object (in binary mode).
'size' is an optional numeric argument. When size is omitted or negative, the entire
contents of the file will be read and returned; it's your problem if the file is twice
as large as your machine's memory. Otherwise, at most size characters (in text mode)
or size bytes (in binary mode) are read and returned. If the end of the file has been
reached, f.read() will return an empty string.

readline() function reads a single line from the file; a newline character (\n) is
left at the end of the string, and is only omitted on the last line of the file if
the file doesn't end in a newline. This makes the return value unambiguous; if the
readline() function returns an empty string, the end of the file has been reached,
while a blank line is represented by '\n', a string containing only a single newline.

For reading lines from a file, you can loop over the file object. This is memory
efficient, fast, and leads to simple code:
>>> d_file = open('another_file')
>>> for line in d_file:
...     print(line, end='')

If you want to read all the lines of a file in a list you can also use 'list(file)'
or call the readlines() function on the file object.

Calling the 'write(string)' function on a file object writes the contents of string
to the file, returning the number of characters written.

Calling the tell() function on a file returns an integer giving the file object's
current position in the file represented as number of bytes from the beginning of the
file when in binary mode and an opaque number when in text mode.

To change the file object's position, call the 'seek(offset, whence)' function.
The position is computed from adding offset to a reference point; the reference point
is selected by the whence argument. A whence value of 0 measures from the beginning of
the file, 1 uses the current file position, and 2 uses the end of the file as the
reference point. whence can be omitted and defaults to 0, using the beginning of
the file as the reference point.
"""
