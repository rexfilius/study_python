# Often you'll want more control over the formatting of your output than simply
# printing space-separated values. There are several ways to format output.
# [1] To use formatted string literals, begin a string with 'f' or 'F' before the
# opening quotation mark or triple quotation mark. Inside this string, you can write
# a Python expression between 'curly braces' that can refer to variables/literal values.
ref_year = 2016
ref_event = 'Referendum'
print(f'Results of the {ref_year} {ref_event}')

# [2] The str.format() method of strings requires more manual effort. You'll still use
# curly braces to mark where a variable will be substituted and can provide detailed
# formatting directives, but you'll also need to provide the information to be formatted.
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print_percentage = '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(print_percentage)
print()

# [3] You can do all the string handling yourself by using string slicing and
# concatenation operations to create any layout you can imagine.
# The string type has some methods that perform useful operations for padding strings
# to a given column width.
