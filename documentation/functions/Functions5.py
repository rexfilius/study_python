# When a final formal parameter of the form **name is present, it receives
# a dictionary containing all keyword arguments except for those corresponding
# to a formal parameter. This may be combined with a formal parameter of the form
# *name which receives a tuple containing the positional arguments beyond
# the formal parameter list. (*name must occur before **name.)
# e.g if we define a function like this:
def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# It could be called like this:
cheese_shop("Limburger", "It's very funny, sir.",
            "It's really very, VERY funny, sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")
