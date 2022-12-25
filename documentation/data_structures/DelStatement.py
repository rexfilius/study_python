# There is a way to remove an item from a list given its index instead of its
# value: the del statement. This differs from the pop() method which returns a
# value. The del statement can also be used to remove slices from a list
# or clear the entire list
n_list = [-1, 1, 66.25, 333, 333, 1234.5]

del n_list[0]
print(n_list)

del n_list[2:4]
print(n_list)

del n_list[:]
print(n_list)

# del can also be used to delete entire variables:
del n_list
# Referencing the variable name hereafter is an error
# (at least until another value is assigned to it)
# print(n_list)
