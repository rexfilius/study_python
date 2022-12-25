from dsa_courses.jovianFCC.binaryTree.BinaryNode \
    import BinaryNode, isBST

zero = BinaryNode(0)
one = BinaryNode(1)
five = BinaryNode(5)
rootNode = BinaryNode(7)
eight = BinaryNode(8)
nine = BinaryNode(9)

rootNode.left = one
one.left = zero
one.right = five
rootNode.right = nine
nine.left = eight

print(rootNode.displayKeys())
print('height-', rootNode.height())
print('size-', rootNode.sizeofTree())

print(rootNode.traverseInOrder())  # [0, 1, 5, 7, 8, 9]
print(rootNode.traversePreOrder())  # [7, 1, 0, 5, 9, 8]
print(rootNode.traversePostOrder())  # [0, 5, 1, 8, 9, 7]

print(isBST(rootNode))
