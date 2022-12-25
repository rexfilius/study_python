# Generators are a simple and powerful tool for creating iterators. They are written
# like regular functions but use the yield statement whenever they want to return data.
# Each time next() is called on it, the generator resumes where it left off
# (it remembers all the data values and which statement was last executed).
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

"""
Anything that can be done with generators can also be done with class-based iterators.
What makes generators so compact is that the __iter__() and __next__() methods 
are created automatically.

Another key feature is that the local variables and execution state are automatically
saved between calls. This made the function easier to write and much more clear 
than an approach using instance variables like 'self.index' and 'self.data'.

In addition to automatic method creation and saving program state, when generators
terminate, they automatically raise StopIteration. In combination, these features 
make it easy to create iterators with no more effort than writing a regular function.
"""
