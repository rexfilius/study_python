# SPECIAL PARAMETERS
# By default, arguments may be passed to a Python function either by position
# or explicitly by keyword. For readability and performance, it makes sense to
# restrict the way arguments can be passed so that a developer need only look at
# the function definition to determine if items are passed by position,
# by position or keyword, or by keyword.

# A function definition may look like the one below where / and * are optional.
# If used, these symbols indicate the kind of parameter by how the arguments
# may be passed to the function: positional-only, positional-or-keyword,
# and keyword-only. Keyword parameters are also referred to as named parameters
def spec_func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass


# pos1, pos2 = Positional only
# pos_or_kwd = Positional or Keyword
# kwd1, kwd2 = Keyword only


"""
Positional-or-Keyword Arguments
If / and * are not present in the function definition, arguments may be passed to a
function by position or by keyword.

Positional-Only Parameters
It is possible to mark certain parameters as  positional-only. If positional-only, 
the parameters’ order matters, and the parameters cannot be passed by keyword. 
Positional-only parameters are placed before a / (forward-slash). The / is used to 
logically separate the positional-only parameters from the rest of the parameters. 
If there is no / in the function definition, there are no positional-only parameters.

Parameters following the / may be positional-or-keyword or keyword-only.

Keyword-Only Arguments
To mark parameters as keyword-only, indicating the parameters must be passed by keyword
argument, place an * in the arguments list just before the first keyword-only parameter.
"""

"""
GUIDANCE ON PARAMETERS:

[1] Use positional-only if you want the name of the parameters to not be available to
the user. This is useful when parameter names have no real meaning, if you want to 
enforce the order of the arguments when the function is called or if you need to take
some positional parameters and arbitrary keywords.

[2] Use keyword-only when names have meaning and the function definition is more 
understandable by being explicit with names or you want to prevent users relying on 
the position of the argument being passed.

[3] For an API, use positional-only to prevent breaking API changes if the parameter's
name is modified in the future.
"""
