from heap import Heap, Node
import sys
LEFT = '0'
RIGHT = '1'

def load_data(filename): 
    try: 
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File \"{filename}\" does not exist")
        sys.exit(1)
        
    heap = Heap([], comparator=lambda x, y: x < y)
    for line in lines[1:]:
        char, freq = line.strip().split(':')
        newNode = Node(char, float(freq))
        heap.insert(newNode)

    return heap

def output(output_file, encodings):
    """Outputs the encodings to a file"""
    try: 
        with open(output_file, 'w') as f:
            for char, code in encodings:
                f.write(f"{char}: {code}\n")
                
    except FileNotFoundError:
        print(f"File \"{output_file}\" does not exist")
        sys.exit(1)
          
def buildHuffmanTree(heap) -> Node:
    """Builds a huffman tree from a heap. 

    Args:
        heap (Heap): A min heap of characters and their frequencies

    Returns:
        Node: The root of the huffman tree
    """
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

        newNode = Node(left.char + right.char, 
                        left.freq + right.freq, 
                        left, right) 
        
        newNode.order = left.order + right.order # sum the order of the left and right nodes

        heap.insert(newNode)  
    return heap.removeRoot()
        
def get_encodings(node, val, encodings: dict): 
    """ Gets the encodings for each char via a dfs traversal of the huffman tree

    Args:
        node (Node): The root of the huffman tree
        val (str, optional): The base recursive step for building each node. Defaults to ''.
        encodings (dict, optional): A dictionary of characters and their huffman code. Defaults to {}.
    """
    
    # if node is not a leaf node keep building the huffman code
    if(node.left): 
        get_encodings(node.left, val + LEFT, encodings) 
    if(node.right): 
        get_encodings(node.right, val + RIGHT, encodings) 
  
    # if the node is a leaf node save the code for the char
    if(not node.left and not node.right): 
        encodings[node.char] = val
              
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print('Usage: python3 huffman.py <input_file> <output_file>')
        sys.exit()
    
    input_file = sys.argv[1].strip()
    output_file = sys.argv[2].strip()
    
    # load the data into a heap
    heap = load_data(input_file)
    
    # build the huffman tree. 
    huffman_tree = buildHuffmanTree(heap)
    
    # get the encodings for each character
    encodings = {}
    get_encodings(huffman_tree, '', encodings)
    
    # Output the encodings in alphabetical order as per the requirements
    encodings = sorted(encodings.items(), key=lambda x: x[0])
    output(output_file, encodings)