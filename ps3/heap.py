class Node:
    def __init__(self, key, value, left = None, right = None):
        self.char = key
        self.freq = value
        
        self.left = left
        self.right = right
        self.order = None
        self.huff = ''
        
    def __lt__(self, other):
        return self.freq < other.freq
    
    def isLeaf(self): 
        return not self.left and not self.right
    
    def __repr__(self):
        return f'{self.char}: {self.freq:.2f} {self.huff} {self.order}'
    
    
class Heap:
    def __init__(self, heap, comparator=lambda x, y: x < y): # defaults to min heap
        self.heap = heap
        self.size = len(heap)
        self.comparator = comparator   
        self.build_heap()
    
    def build_heap(self):
        for i in range(self.size//2, -1, -1):
            self.heapify(i)
    
    def heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
        
        if left < self.size and self.comparator(self.heap[left], self.heap[smallest]):
            smallest = left
        
        if right < self.size and self.comparator(self.heap[right], self.heap[smallest]):
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
            
    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.comparator(self.heap[i], self.heap[(i-1)//2]):
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2
            
    def removeRoot(self):
        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.heapify(0)
        return root
    
    def __str__(self):
        return str([node for node in self.heap])
    
    def __len__(self):
        return self.size
