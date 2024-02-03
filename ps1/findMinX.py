import random 
from heap import Heap
import heapq
"""
    Given a minheap, look at the root and check if its less than X. 
    if it is then recurse to its children
    if the root is greater than X, then prune that subtree
"""
def findValLtXInHeap(heap, x, idx=0):
    if idx >= len(heap.lst):
        return []
    
    if heap.lst[idx] < x:           # if root is less than x then traverse the heap
        return ([heap.lst[idx]] + 
                findValLtXInHeap(heap, x, 2*idx + 1) + 
                findValLtXInHeap(heap, x, 2*idx + 2))
    else:   # if root is greater than x then prune that subtree
        return []
    
def testFindValLtXInHeap():
    lst = [random.randint(0, 50) for _ in range(10)]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heap = Heap(lst)
    lst1 = lst.copy()
    heapq.heapify(lst1)
    print(f'Input list: {lst1} {len(lst1)}')
    print(f'Input min heap: {heap} {len(heap.lst)}')
    
    print(findValLtXInHeap(heap, 3, 0))

testFindValLtXInHeap()