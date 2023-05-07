"""
Implementation of a Queue using Two Stacks. The idea behind using two stacks
is simple. Whenever you enqueue an element, it goes into the right stack.
When you need to dequeue an element, you reverse the right stack and place it in
the left stack so that you can retrieve the elements using FIFO order.

Queues use FIFO (first in, first out) ordering, meaning the first element that
was added will always be the first one removed. Queues are handy when you need
to maintain the order of your elements to process later.

NOTE: the queue only cares about removal from the front and insertion at the
back. You don't need to know what the contents are in between. If you did,
you'd presumably use an array instead of a Queue.
"""
from dsa.notes.stack_.stack import Stack


class QueueOnStack:

    def __init__(self):
        self.outStack = Stack()  # left stack
        self.inStack = Stack()  # right stack

    def __len__(self):
        return self.outStack.size() + self.inStack.size()

    def __repr__(self):
        return f"Left/Out: {self.outStack} Right/In: {self.inStack}"

    def isEmpty(self) -> bool:
        return self.outStack.size() == 0 and self.inStack.size() == 0

    def enqueue(self, data):
        """
        Add element at the back of the queue.
        implementation - push data to the right/in stack.
        """
        self.inStack.push(data)

    def dequeue(self):
        """
        Remove and return element at the front of the queue
        implementation - pop data on the left/out stack
        """
        if self.outStack.isEmpty():
            self.transferElements()
        return self.outStack.pop()

    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        """
        if self.outStack.isEmpty():
            self.transferElements()
        return self.outStack.peek()

    def transferElements(self):
        """
        Function to transfer the elements from the right/in stack into the
        left/out stack. That needs to happen whenever the left stack is empty.
        """
        while self.inStack.size() > 0:
            self.outStack.push(self.inStack.pop())

    # -----------------------------------------
    # BELOW ARE SPECIAL FUNCTIONS FOR A QUEUE
    # -----------------------------------------

# -------------------------------------------
# SPECIAL FUNCTIONS FOR A QUEUE [continued]
# -------------------------------------------
