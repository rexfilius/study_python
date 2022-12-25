"""
Most container objects can be looped over using a for statement

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
   print(char)
for line in open("myfile.txt"):
    print(line, end='')

This style of access is clear, concise, and convenient. The use of iterators pervades
and unifies Python. Behind the scenes, the for statement calls iter() on the container
object. The function returns an iterator object that defines the method __next__()
which accesses elements in the container one at a time.

When there are no more elements, __next__() raises a StopIteration exception which
tells the for loop to terminate. You can call the __next__() method using the next()
built-in function
"""
street_names = ['Miyaki', 'Alonge', 'Ayoola', 'Ireku']
iterate = iter(street_names)
print(iterate)

print(next(iterate))
print(next(iterate))
print(next(iterate))
print(next(iterate))
# print(next(iterate))  # StopIterationError
