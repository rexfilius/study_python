class Stack:
    """Implementation of a Stack using a List"""

    def __init__(self):
        self.storage = []

    def __bool__(self) -> bool:
        """
        Object is considered true if its result is nonzero i.e.
        Stack is considered true if storage is > 0
        """
        return bool(self.storage)

    def __contains__(self, item) -> bool:
        """Checks if an item is in the Stack"""
        return item in self.storage

    def __repr__(self):
        """String representation of a Stack"""
        return str(self.storage)

    def isEmpty(self) -> bool:
        """Check if Stack is empty. Another way is using __len__"""
        return not self.__bool__()

    def size(self) -> int:
        """Return the number of items in the Stack"""
        return len(self.storage)

    def push(self, data):
        """Add an element to the top of the stack"""
        self.storage.append(data)

    def pop(self):
        """Removes an element at the top of the stack and returns it"""
        if self.isEmpty():
            return None
        else:
            return self.storage.pop()

    def peek(self):
        """Peek at the topmost element in the Stack"""
        return self.storage[-1]

    # -----------------------------------------
    # BELOW ARE SPECIAL FUNCTIONS FOR A STACK
    # -----------------------------------------


# -------------------------------------------
# SPECIAL FUNCTIONS FOR A STACK [continued]
# -------------------------------------------
def createStackFromIterable(items) -> Stack:
    """Convert an existing list to a Stack"""
    stack = Stack()
    for item in items:
        stack.push(item)
    return stack
