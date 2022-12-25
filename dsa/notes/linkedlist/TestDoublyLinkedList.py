from dsa.notes.linkedlist.DoublyLinkedList import DoublyLinkedList

# Create a DoublyLinkedList
letters = DoublyLinkedList()
for i in range(97, 109):
    letters.append(chr(i))
print('letters=', letters, '\n')

# Get a node and Set a node at an index
print('node at index3=', letters[3])  # or letterList.getNodeAtIndex(3)
letters[3] = 'dd'
print('change node value at index3=', letters, '\n')

# using __len__ and __iter__
print('length of list= ', len(letters))
for i in range(len(letters)):
    print(letters[i], end='..')
print('\n')

# insert at head and tail
print('head insertion=', letters.push('A1'), letters)
print('tail insertion=', letters.append('L1'), letters)
print('delete head=', letters.deleteHead(), letters)
print('delete tail=', letters.deleteTail(), letters, '\n')

# insert at an index
print('insert at index4=', letters.insertNth(4, 'E1'), letters)
print('delete at index4=', letters.deleteNth(4), letters, '\n')

# SPECIAL FUNCTIONS ON LINKED LIST
print('letters', letters)
print('print elements=:')
letters.print()
print('\nprint elements in reverse=:')
letters.printReverse2()
