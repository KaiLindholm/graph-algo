"""
    A MinHeap represented as a list 
"""
import sys
class Heap: 
    def __init__(self, lst): 
        self.lst = lst
        self.heapify()
        
    def swap(self, i, j): 
        heap = self.lst
        heap[i], heap[j] = heap[j], heap[i]
        
    def heapify(self): 
        for i in range(len(self.lst)//2, -1, -1): 
            self.sift_down(i)

    def sift_down(self, index, end=None):
        
        if end is None:
            end = len(self.lst)
            
        heap = self.lst
        
        left_child_index = 2 * index + 1
        smallest = index

        while left_child_index < end:
            right_child_index = left_child_index + 1

            if right_child_index < end and heap[right_child_index] > heap[left_child_index]:
                smallest = right_child_index
            else:
                smallest = left_child_index

            if heap[smallest] > heap[index]:
                heap[index], heap[smallest] = heap[smallest], heap[index]
                index = smallest
                left_child_index = 2 * index + 1
            else:
                break
            
    def sift_up(self, i): 
        while i > 0 and self.lst[i] > self.lst[self.get_parent(i)]: 
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)
    
    def heap_sort(self): 
        heap = self.lst
        for i in range(len(heap)-1, 0, -1): 
            heap[0], heap[i] = heap[i], heap[0]
            self.sift_down(0, i)
            
        return heap
    
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
