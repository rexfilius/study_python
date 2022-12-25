# open() returns a file object, and is most commonly used with two arguments:
# open(filename, mode).
my_file = open('work_file', 'w')

"""
The first argument is a string containing the filename. The second argument is another
string containing a few characters describing the way in which the file will be used.
mode can be 'r' when the file will only be read, 
'w' for only writing (an existing file with the same name will be erased), and 
'a' opens the file for appending; any data written to the file is automatically added
to the end. 
'r+' opens the file for both reading and writing. The mode argument is optional.
'r' will be assumed if it's omitted.

Normally, files are opened in text mode, that means, you read and write strings from
and to the file, which are encoded in a specific encoding. If encoding is not specified,
the default is platform dependent. 'b' appended to the mode opens the file in 
binary mode: now the data is read and written in the form of bytes objects. 
This mode should be used for all files that don't contain text.

In text mode, the default when reading is to convert platform-specific line endings 
(\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is 
to convert occurrences of \n back to platform-specific line endings. 
This behind-the-scenes modification to file data is fine for text files, but will 
corrupt binary data like that in JPEG or EXE files.
Be very careful to use binary mode when reading and writing such files.
"""

# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes,
# even if an exception is raised at some point. Using with is also much shorter
# than writing equivalent try-finally blocks
with open('work_file') as a_file:
    read_data = a_file.read()

# We can check that the file has been automatically closed
is_file_closed = a_file.closed

"""
If you're not using the with keyword, then you should call the close() function to
close the file and immediately free up any system resources used by it.

WARNING: Calling the write() function without using the with keyword or calling 
the close() function might result in the arguments of the write() function not being
completely written to the disk, even if the program exits successfully.

After a file object is closed, either by a with statement or by calling the close() 
function, attempts to use the file object will automatically fail.
"""
