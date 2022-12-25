from dsa_notes.dsa.queue.QueueOnStack import QueueOnStack

# Create a QueueOnStack
qu = QueueOnStack()
print('queue', qu)

# Check if queue is empty
print('is queue empty -', qu.isEmpty(), '\n')

# Enqueue operation on a Queue
for i in range(97, 106):
    qu.enqueue(chr(i))
print('queue -', qu)

# Peek a Queue
print('element in front -', qu.peek())
# Size of Queue
print('size of queue -', len(qu), '\n')

# Dequeue operation on a queue
print('queue', qu)
qu.dequeue()
qu.dequeue()
print('queue after dequeueing twice -', qu)
print('element in front -', qu.peek())
