from pprint import pformat
from queue import SimpleQueue


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __repr__(self):
        if self.leftChild is None and self.rightChild is None:
            return str(self.value)
        return pformat({f"{self.value}": f"Left:({self.leftChild}) Right:({self.rightChild})"}, indent=1)

    def insertLeft(self, data):
        """
        If the current node doesn't have a left child, we just create a new node and set it to the current
        node’s left_child.
        If it does have the left child, we create a new node and put it in the current left child’s place.
        Allocate this left child node to the new node’s left child.
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(data)
        else:
            newNode = BinaryTree(data)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode

    def insertRight(self, data):
        if self.rightChild is None:
            self.rightChild = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.rightChild = self.rightChild
            self.rightChild = new_node

    def preOrder(self):
        """
        Print the value of the node.
        Go to the left child and print it. This is if, and only if, it has a left child.
        Go to the right child and print it. This is if, and only if, it has a right child.
        """
        print(self.value)
        if self.leftChild is not None:
            self.leftChild.preOrder()
        if self.rightChild is not None:
            self.rightChild.preOrder()

    def inOrder(self):
        """
        Go to the left child and print it. This is if, and only if, it has a left child.
        Print the node's value.
        Go to the right child and print it. This is if, and only if, it has a right child.
        """
        if self.leftChild is not None:
            self.leftChild.inOrder()
        print(self.value)
        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):
        """
        Go to the left child and print it. This is if, and only if, it has a left child.
        Go to the right child and print it. This is if, and only if, it has a right child.
        Print the node's value.
        """
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print(self.value)

    def bfs(self):
        """
        First add the root node into the queue with the put method.
        Iterate while the queue is not empty.
        Get the first node in the queue, and then print its value.
        Add both left and right children into the queue (if the current node has children).
        Done. We will print the value of each node, level by level, with our queue helper.
        """
        queue = SimpleQueue()
        queue.put(self)
        while queue.qsize() > 0:  # while it is not empty
            currentNode = queue.get()
            print(currentNode.value, end=' ')
            if currentNode.leftChild:
                queue.put(currentNode.leftChild)
            if currentNode.rightChild:
                queue.put(currentNode.rightChild)
