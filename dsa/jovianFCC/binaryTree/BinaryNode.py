class BinaryNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def sizeofTree(self):
        """counts the number of nodes in a binary tree"""
        if self is None:
            return 0
        return 1 + BinaryNode.sizeofTree(self.left) + \
               BinaryNode.sizeofTree(self.right)

    def height(self):
        if self is None:
            return 0
        return 1 + max(BinaryNode.height(self.left), BinaryNode.height(self.right))

    def traverseInOrder(self):
        if self is None:
            return []
        return BinaryNode.traverseInOrder(self.left) + [self.key] + \
               BinaryNode.traverseInOrder(self.right)

    def traversePreOrder(self):
        """My implementation. It worked, I cross-checked with my Kotlin code"""
        if self is None:
            return []
        return [self.key] + BinaryNode.traversePreOrder(self.left) + \
               BinaryNode.traversePreOrder(self.right)

    def traversePostOrder(self):
        """My implementation. It worked, I cross-checked with my Kotlin code"""
        if self is None:
            return []
        return BinaryNode.traversePostOrder(self.left) + \
               BinaryNode.traversePostOrder(self.right) + [self.key]

    def displayKeys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '--')
            return
        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
        # If the node has children
        BinaryNode.displayKeys(self.right, space, level + 1)
        print(space * level + str(self.key))
        BinaryNode.displayKeys(self.left, space, level + 1)

    def toTuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return BinaryNode.toTuple(self.left), self.key, BinaryNode.toTuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.toTuple())

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def parseTuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = BinaryNode(data[1])
            node.left = BinaryNode.parseTuple(data[0])
            node.right = BinaryNode.parseTuple(data[2])
        else:
            node = BinaryNode(data)
        return node
    # END OF CLASS - TreeNode


# TOP LEVEL FUNCTIONS FOR A BINARY TREE
def displayKeysfn(node, space='\t', level=0):
    # If the node is empty
    if node is None:
        print(space * level + '--')
        return
    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    # If the node has children
    displayKeysfn(node.right, space, level + 1)
    print(space * level + str(node.key))
    displayKeysfn(node.left, space, level + 1)


def sizeofTreefn(node):
    """counts the number of nodes in a binary tree"""
    if node is None:
        return 0
    return 1 + sizeofTreefn(node.left) + sizeofTreefn(node.right)


def removeNone(nums):
    return [x for x in nums if x is not None]


def isBST(node):
    """Checks whether a binary tree is a BST"""
    if node is None:
        return True, None, None

    isBSTleft, minKeyLeft, maxKeyLeft = isBST(node.left)
    isBSTright, minKeyRight, maxKeyRight = isBST(node.right)

    isBSTnode = (isBSTleft and isBSTright and
                 (maxKeyLeft is None or node.key > maxKeyLeft) and
                 (minKeyRight is None or node.key < minKeyRight))

    minKey = min(removeNone([minKeyLeft, node.key, minKeyRight]))
    maxKey = max(removeNone([maxKeyLeft, node.key, maxKeyRight]))

    return isBSTnode, minKey, maxKey
