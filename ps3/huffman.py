from heap import Heap, Node

LEFT = '0'
RIGHT = '1'

def load_data(filename): 
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    heap = Heap([], comparator=lambda x, y: x < y)
    for line in lines[1:]:
        char, value = line.strip().split(':')
        newNode = Node(char, float(value))
        heap.insert(newNode)

    return heap

def output(output_list, encodings):
    print(encodings)
    with open(output_list, 'w') as f:
        for item in encodings:
            f.write(f"{item[0]}: {item[1]}\n")
          
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
        
        # set the huffman code for the left and right nodes
        left.huff = LEFT
        right.huff = RIGHT

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
    newVal = val + node.huff
  
    # if node is not a leaf node keep building the huffman code
    if(node.left): 
        get_encodings(node.left, newVal, encodings) 
    if(node.right): 
        get_encodings(node.right, newVal, encodings) 
  
    # if the node is a leaf node save the code for the char
    if(not node.left and not node.right): 
        encodings[node.char] = newVal
              
if __name__ == '__main__':
    # load the data into a heap
    heap = load_data('data/input.txt')
    
    # build the huffman tree. 
    huffman_tree = buildHuffmanTree(heap)
    
    # get the encodings for each character
    encodings = {}
    get_encodings(huffman_tree, '', encodings)
    
    # Output the encodings in alphabetical order as per the requirements
    encodings = sorted(encodings.items(), key=lambda x: x[0])
    output('data/output.txt', encodings)