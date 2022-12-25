from dsa_notes.dsa.heap.HeapMax import HeapMax
from dsa_notes.dsa.heap.HeapMin import HeapMin


class PriorityQueue:
    """Implementation of a priority queue using a max-heap"""

    def __init__(self):
        self.heap = HeapMax()

    def __repr__(self):
        return self.heap.__repr__()

    def __str__(self):
        return self.__repr__()

    def size(self):
        return self.heap.size()

    def isEmpty(self):
        return self.heap.size() == 0

    def enqueue(self, value):
        self.heap.insert(value)

    def dequeue(self):
        self.heap.remove()

    def peek(self):
        self.heap.peek()
