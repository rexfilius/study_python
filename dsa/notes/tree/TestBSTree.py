from dsa_notes.dsa.tree.BSTree import BSTree, inorderBSTree, \
    preorderBSTree, postorderBSTree, heightBSTree, greatestValueBSTree

a1 = (8, 3, 6, 1, 10, 14, 13, 4, 7)
a2 = [10, 20, 8, 12, 17, 25, 19]

# Creating and Inserting into a Binary Search Tree
bst = BSTree(8)
bst.insert(3)
bst.insert(6)
bst.insert(1)
bst.insert(10)
bst.insert(14)
bst.insert(13)
bst.insert(4)
bst.insert(7)

bst2 = BSTree(15)
for number in a2:
    bst2.insert(number)

print('BST-1', bst)
print('BST-2', bst2, '\n')

# Breadth-First Search on a BST
print("::BST-1.", bst.bfs())
print("::BST-2.", bst2.bfs(), '\n')

# Searching in a BST
print('search 5 in BST-1 =', bst.search(5))
print('search 10 in BST-1 =', bst.search(10))
print('search 9 in BST-2 =', bst2.search(9))
print('search 17 in BST-2 =', bst2.search(17), '\n')

# Searching Recursively in a BST
print('search 5 in BST-1 =', bst.searchRecursive(5))
print('search 10 in BST-1 =', bst.searchRecursive(10))
print('search 9 in BST-2 =', bst2.searchRecursive(9))
print('search 17 in BST-2 =', bst2.searchRecursive(17), '\n')

# Delete in a BSTree
bst3 = BSTree(15)
bst3.insert(10)
bst3.insert(8)
bst3.insert(12)
bst3.insert(20)
bst3.insert(17)
bst3.insert(25)
bst3.insert(19)
print('BST-3', bst3)
print(bst3.bfs(), '::BST-3.', '\n')

# # remove node with value 8
# bst3.delete(8)
# print('nodes after removing 8')
# bst3.bfs()
# print('\n')
#
# # remove node with value 17
# bst3.delete(17)
# print('nodes after removing 17')
# bst3.bfs()
# print('\n')
#
# # remove node with value 15
# bst3.delete(15)
# print('nodes after removing 15')
# bst3.bfs()
# print('\n')

# Traversal in a BSTree
print('::IN-ORDER Traverse.', inorderBSTree(bst2))
print('::PRE-ORDER Traverse.', preorderBSTree(bst2))
print('::POST-ORDER Traverse.', postorderBSTree(bst2), '\n')

# Height of a BSTree
print('height of BST-2 =', heightBSTree(bst2))

# Greatest value in a BSTree
print('greatest value in BST-2 =', greatestValueBSTree(bst2))
