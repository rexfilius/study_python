from dsa_notes.dsa.linkedlist.SinglyLinkedList \
    import SinglyLinkedList, mergeTwoLists

# Create a SinglyLinkedList
letterList = SinglyLinkedList()
for i in range(97, 110):
    letterList.append(chr(i))
print('letterlist=', letterList)

# Get a node and Set a node at an index
print('node at index3=', letterList[3])  # or letterList.getNodeAtIndex(3)
letterList[3] = 'dd'
print('change node value at index3=', letterList, '\n')

# using __len__ and __iter__
print('length of list= ', len(letterList))
for i in range(len(letterList)):
    print(letterList[i], end='..')
print('\n')

# insert at head and tail
print('head insertion=', letterList.push('a1'), letterList)
print('tail insertion=', letterList.append('z1'), letterList)
print('delete head=', letterList.deleteHead(), letterList)
print('delete tail=', letterList.deleteTail(), letterList, '\n')

# insert at an index
print('insert at index3=', letterList.insertNth(3, 'c1'), letterList)
print('delete at index3=', letterList.deleteNth(3), letterList, '\n')

# SPECIAL FUNCTIONS ON LINKED LIST
print('linked list', letterList)
print('print elements=:')
letterList.print()
print('\nprint elements in reverse=:')
letterList.printReverse2()

print('\nlast element=:', letterList.lastElement())
print('middle node=:', letterList.getMiddleNode())

# SPECIAL FUNCTION = Merge Two Sorted Linked List
listA = SinglyLinkedList()
listB = SinglyLinkedList()
listA.append(5)
listA.append(10)
listA.append(15)
listB.append(2)
listB.append(3)
listB.append(20)
print('\nlistA=', listA)
print('listB=', listB)
print('merge lists=', mergeTwoLists(listA.head, listB.head))
