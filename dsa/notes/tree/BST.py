# -------------------------------------------------------------
# TOP LEVEL FUNCTIONS FOR A BINARY SEARCH TREE
# -------------------------------------------------------------
from queue import SimpleQueue
from dsa.notes.tree.BSTree import BSTree


def isEmptyBST(node: BSTree) -> bool:
    """Checks if a BST is empty"""
    return node is None


def searchBST(node: BSTree, data):
    """Search for a value in a BST. Return None if not found."""
    if isEmptyBST(node):
        return None
    while node is not None and node.value is not data:
        if data < node.value:
            node = node.left
        else:
            node = node.right
    return node


def searchBSTRecursive(node: BSTree, value):
    """Search for a value in a BST. Return None if not found."""
    if node is None or node.value == value:
        return node
    elif value < node.value:
        return searchBSTRecursive(node.left, value)
    else:  # value > node.value:
        return searchBSTRecursive(node.right, value)


def deleteBST(node: BSTree, data):
    """Deletes a node in a BST and returns it"""
    if node is None:
        return None
    elif data < node.value:
        node.left = deleteBST(node.left, data)
        return node
    elif data > node.value:
        node.right = deleteBST(node.right, data)
        return node
    elif data == node.value:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            node.right = liftNodeBST(node.right, node)
            return node


def liftNodeBST(node: BSTree, nodeToDelete):
    if node.left:
        node.left = liftNodeBST(node.left, nodeToDelete)
        return node
    else:
        nodeToDelete.value = node.value
        return node.right


def bfsBST(node: BSTree):
    queue = SimpleQueue()
    queue.put(node)
    while queue.qsize() > 0:
        currentNode = queue.get()
        print(currentNode.value, end=' ')
        if currentNode.left:
            queue.put(currentNode.left)
        if currentNode.right:
            queue.put(currentNode.right)


def inorderTraverseBST(node: BSTree):
    if node is None:
        return
    inorderTraverseBST(node.left)
    print(node.value, end=', ')
    inorderTraverseBST(node.right)


def preorderTraverseBST(node: BSTree):
    if node is None:
        return
    print(node.value, end=', ')
    preorderTraverseBST(node.left)
    preorderTraverseBST(node.right)


def postorderTraverseBST(node: BSTree):
    if node is None:
        return
    postorderTraverseBST(node.left)
    postorderTraverseBST(node.right)
    print(node.value, end=', ')


# -----------------------------------------------------
# SPECIAL TOP LEVEL FUNCTIONS FOR A BINARY SEARCH TREE
# -----------------------------------------------------
def greatestValueBST(node: BSTree):
    """
    Returns the greatest value in a BST.
    Greatest value will be on the righter side of the root node.
    """
    if node.right is None:
        return node.value
    else:
        return greatestValueBST(node.right)
