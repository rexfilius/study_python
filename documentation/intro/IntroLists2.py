# Assignment to slices is also possible, and this can even change the size
# of the list or clear it entirely
lettered_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(lettered_list)

lettered_list[2:5] = ['C', 'D', 'E']
print(lettered_list)

lettered_list[2:5] = []
print(lettered_list)

lettered_list[:] = []
print(lettered_list)
print()

# The built-in function len() also applies to lists:
street_names = ['Miyaki', 'Alonge', 'Awolowo', 'Ososa']
print(street_names)
print(len(street_names))
print()

# It is possible to nest lists (create lists containing other lists)
school_boys = ['Bob', 'Ken', 'Jake']
school_girls = ['Kate', 'Alice']
school_student = [school_boys, school_girls]
print(school_student)

print(school_student[0])
print(school_student[1])
print(school_student[0][1])
print(school_student[1][1])
print()

# RANDOM - Fibonacci Series
# The keyword argument 'end' can be used to avoid the newline after the output,
# or end the output with a different string
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a + b
