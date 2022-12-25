# Besides numbers, Python can also manipulate strings, which can be expressed in
# several ways. They can be enclosed in single quotes or double quotes
# with the same result. '\' can be used to escape quotes.
single_quote_string = 'a single quote string'
double_quote_string = "a double quote string"
escape_in_single_quote = 'He doesn\'t dance'
escape_in_single_quote_2 = '"Yes," they said.'
escape_in_double_quote = "he doesn't dance"
escape_in_double_quote_2 = "\"Yes,\" they said."

# If you don't want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote
raw_directory = "C:\some\name"
print(raw_directory)
raw_directory_2 = r"C:\some\name"
print(raw_directory_2)

# String literals can span multiple lines. One way is using triple-quotes: """..."""
# or '''...'''. End of lines are automatically included in the string,
# but it's possible to prevent this by adding a \ at the end of the line.
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated with the '+' operator, and repeated with '*'
string_concat = 3 * 'ha' + 'LOL'
print(string_concat)

# Two or more string literals (i.e. the ones enclosed between quotes) next to each
# other are automatically concatenated.
say = 'w' 'tf'
print(say)

long_text = ('Put several strings within parentheses '
             'to have them joined together.')
print(long_text)

# If you want to concatenate variables or a variable and a literal, use '+'
cus = 'wtf'
cus_Bob = cus + ' Bob'
print(cus_Bob)
