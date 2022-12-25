from dsa.notes.heap.HeapMax import HeapMax

# Creating a Max-Heap
heap1 = HeapMax()
heap1.insert(6)
heap1.insert(10)
heap1.insert(15)
heap1.insert(12)
print('heap1 =', heap1)

heap2 = HeapMax()
n1 = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
for num in n1:
    heap2.insert(num)
print('heap2 =', heap2, )

heap3 = HeapMax()
n2 = [88, 100, 25, 87, 16, 8, 86, 12, 50, 2, 15, 3]
for num in n2:
    heap3.insert(num)
print('heap3 =', heap3, '\n')

# Peek operation on Heap
print('element at top heap1 =', heap1.peek())
print('element at top heap2 =', heap2.peek())
print('element at top heap3 =', heap3.peek(), '\n')

# Insert operation on a heap
heap1.insert(19)
print('insert 19 in heap1 =', heap1)
heap2.insert(300)
print('insert 300 in heap2 =', heap2)
heap3.insert(105)
print('insert 105 in heap3 =', heap3, '\n')

# Remove operation on a heap
heap1.remove()
print('after deletion, heap1 =', heap1)
heap2.remove()
print('after deletion, heap2 =', heap2)
heap3.remove()
print('after deletion, heap3 =', heap3)


