class QueueOnList:
    """Implementation of a Queue using a List"""

    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def isEmpty(self) -> bool:
        return len(self.list) == 0

    def enqueue(self, data):
        """
        Add element at the back of the queue.
        Implementation - add element at the end of the List
        """
        self.list.append(data)

    def dequeue(self):
        """
        Remove element at the front of the queue.
        Implementation - remove element at index 0 of the List
        """
        if self.isEmpty():
            return None
        else:
            self.list.pop(0)

    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        """
        return self.list[0]
