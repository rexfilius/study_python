# Storing Key-Value Pairs using BSTs
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# TOP LEVEL FUNCTIONS FOR A BST
def insertNode(node, key, value):
    """
    Inserts a new node into a BST.
    1. Starting from the root node, compare the key to be inserted with
    the current node's key
    2. If the key is smaller, we recursively insert in the left subtree
    (if it exists), or attach it as the left child if no left subtree exists
    3. if the key is larger, we recursively insert in the right subtree
    (if it exits) or attach it as the right child if no right subtree exists.
    The order of insertion of nodes affects the structure of the tree,
    which could result in an unbalanced tree
    """
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insertNode(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insertNode(node.right, key, value)
        node.right.parent = node
    return node


def findNode(node, key):
    """Finds and returns a Node"""
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return findNode(node.left, key)
    if key > node.right:
        return findNode(node.right, key)


def updateNode(node, key, value):
    """Update the value associated with a given key in a BST"""
    target = findNode(node, key)
    if target is not None:
        target.value = value


def listAllNodes(node):
    """
    Retrieves all the key-value pairs in a BST in the sorted order
    of keys. Same as inorder traversal.
    """
    if node is None:
        return []
    return listAllNodes(node.left) + [(node.key, node.value)] \
           + listAllNodes(node.right)


def isBalanced(node):
    """
    Function to check if a binary tree or BST is balanced.
    1. Ensure that the left subtree is balanced
    2. Ensure that the right subtree is balanced
    3. Ensure that the difference between heights of left subtree and
    right subtree is not more than 1
    """
    if node is None:
        return True, 0
    balancedLeft, heightLeft = isBalanced(node.left)
    balancedRight, heightRight = isBalanced(node.right)

    balanced = balancedLeft and balancedRight and \
               abs(heightLeft - heightRight) <= 1
    height = 1 + max(heightLeft, heightRight)
    return balanced, height


def createBalancedBST(data, lowIndex=0, highIndex=None, parent=None):
    """
    Creates a balanced BST from a sorted list/array of key-value pairs
    """
    if highIndex is None:
        highIndex = len(data) - 1
    if lowIndex > highIndex:
        return None

    midIndex = (lowIndex + highIndex) // 2
    key, value = data[midIndex]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = createBalancedBST(data, lowIndex, midIndex - 1, root)
    root.right = createBalancedBST(data, midIndex + 1, highIndex, root)
    return root


def balanceBst(node):
    """
    Balances an unbalanced binary search tree.
    First, perform an inorder traversal, then create a balanced BST
    from the list of nodes
    """
    return createBalancedBST(listAllNodes(node))
