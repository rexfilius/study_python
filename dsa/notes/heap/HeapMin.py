class HeapMin:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return self.items.__repr__()

    def __str__(self):
        return self.__repr__()

    def size(self) -> int:
        return len(self.items)

    def leftIndex(self, index: int) -> int | None:
        """Returns the left child index of the given index."""
        leftChildIndex = (2 * index) + 1
        if leftChildIndex < self.size():
            return leftChildIndex
        return None

    def rightIndex(self, index: int) -> int | None:
        """Returns the right child index of the given index."""
        rightChildIndex = (2 * index) + 2
        if rightChildIndex < self.size():
            return rightChildIndex
        return None

    @staticmethod
    def parentIndex(index) -> int | None:
        """Returns the parent index of the given index."""
        if index > 0:
            return (index - 1) // 2
        return None

    def peek(self):
        """
        Returns the element at the top of the Heap.
        implementation - returns first element in the list.
        """
        return self.items[0]

    def insert(self, value):
        """Insert a new element to the heap"""
        self.items.append(value)
        count = self.size()
        self.siftUp(count - 1)

    def siftUp(self, index: int):
        """
        Swaps the current node with its parent, as long as the node has a
        higher priority than its parent.
        """
        parentIdx = HeapMin.parentIndex(index)
        while parentIdx is not None and self.items[index] < self.items[parentIdx]:
            self.items[index], self.items[parentIdx] = \
                self.items[parentIdx], self.items[index]
            index, parentIdx = parentIdx, HeapMin.parentIndex(parentIdx)

    def remove(self):
        """
        Removes and return the root node in the heap.
        """
        count = self.size()
        self.items[0], self.items[count - 1] = self.items[count - 1], self.items[0]
        minValue = self.items.pop(count - 1)
        self.siftDown(0)
        return minValue

    def siftDown(self, index: int):
        """
        Swaps the current node with its smaller child.
        Repeats until the node is in its proper place.
        """
        while self.leftIndex(index) is not None:
            leftChildIndex = self.leftIndex(index)
            leftChild = self.items[leftChildIndex]
            smallerChildIdx = self.items.index(leftChild)
            #
            if self.rightIndex(index) is not None:
                rightChildIndex = self.rightIndex(index)
                rightChild = self.items[rightChildIndex]
                smallerChild = min(leftChild, rightChild)
                smallerChildIdx = self.items.index(smallerChild)
            #
            if self.items[index] > self.items[smallerChildIdx]:
                self.items[index], self.items[smallerChildIdx] = \
                    self.items[smallerChildIdx], self.items[index]
            index = smallerChildIdx
