from dsa_courses.jovianFCC.binaryTree.User \
    import User, UserDatabase

# Brute force implementation for a tree
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
print()

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

userDatabase = UserDatabase()
userDatabase.insert(aakash)
userDatabase.insert(vishal)
userDatabase.insert(siddhant)
print(userDatabase.listAll())
