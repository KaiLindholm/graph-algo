   
class Heap: 
    def __init__(self):
        self.heap = []
        
    def __init__(self, lst):
        self.heap = []
        self.buildHeap(lst.copy())
    
    def buildHeap(self, lst):
        self.heap = lst
        for i in range(len(self.heap)//2, -1, -1):
            self.heapifyDown(i)


    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap)-1)
            
    def removeRoot(self):
        if len(self.heap) == 0:
            return None
        
        minVal = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapifyDown(0)
        
        return minVal
    
    def getLeftChild(self, index):  
        return 2*index + 1
    
    def getRightChild(self, index):
        return 2*index + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __str__(self):
        return str(self.heap)
    
    def __len__(self):
        return len(self.heap)
        
    def __getitem__(self, index):
        return self.heap[index]
    
class MinHeap(Heap):            
    def heapifyDown(self, index):
        while index < len(self.heap):
            left = self.getLeftChild(index)
            right = self.getRightChild(index)
            smallest = index
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break
    
    def heapifyUp(self, index):
        while index > 0:
            parent = (index-1) // 2
            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break
            
class MaxHeap(Heap): 
    def heapifyDown(self, index):
        while index < len(self.heap):
            left = self.getLeftChild(index)
            right = self.getRightChild(index)
            largest = index
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break
    
    def heapifyUp(self, index):
        while index > 0:
            parent = (index-1) // 2
            if self.heap[index] > self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break
            
def heapSort(lst, reverse=False):
    if reverse:
        heap = MinHeap(lst)
    else:
        heap = MaxHeap(lst)
        
    sortedList = []
    for _ in range(len(heap)):
        sortedList.append(heap.removeRoot())
    return sortedList

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7]
    minHeap = MinHeap(lst)
    print(minHeap)
    minHeap.removeRoot()
    print(minHeap)
    maxHeap = MaxHeap(lst)
    print(maxHeap)
    maxHeap.removeRoot()
    print(maxHeap)
    import random

    random_numbers = [random.randint(1, 100) for _ in range(10)]

    print(random_numbers)
    print(heapSort(random_numbers, True))
    