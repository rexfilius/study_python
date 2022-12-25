class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        return "<-->".join([str(item) for item in self])

    def __len__(self):
        return len(tuple(iter(self)))

    def __getitem__(self, index: int):
        """Indexing Support. Used to get a node at the given index"""
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index: int, data):
        """Indexing Support. Used to change the data of a node at the given index"""
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def isEmpty(self):
        return len(self) == 0

    def insertNth(self, index: int, data):
        """Insert a node at a given index"""
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        newNode = DoubleNode(data)
        if self.head is None:  # inserting in an empty list
            self.head = self.tail = newNode
        elif index == 0:  # inserting at head
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        elif index == len(self):  # inserting at tail
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        else:  # inserting at any other index
            currentNode = self.head
            for i in range(0, index):
                currentNode = currentNode.next
            currentNode.previous.next = newNode
            newNode.previous = currentNode.previous
            newNode.next = currentNode
            currentNode.previous = newNode

    def deleteNth(self, index: int):
        """Delete a node at a given index"""
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range")
        if len(self) == 1:  # deleting a 1-Item list
            self.head = self.tail = None
        elif index == 0:  # deleting at head
            self.head = self.head.next
            self.head.previous = None
        elif index == len(self) - 1:  # deleting at tail; last index
            self.tail = self.tail.previous
            self.tail.next = None
        else:  # deleting at any other index
            currentNode = self.head
            for i in range(0, index):
                currentNode = currentNode.next
            currentNode.next.previous = currentNode.previous
            currentNode.previous.next = currentNode.next

    def getNodeAtIndex(self, index):
        """
        Returns the node at the given index.
        Similar to implementation of __getitem__ function
        """
        currentNode = self.head
        currentIndex = 0
        while currentIndex < index:
            currentNode = currentNode.next
            currentIndex += 1
            if currentNode is None:
                return None
        return currentNode  # or currentNode.data

    def push(self, data):
        """Insert at head"""
        self.insertNth(0, data)

    def append(self, data):
        """Insert at tail"""
        self.insertNth(len(self), data)

    def deleteHead(self):
        """Delete at head"""
        self.deleteNth(0)

    def deleteTail(self):
        """Delete at tail"""
        self.deleteNth(len(self) - 1)

    # ----------------------------------------------------
    # BELOW ARE SPECIAL FUNCTIONS FOR A DOUBLY LINKED LIST
    # ----------------------------------------------------
    def print(self):
        """Prints all elements of a Linked List"""
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=' ')
            currentNode = currentNode.next

    def printReverse(self):
        """
        Reverse the list. Prints all elements in reverse.
        I IMPLEMENTED THIS ALGORITHM MYSELF
        """
        currentNode = self.head
        nodes = []
        while currentNode is not None:
            nodes.append(currentNode)
            currentNode = currentNode.next
        for i in range(len(self) - 1, -1, -1):
            print(nodes[i], end=' ')

    def printReverse2(self):
        """Reverse the list. Print all elements in reverse"""
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        while currentNode != self.head:
            print(currentNode, end=' ')
            currentNode = currentNode.previous
        print(currentNode, end=' ')  # or currentNode.data
