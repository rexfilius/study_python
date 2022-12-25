from collections import deque

# Using Lists as Queues::
# It is also possible to use a list as a queue, where the first element added is the
# first element retrieved ("first-in, first-out"); however, lists are not efficient
# for this purpose. While 'appends' and 'pops' from the end of list are fast,
# doing 'inserts' or 'pops' from the beginning of a list is slow
# (because all of the other elements have to be shifted by one).
#
# To implement a queue, use collections.deque which was designed to have fast appends
# and pops from both ends.
queue_names = deque(['Eric', 'John', 'Michael'])
print(queue_names)

queue_names.append('Terry')
queue_names.append('Graham')
print(queue_names)
print()

# queue_names.pop()
# pop will remove the last item on the queue which isn't the desired behavior of queues
# popLeft will remove the first item on the queue
queue_names.popleft()
print(queue_names)