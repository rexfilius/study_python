from dsa.notes.tree.BSTree2 import BSTree

bst = BSTree(15)
bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)
print('bst', bst, '\n')

print('breadth first search (ALL NODES):=')
bst.bfs()
print('\n')

# remove node with value 8
bst.remove_node(8, None)
print('nodes after removing 8')
bst.bfs()
print('\n')

# remove node with value 17
bst.remove_node(17, None)
print('nodes after removing 17')
bst.bfs()
print('\n')

# remove node with value 15
bst.remove_node(15, None)
print('nodes after removing 15')
bst.bfs()
print('\n')
