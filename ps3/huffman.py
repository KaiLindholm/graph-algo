import numpy as np
from heap import Heap, Node

def load_data(filename): 
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    heap = Heap([], comparator=lambda x, y: x < y)
    for line in lines[1:]:
        char, value = line.strip().split(':')
        newNode = Node(char, float(value))
        heap.insert(newNode)

    return heap

def output(output_list, huffman_tree):
    with open(output_list, 'w') as f:
        for item in huffman_tree:
            f.write(f'{(item[0])}: {item[1]}\n')
            
def printNodes(node, val='', tree = {}): 
  
    # huffman code for current node 
    newVal = val + str(node.huff) 
  
    # if node is not an edge node 
    # then traverse inside it 
    if(node.left): 
        printNodes(node.left, newVal, tree) 
    if(node.right): 
        printNodes(node.right, newVal, tree) 
  
        # if node is edge node then 
        # display its huffman code 
    if(not node.left and not node.right): 
        tree[node.char] = newVal
              
if __name__ == '__main__':
    
    heap = load_data('data/input.txt')
    
    # ensure some base order of the heap to ensure nodes that are popped as left and right are consistent
    for i, node in enumerate(heap.heap):
        node.order = i
        
    while len(heap) > 1:
        left = heap.removeRoot()
        right = heap.removeRoot()
        
        # if the order of the left node is greater than the right node, swap them
        # left node order will be less than right node order
        if left.order > right.order:
            left, right = right, left
            
        left.huff = 0
        right.huff = 1

        newNode = Node(left.char + right.char, 
                        left.freq + right.freq, 
                        left, right) 
        
        newNode.order = left.order + right.order

        heap.insert(newNode)
    # printNodes(heap.heap[0])
    encodings = {}
    printNodes(heap.heap[0], '', encodings)

    # print encodings in alphabetical order
    encodings = sorted(encodings.items(), key=lambda x: x[0])
    for item in encodings:
        print(f"{item[0]}: {item[1]}")