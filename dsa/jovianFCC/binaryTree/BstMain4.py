from dsa_courses.jovianFCC.binaryTree.User import User
from dsa_courses.jovianFCC.binaryTree.BSTNode import BSTNode
from dsa_courses.jovianFCC.binaryTree.BinaryNode import displayKeysfn

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# inserting nodes very primitively
# Level 0
rootNode = BSTNode(jadhesh.username, jadhesh)
# Level 1
rootNode.left = BSTNode(biraj.username, biraj)
rootNode.left.parent = rootNode
rootNode.right = BSTNode(sonaksh.username, sonaksh)
rootNode.right.parent = rootNode
# Level 2
rootNode.left.left = BSTNode(aakash.username, aakash)
rootNode.left.left.parent = rootNode.left
rootNode.left.right = BSTNode(hemanth.username, hemanth)
rootNode.left.right.parent = rootNode.left

rootNode.right.left = BSTNode(siddhant.username, siddhant)
rootNode.right.left.parent = rootNode.right
rootNode.right.right = BSTNode(vishal.username, vishal)
rootNode.right.right.parent = rootNode.right

print(displayKeysfn(rootNode))
