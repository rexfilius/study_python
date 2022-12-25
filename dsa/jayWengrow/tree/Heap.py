class Heap:
    """Implementation of an Array-Based Heap"""

    def __init__(self):
        self.data = []

    def __repr__(self):
        return self.data.__repr__()

    def rootNode(self):
        return self.data[0]  # value at first index

    def lastNode(self):
        return self.data[-1]  # value at last index

    @classmethod
    def leftChildIndex(cls, index):
        return (index * 2) + 1

    @classmethod
    def rightChildIndex(cls, index):
        return (index * 2) + 2

    @classmethod
    def parentIndex(cls, index):
        return (index - 1) // 2

    def insert(self, value):
        self.data.append(value)
        newNodeIndex = len(self.data) - 1
        parent = self.parentIndex(newNodeIndex)

        while newNodeIndex > 0 and self.data[newNodeIndex] > self.data[parent]:
            self.data[parent], self.data[newNodeIndex] = \
                self.data[newNodeIndex], self.data[parent]
            # newNodeIndex = self.parentIndex(newNodeIndex)
            newNodeIndex = parent

    def delete(self):
        """NOT WORKING AS INTENDED."""
        self.data[0] = self.data.pop()
        trickleNodeIndex = 0
        while self.hasGreaterChild(trickleNodeIndex):
            largerChildIndex = self.getLargerChildIndex(trickleNodeIndex)
            self.data[trickleNodeIndex], self.data[largerChildIndex] = \
                self.data[largerChildIndex], self.data[trickleNodeIndex]
            trickleNodeIndex = largerChildIndex

    def hasGreaterChild(self, index):
        """Check whether the node at index has left and right children and
         if either of those children are greater than the node at index.
         NOT WORKING AS INTENDED."""
        leftChild = self.leftChildIndex(index)
        rightChild = self.rightChildIndex(index)
        hasLeftChild = self.data[leftChild] is None \
                       and self.data[leftChild] > self.data[index]
        hasRightChild = self.data[rightChild] is None \
                        and self.data[rightChild] > self.data[index]
        return hasLeftChild or hasRightChild

    def getLargerChildIndex(self, index):
        leftChild = self.leftChildIndex(index)
        rightChild = self.rightChildIndex(index)
        if self.data[rightChild] is None:
            return leftChild
        if self.data[rightChild] > self.data[leftChild]:
            return rightChild
        else:
            return leftChild
