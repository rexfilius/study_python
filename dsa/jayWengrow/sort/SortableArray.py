class SortableArray:
    """Implementation of a SortableArray class that includes a partition method"""

    def __init__(self, array):
        self.array = array

    def partitionMethod(self, leftPointer, rightPointer):
        pivotIndex = rightPointer
        pivot = self.array[pivotIndex]
        rightPointer -= 1
        while True:
            while self.array[leftPointer] < pivot:
                leftPointer += 1
            while self.array[rightPointer] > pivot:
                rightPointer -= 1
            if leftPointer >= rightPointer:
                break
            else:
                self.array[leftPointer], self.array[rightPointer] = \
                    self.array[rightPointer], self.array[leftPointer]
                leftPointer += 1
        self.array[leftPointer], self.array[pivotIndex] = \
            self.array[pivotIndex], self.array[leftPointer]
        return leftPointer

    def quickSortMethod(self, leftIndex, rightIndex):
        """O(NlogN) time"""
        if rightIndex - leftIndex <= 0:
            return
        pivotIndex = self.partitionMethod(leftIndex, rightIndex)
        self.quickSortMethod(leftIndex, pivotIndex - 1)
        self.quickSortMethod(pivotIndex + 1, rightIndex)
