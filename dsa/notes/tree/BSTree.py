"""
A binary search tree, or BST, is a data structure that facilitates fast lookup,
insert and removal operations.
A binary search tree imposes two rules on the binary tree.
1. The value of a left child must be less than the value of its parent.
2. The value of a right child must be >= to the value of its parent.
Binary search trees use this property to save you from performing unnecessary
checking. As a result, lookup, insert and removal have an average time complexity
of O(logN).
By definition, binary search trees can only hold values that are Comparable.
"""
from pprint import pformat
from queue import SimpleQueue


class BSTree:

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    def __str__(self):
        return self.__repr__()

    def isEmpty(self):
        """Returns True if the root node is null"""
        return self.value is None

    def insert(self, data):
        """
        Insert a value into a BST
        """
        newNode = BSTree(data)
        if self.isEmpty():
            self.value = newNode
        if data < self.value:
            if self.left is None:
                self.left = newNode
            else:
                self.left.insert(data)
        elif data > self.value:
            if self.right is None:
                self.right = newNode
            else:
                self.right.insert(data)

    def search(self, data):
        """
        Search for a value in a BSTree, returns None if not found.
        """
        if self.isEmpty():
            return None
        else:
            node = self
            # use lazy evaluation here to avoid NoneType Attribute error
            while node is not None and node.value is not data:
                if data < node.value:
                    node = node.left
                else:
                    node = node.right
            return node

    def searchRecursive(self, data):
        """
        Search for a value in a BST, returns None if not found.
        This method uses recursion.
        """
        node = self
        if node.value is None or node.value == data:
            return node.value
        elif data < node.value:
            node = node.left
            return node.searchRecursive(data)
        else:  # value > node.data
            node = node.right
            return node.searchRecursive(data)

    def delete(self, data):
        """
        Remove and return a node in a BSTree.
        NOT WORKING PERFECTLY YET
        """
        if self.isEmpty():
            return None
        node = self
        if data < node.value:
            node.left = node.left.delete(data)
            return node
        elif data > node.value:
            node.right = node.right.delete(data)
            return node
        elif data == node.value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # self.right = self.right.liftNode(self.value)
                node.right = node.right.liftNode(node)
                return node  # self.value

    def liftNode(self, nodeToDelete):
        if self.left:
            self.left = self.left.liftNode(nodeToDelete)
            return self.value
        else:
            nodeToDelete.value = self.value
            return self.right

    def bfs(self):
        """
        A breadth-first-search traversal of this tree.
        1. Add the root node into the queue with the put method.
        2. Iterate while the queue is not empty.
        3. Get the first node in the queue, and then print its value.
        4. Add both left and right children into the queue.
        (if the current node has children).
        5. Done. We will print the value of each node, level by level,
        with our queue helper.
        """
        queue = SimpleQueue()
        queue.put(self)
        while queue.qsize() > 0:
            currentNode = queue.get()
            print(currentNode.value, end=' ')
            if currentNode.left:
                queue.put(currentNode.left)
            if currentNode.right:
                queue.put(currentNode.right)


# -----------------------------------------
# SPECIAL TOP-LEVEL FUNCTIONS FOR A BSTree
# -----------------------------------------
def inorderBSTree(node: BSTree):
    """In-order traversal of a BSTree"""
    if node is None:
        return
    inorderBSTree(node.left)
    print(node.value, end=' ')
    inorderBSTree(node.right)


def preorderBSTree(node: BSTree):
    """Pre-order traversal of a BSTree"""
    if node is None:
        return
    print(node.value, end=' ')
    preorderBSTree(node.left)
    preorderBSTree(node.right)


def postorderBSTree(node: BSTree):
    """Post-order traversal of a BSTree"""
    if node is None:
        return
    postorderBSTree(node.left)
    postorderBSTree(node.right)
    print(node.value, end=' ')


def heightBSTree(node: BSTree):
    """Returns the integer value that represents the height of a BSTree"""
    if node is None:
        return -1
    else:
        return 1 + max(heightBSTree(node.left), heightBSTree(node.right))


def greatestValueBSTree(node: BSTree):
    """
    Returns the greatest value in a BSTree.
    Greatest value will be on the righter side of the root node
    """
    if node.right is None:
        return node.value
    else:
        return greatestValueBSTree(node.right)


def lca(node, v1, v2):
    """
    Lowest common ancestor of a node
    :param node: a pointer to the root node of a binary search tree
    :param v1: a node value
    :param v2: a node value
    :return: the lowest common ancestor node of the two values given
    """
    if max(v1, v2) < node.value:
        return lca(node.left, v1, v2)
    if min(v1, v2) > node.value:
        return lca(node.right, v1, v2)
    return node
