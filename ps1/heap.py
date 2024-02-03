"""
    A MinHeap represented as a list 
"""
import sys
class Heap: 
    def __init__(self, lst): 
        self.lst = lst.copy()
        self.heapify()
        
    def swap(self, i, j): 
        heap = self.lst
        heap[i], heap[j] = heap[j], heap[i]
    """
        O(n) heapify operation
    """
    def heapify(self): 
        for i in range(len(self.lst)//2, -1, -1): 
            self.sift_down(i)

    def sift_down(self, index):
        heap = self.lst
        size = len(heap)
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < size and heap[left_child] < heap[smallest]:
            smallest = left_child

        if right_child < size and heap[right_child] < heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.swap(index, smallest)
            self.sift_down(smallest)
        
    """
        HOMEWORK REQUIRED
    """
    def deleteMin(self):
        heap = self.lst
        if len(heap) == 0:
            return None
        if len(heap) == 1:
            return heap.pop()
        min = heap[0]
        heap[0] = heap.pop()
        self.sift_down(0)
        
        return min

    def sift_up(self, i): 
        while i > 0 and self.lst[i] > self.lst[self.get_parent(i)]: 
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)
    """
        HOMEWORK REQUIRED
        returns an increasing order list of elements in the heap
    """
    def heap_sort(self): 
        return [self.deleteMin() for _ in range(len(self.lst))]
    
    def getElement(self, i):
        return self.lst[i]
    
    def __str__(self):
        return str(self.lst)    
    
def output(output_list, sorted_list):
    with open(output_list, 'w') as file:
        for item in sorted_list:
            file.write(f'{item}\n')
     
"""
    If the script is run with no arguments, a random list of 10 integers is generated and sorted.
    
    else  the script requires an input text file with vertically aligned numbers, 
    and an output file to write the sorted list to.
"""
if __name__ == "__main__":
    if len(sys.argv) == 1:
        import random 
        lst = [random.randint(0, 100) for _ in range(10)]
        print(f'Input list: {lst}')
        heap = Heap(lst)
        print(f'Heap: {heap.lst}')
        sorted_list = heap.heap_sort()
        print(f'Sorted list: {sorted_list}')
        output('output.txt', sorted_list)

        sys.exit(0)
        
    if len(sys.argv) != 3: 
        print('Usage: python heap.py <input_list> <output_list>')
        sys.exit(1)
        
    input_list = sys.argv[1]
    output_list = sys.argv[2]
    
    with open (input_list, 'r') as file:
        lst = [int(line.strip()) for line in file]
        
    print(f'Input list: {lst}')
    heap = Heap(lst)
    sorted_list = heap.heap_sort()
    print(f'Sorted list: {sorted_list}')
    output(output_list, sorted_list)
