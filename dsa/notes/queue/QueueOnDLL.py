"""
DLLs have immediate access to both the front and end of the list, they can insert
data on either side at O(1) as well as delete data on either side at O(1).
This makes DLLs a perfect underlying data structure for a queue.
"""
from dsa.notes.linkedlist.DoublyLinkedList import DoublyLinkedList


class QueueOnDLL:

    def __init__(self):
        self.list = DoublyLinkedList()

    def __len__(self) -> int:
        return len(self.list)

    def __repr__(self):
        return self.list.__repr__()

    def __str__(self):
        return self.__repr__()

    def isEmpty(self) -> bool:
        return len(self.list) == 0

    def enqueue(self, element):
        """
        Add element at the back of the queue.
        Implementation - add element at the tail of the DLL.
        O(1) Time.
        """
        self.list.append(element)

    def dequeue(self):
        """
        Remove element at the front of the queue.
        Implementation - remove element at the head of the DLL.
        O(1) Time.
        """
        if self.isEmpty():
            return None
        else:
            self.list.deleteHead()

    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        O(1) Time.
        """
        if self.list.head is None:
            return None
        else:
            return self.list.head  # or self.list[0]
