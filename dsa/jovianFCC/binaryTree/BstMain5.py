from dsa_courses.jovianFCC.binaryTree.User import User
from dsa_courses.jovianFCC.binaryTree.BSTNode \
    import BSTNode, insertNode, listAllNodes, createBalancedBST
from dsa_courses.jovianFCC.binaryTree.BinaryNode import displayKeysfn

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# Using the insert function for a BST
tree = insertNode(None, jadhesh.username, jadhesh)
displayKeysfn(tree)

insertNode(tree, biraj.username, biraj)
insertNode(tree, sonaksh.username, sonaksh)
insertNode(tree, aakash.username, aakash)
insertNode(tree, hemanth.username, hemanth)
insertNode(tree, siddhant.username, siddhant)
insertNode(tree, vishal.username, vishal)
displayKeysfn(tree)
print()
print(listAllNodes(tree), '\n')

# Creating a balanced BST
users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
data = [(user.username, user) for user in users]

tree2 = createBalancedBST(data)
displayKeysfn(tree2)
