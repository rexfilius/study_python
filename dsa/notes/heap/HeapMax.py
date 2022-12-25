class HeapMax:

    def __init__(self):
        self.array = []

    def __repr__(self):
        return self.array.__repr__()

    def __str__(self):
        return self.__repr__()

    def size(self) -> int:
        """Returns the number of elements in the array/heap"""
        return len(self.array)

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
        return self.array[0]

    def insert(self, value):
        """Insert a new element to a heap"""
        self.array.append(value)
        count = self.size()
        self.siftUp(count - 1)

    def siftUp(self, index: int):
        """
        Swaps the current node with its parent, as long as the node has a
        higher priority than its parent.
        """
        parentIdx = HeapMax.parentIndex(index)
        while parentIdx is not None and self.array[index] > self.array[parentIdx]:
            self.array[index], self.array[parentIdx] = \
                self.array[parentIdx], self.array[index]
            index, parentIdx = parentIdx, HeapMax.parentIndex(parentIdx)

    def remove(self):
        """
        Removes and return the root node in a max-heap.
        """
        lastIndex = self.size() - 1
        self.array[0], self.array[lastIndex] = self.array[lastIndex], self.array[0]
        maxValue = self.array.pop(lastIndex)
        self.siftDown(0)
        return maxValue

    def siftDown(self, index: int):
        """
        Swaps the current node with its larger child,
        Repeats until the node is in its proper place.
        """
        while self.leftIndex(index) is not None:
            leftChildIndex = self.leftIndex(index)
            leftChild = self.array[leftChildIndex]
            largerChildIdx = self.array.index(leftChild)
            #
            if self.rightIndex(index) is not None:
                rightChildIndex = self.rightIndex(index)
                rightChild = self.array[rightChildIndex]
                largerChild = max(leftChild, rightChild)
                largerChildIdx = self.array.index(largerChild)
            #
            if self.array[index] < self.array[largerChildIdx]:
                self.array[index], self.array[largerChildIdx] = \
                    self.array[largerChildIdx], self.array[index]
            index = largerChildIdx
