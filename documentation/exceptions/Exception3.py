"""
The last except clause may omit the exception name(s), to serve as a wildcard.
Use this with extreme caution, since it is easy to mask a real programming error
in this way! It can also be used to print an error message and then re-raise the
exception (allowing a caller to handle the exception as well)
"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

"""
The try…except statement has an optional else clause, which, when present, must follow
all except clauses. It is useful for code that must be executed if the try clause 
does not raise an exception.

The use of the else clause is better than adding additional code to the try clause 
because it avoids accidentally catching an exception that wasn't raised by the code 
being protected by the try…except statement.
"""
for arg in sys.argv[1:]:
    try:
        f_file = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f_file.readlines()), 'lines')
        f_file.close()
