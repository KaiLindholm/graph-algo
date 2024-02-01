   
class Heap: 
    def __init__(self):
        self.heap = []
    def __init__(self, lst):
        self.heap = []
        self.buildHeap(lst)
        
    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap)-1)
    
    def heapifyUp(self, index):
        while index > 0:
            parent = (index-1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
            
    def removeMin(self):
        if len(self.heap) == 0:
            return None
        minVal = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapifyDown(0)
        return minVal
    
    def heapifyDown(self, index):
        while index < len(self.heap):
            left = 2*index + 1
            right = 2*index + 2
            if left < len(self.heap) and self.heap[left] < self.heap[index]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                index = left
            elif right < len(self.heap) and self.heap[right] < self.heap[index]:
                self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                index = right
            else:
                break
    
    def __str__(self):
        return str(self.heap)
    
    def __len__(self):
        return len(self.heap)
    
    def buildHeap(self, lst):
        self.heap = lst
        for i in range(len(self.heap)-1, -1, -1):
            self.heapifyDown(i)
            
    def __getitem__(self, index):
        return self.heap[index]
    