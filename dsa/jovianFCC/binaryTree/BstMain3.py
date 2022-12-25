from dsa_courses.jovianFCC.binaryTree.BinaryNode \
    import BinaryNode, isBST

# example from the Jovian course video
rootNode = BinaryNode(2)
three = BinaryNode(3)
one = BinaryNode(1)
five = BinaryNode(5)
three2 = BinaryNode(3)
four = BinaryNode(4)
six = BinaryNode(6)
seven = BinaryNode(7)
eight = BinaryNode(8)

rootNode.left = three
rootNode.right = five
three.left = one
five.left = three2
five.right = seven
three2.right = four
seven.left = six
seven.right = eight

print(rootNode.displayKeys())
print('height-', rootNode.height())
print('size-', rootNode.sizeofTree())

print(isBST(rootNode))
