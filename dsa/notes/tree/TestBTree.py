from dsa_notes.dsa.tree.BTree import BinaryTree

# tree = BinaryTree('a')
# print(tree)

a_node = BinaryTree('a')
a_node.insertLeft('b')
a_node.insertRight('c')

b_node = a_node.leftChild
b_node.insertRight('d')

c_node = a_node.rightChild
c_node.insertLeft('e')
c_node.insertRight('f')

d_node = b_node.rightChild
e_node = c_node.leftChild
f_node = c_node.rightChild

print(a_node.value)  # a
print(b_node.value)  # b
print(c_node.value)  # c
print(d_node.value)  # d
print(e_node.value)  # e
print(f_node.value, '\n')  # f

print('breadth-first search (ALL NODES):=')
a_node.bfs()
print('\n')
