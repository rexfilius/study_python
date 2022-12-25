"""
You are tasked with developing a fast in-memory data structure to manage profile
info (username, name, email) for 100 million users. It should allow the following
operations to be performed efficiently.
1. Insert the profile info for a new user
2. Find the profile info of a new user, given their username
3. Update the profile info of a user, given their username
4. List all the users of the platform, sorted by username
You can assume the usernames are unique
"""
from dsa_courses.jovianFCC.binaryTree.BSTNode import findNode, \
    insertNode, balanceBst, updateNode, listAllNodes
from dsa_courses.jovianFCC.binaryTree.BinaryNode \
    import displayKeysfn, sizeofTreefn


class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = findNode(self.root, key)
        if not node:
            self.root = insertNode(self.root, key, value)
            self.root = balanceBst(self.root)
        else:
            updateNode(self.root, key, value)

    def __getitem__(self, key):
        node = findNode(self.root, key)
        return node.value if node else None

    def __iter__(self):
        # returns a generator, not a list
        # allows this class to be used in a for-loop
        return (x for x in listAllNodes(self.root))

    def __len__(self):
        return sizeofTreefn(self.root)

    def display(self):
        return displayKeysfn(self.root)
