class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right


def searchBST(searchValue, node: TreeNode):
    """Searching a BST"""
    if node is None or node.value == searchValue:
        return node
    elif searchValue < node.value:
        return searchBST(searchValue, node.leftChild)
    else:  # searchValue > node.value
        return searchBST(searchValue, node.rightChild)


def insertBST(value, node: TreeNode):
    """Insertion in a BST"""
    if value < node.value:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insertBST(value, node.leftChild)
    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insertBST(value, node.rightChild)


def deleteBST(value, node: TreeNode):
    if node is None:
        return None
    elif value < node.value:
        node.leftChild = deleteBST(value, node.leftChild)
        return node
    elif value > node.value:
        node.rightChild = deleteBST(value, node.rightChild)
        return node
    elif value == node.value:
        if node.leftChild is None:
            return node.rightChild
        elif node.rightChild is None:
            return node.leftChild
        else:
            node.rightChild = liftNode(node.rightChild, node)
            return node


def liftNode(node, nodetoDelete):
    if node.leftChild:
        node.leftChild = liftNode(node.leftChild, nodetoDelete)
        return node
    else:
        nodetoDelete.value = node.value
        return node.rightChild


def inorderTraverse(node: TreeNode):
    """Inorder traversal and print the value of the node. O(N) time."""
    if node is None:
        return
    inorderTraverse(node.leftChild)
    print(node.value, end=', ')
    inorderTraverse(node.rightChild)


def preorderTraverse(node: TreeNode):
    if node is None:
        return
    print(node.value, end=', ')
    preorderTraverse(node.leftChild)
    preorderTraverse(node.rightChild)


def postorderTraverse(node: TreeNode):
    if node is None:
        return
    postorderTraverse(node.leftChild)
    postorderTraverse(node.rightChild)
    print(node.value, end=', ')


def greatesValueInBST(node: TreeNode):
    """
    Exercise: returns the greatest value in a BST.
    Greatest value will be on the righter side of the root node
    """
    if node.rightChild is None:
        return node.value
    else:
        return greatesValueInBST(node.rightChild)
