from heap import Heap
import heapq


def hopProb(n):
    if n == 1:  # the one hop case that will never get the cricket back to the goal 
        return 0
    # recursive case
    def hop(n): 
        if n == 0:
            return 1
        else: 
            return (1/3) * hop(n-1)
         
    return hop(n)
    
def testHopProb():
    for i in range(10):
        print('n =', i, 'prob =', hopProb(i))