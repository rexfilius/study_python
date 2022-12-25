from dsa_courses.jayWengorw.tree.BST import TreeNode, \
    inorderTraverse, postorderTraverse, preorderTraverse

nodeV25 = TreeNode(25)
nodeV75 = TreeNode(75)
nodeV10 = TreeNode(10)
nodeV33 = TreeNode(33)
nodeV56 = TreeNode(56)
nodeV89 = TreeNode(89)
nodeV4 = TreeNode(4)
nodeV11 = TreeNode(11)
nodeV30 = TreeNode(30)
nodeV40 = TreeNode(40)
nodeV52 = TreeNode(52)
nodeV61 = TreeNode(61)
nodeV82 = TreeNode(82)
nodeV95 = TreeNode(95)
rootNode = TreeNode(50, left=nodeV25, right=nodeV75)

nodeV25.leftChild = nodeV10
nodeV25.rightChild = nodeV33
nodeV10.leftChild = nodeV4
nodeV10.rightChild = nodeV11
nodeV33.leftChild = nodeV30
nodeV33.rightChild = nodeV40

nodeV75.leftChild = nodeV56
nodeV75.rightChild = nodeV89
nodeV56.leftChild = nodeV52
nodeV56.rightChild = nodeV61
nodeV89.leftChild = nodeV82
nodeV89.rightChild = nodeV95

# inorderTraverse(rootNode)
# print()
# print('greatest value in BST-', greatesValueInBST(rootNode))

nodeL01 = TreeNode('Great')
nodeL02 = TreeNode('Robinson')
nodeL11 = TreeNode('Alice')
nodeL12 = TreeNode('Lord')
nodeL13 = TreeNode('Pride')
nodeL14 = TreeNode('The-Odyssey')
nodeL00 = TreeNode('Moby', left=nodeL01, right=nodeL02)
nodeL01.leftChild = nodeL11
nodeL01.rightChild = nodeL12
nodeL02.leftChild = nodeL13
nodeL02.rightChild = nodeL14

inorderTraverse(nodeL00)
print()
preorderTraverse(nodeL00)
print()
postorderTraverse(nodeL00)

