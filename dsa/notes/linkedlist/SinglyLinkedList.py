from dsa.notes.stack.Stack import Stack


class SingleNode:
    """Node for a Single Linked List"""

    def __init__(self, data):
        self.value = data
        self.next = None

    def __repr__(self):
        return f"{self.value}"


class SinglyLinkedList:
    """A Single Linked List"""

    def __init__(self):
        self.head = None

    def __iter__(self):
        """
        This function is intended for iterators to access
        and iterate through data inside linked list.
        """
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __len__(self):
        """Return length of the linked list"""
        return len(tuple(iter(self)))

    def __repr__(self):
        """String representation of a Linked List"""
        return "->".join([str(item) for item in self])

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
        current.value = data

    def isEmpty(self) -> bool:
        """Check if Linked List is empty"""
        return self.head is None

    def insertNth(self, index: int, data):
        """Insert a node at a given index"""
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        newNode = SingleNode(data)
        if self.head is None:  # inserting in an empty list
            self.head = newNode
        elif index == 0:  # inserting at head
            newNode.next = self.head
            self.head = newNode
        else:  # inserting at any other index
            currentNode = self.head
            for _ in range(index - 1):
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode

    def deleteNth(self, index: int):
        """Delete a node at a given index"""
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range.")
        if index == 0:  # deleting at head
            self.head = self.head.next
            return
        else:  # deleting at any other index
            currentNode = self.head
            currentIndex = 0
            # find node before the one to be deleted
            while currentIndex < index - 1:
                currentNode = currentNode.next
                currentIndex += 1
            nodeAfterDeletedOne = currentNode.next.next
            currentNode.next = nodeAfterDeletedOne

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
        return currentNode  # or currentNode.value

    def push(self, data):
        """Insert a node at the beginning of the Linked List
        another name is 'insert_head()' function'"""
        self.insertNth(0, data)

    def append(self, data):
        """Insert a node at the end of the Linked List
        another name is 'insert_tail()' function"""
        self.insertNth(len(self), data)

    def deleteHead(self):
        """Delete Node at the beginning of the Linked List"""
        self.deleteNth(0)

    def deleteTail(self):
        """Delete Node at the end of the Linked List"""
        self.deleteNth(len(self) - 1)

    # ----------------------------------------------------
    # BELOW ARE SPECIAL FUNCTIONS FOR A SINGLY LINKED LIST
    # ----------------------------------------------------
    def print(self):
        """Prints all elements of a Linked List"""
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=' ')
            currentNode = currentNode.next

    def printReverse(self):
        """
        Reverse the list. Prints all elements in reverse.
        I IMPLEMENTED THIS ALGORITHM MYSELF USING A LIST
        """
        currentNode = self.head
        nodes = []
        while currentNode is not None:
            nodes.append(currentNode)
            currentNode = currentNode.next
        for i in range(len(self) - 1, -1, -1):
            print(nodes[i], end=' ')

    def printReverse2(self):
        """Reverse the list. Prints all element in reverse
        THIS IMPLEMENTATION USES A STACK"""
        stack = Stack()
        currentNode = self.head
        while currentNode is not None:
            stack.push(currentNode)
            currentNode = currentNode.next
        while stack.size() > 0:
            print(stack.pop(), end=' ')

    def lastElement(self):
        """Returns the last element in the list"""
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        return currentNode  # or currentNode.data

    def getMiddleNode(self):
        """
        Returns the node at the middle index.
        In the while loop, you bind the next node to fast. If there's a next node,
        you update fast to the next node of fast, effectively traversing down the
        list twice. slow is updated only once.
        This is also known as the RUNNER TECHNIQUE.
        O(n) time complexity since the list is traversed in a single pass.
        """
        slowPointer = self.getNodeAtIndex(0)  # or self[0]
        fastPointer = self.getNodeAtIndex(0)  # or self[0]
        while fastPointer is not None:
            fastPointer = fastPointer.next
            if fastPointer is not None:
                fastPointer = fastPointer.next
                slowPointer = slowPointer.next
        # when fast is at the last index, slow will be at the middle index
        return slowPointer


# -----------------------------------------------
# SPECIAL FUNCTIONS FOR A SINGLY LINKED LIST [continued]
# -----------------------------------------------
def mergeTwoLists(head_1: SingleNode, head_2: SingleNode):
    """
    Function to merge two sorted linked lists.
    @:return: the head of the merged linked list
    """
    dummyNode = SingleNode(None)
    tail = dummyNode
    while True:
        if head_1 is None:
            tail.next = head_2
            break
        if head_2 is None:
            tail.next = head_1
            break
        if head_1.value <= head_2.value:
            tail.next = head_1
            head_1 = head_1.next
        else:
            tail.next = head_2
            head_2 = head_2.next
        tail = tail.next
    return dummyNode.next
