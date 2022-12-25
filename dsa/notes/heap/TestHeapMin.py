from dsa_notes.dsa.heap.HeapMin import HeapMin

# Creating a Min-Heap
heap1 = HeapMin()
heap1.insert(12)
heap1.insert(20)
heap1.insert(5)
heap1.insert(25)
heap1.insert(13)
print('heap1 =', heap1)

heap2 = HeapMin()
n1 = [1, 2, 25, 7, 17, 36, 3, 19, 100]
for num in n1:
    heap2.insert(num)
print('heap2 =', heap2, '\n')

# Peek operation on a min-heap
print('element at top heap1 =', heap1.peek())
print('element at top heap2 =', heap2.peek(), '\n')

# Insert operation on a min-heap
heap1.insert(3)
print('insert 3 in heap1 =', heap1)
heap2.insert(5)
print('insert 5 in heap2 =', heap2, '\n')

# Remove operation on a min-heap
heap1.remove()
print('after deletion, heap1 =', heap1)
heap2.remove()
print('after deletion, heap2 =', heap2, '\n')
