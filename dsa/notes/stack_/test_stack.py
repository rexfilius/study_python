from dsa.notes.stack_.stack import Stack

# Create a Stack
stack = Stack()
print('stack -', stack)
print('Is stack empty -', stack.isEmpty(), '\n')

# Push to a Stack
stack.push('a')
stack.push('b')
stack.push('c')
print('stack -', stack)

# Size of a Stack
print('number of items -', stack.size())

# Peek a Stack
print('topmost item -', stack.peek())

# __contains__ function
print("Is 'c' in Stack -", stack.__contains__('c'), '\n')

# Pop a Stack
print('stack - ', stack)
stack.pop()
stack.pop()
print('stack; after popping twice -', stack)
