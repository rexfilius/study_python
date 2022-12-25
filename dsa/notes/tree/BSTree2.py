from pprint import pformat
from queue import SimpleQueue


class BSTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        if self.left_child is None and self.right_child is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left_child, self.right_child)}, indent=1)
        # return pformat({f"{self.value}": f"Left:[{self.left_child}] Right:[{self.right_child}]"}, indent=1)

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BSTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BSTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)
        return value == self.value

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)
            return True

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def bfs(self):
        """
        First add the root node into the queue with the put method.
        Iterate while the queue is not empty.
        Get the first node in the queue, and then print its value.
        Add both left and right children into the queue (if the current node has children).
        Done. We will print the value of each node, level by level, with our queue helper.
        """
        queue = SimpleQueue()
        queue.put(self)
        while queue.qsize() > 0:
            currentNode = queue.get()
            print(currentNode.value, end=' ')
            if currentNode.left_child:
                queue.put(currentNode.left_child)
            if currentNode.right_child:
                queue.put(currentNode.right_child)
