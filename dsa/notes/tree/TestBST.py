from dsa.notes.tree.BST import searchBST, \
    searchBSTRecursive, deleteBST, isEmptyBST, bfsBST
from dsa.notes.tree.BSTree import BSTree

values = (8, 3, 6, 1, 10, 14, 13, 4, 7)
bst = BSTree(8)
bst.insert(3)
bst.insert(6)
bst.insert(1)
bst.insert(10)
bst.insert(14)
bst.insert(13)
bst.insert(4)
bst.insert(7)

bfsBST(bst)
print(searchBST(bst, 6))
print(searchBSTRecursive(bst, 6))
