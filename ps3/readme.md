# Huffman Encoding

This is a Python script that implements Huffman encoding, a lossless data compression algorithm. Huffman encoding is commonly used in file compression and data transmission applications.

## Usage

To use this script, follow these steps:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt and navigate to the directory where `huffman.py` is located.
3. Run the script using the following command:

    ```shell
    python huffman.py <input file> <output file>
    ```

## Algorithm

The script uses the following steps to perform Huffman encoding:

1. Read the input file and initialize the heap. 
2. Generate the Huffman codes for each character in the tree.

    a. This is done by popped the two least frequent characters from the heap and creating a new node 
    with the sum of their frequencies.

    b. We also keep track of the relative ordering of the nodes so there is some consistency as to how nodes are determined to be left, or right.

    c. Continue popping nodes from the heap until we are left with the huffman tree root node. 

3. To extract the encodings we then recursively traverse the tree and assign a `0` to left nodes and `1` to right nodes. Saving the code to a dictionary that maps each character to its encoding.
4. Outputs the character, and its huffman coding to an output file of the users choice. 

## Examples
`python huffman.py data/input.txt data/output.txt`

input.txt 
```
5
a : 0.32
b : 0.25
c : 0.20
d : 0.18
e : 0.05
```

output.txt
```
a : 11
b : 10
c : 01
d : 001
e : 000
```