"""
All of these implementations are all brute force, but the last one 
has an optimize path validation function
"""

import sys
import time
import matplotlib.pyplot as plt

# find all paths that start with a 1, and end with a 0, and have equal number of 0s and 1s
# at any given time point if the number of 1s must be greater than or equal to the number of 0s
def bunnyHopBrute(n):
    n = 2*n
    UP = 1
    DOWN = -1
    
    # generate all possible paths with no constraints 
    paths = [[]]
    for _ in range(n): 
        new_paths = []
        for path in paths:
            new_paths.append(path + [DOWN])
            new_paths.append(path + [UP])
        paths = new_paths
    
    count = 0
    actualPaths = []
    if n == 0:
        return 0, []
    
    """
    Check if a path is valid 
    Criterion - 
        1. The path starts with a 1 and ends with a -1 
        2. The sum of the path is 0
        3. At any given time point if the number of 1s must be greater than or equal to the number of 0s
    """
    for path in paths: 
        if path[0] == UP and path[-1] == DOWN and sum(path) == 0 and all([sum(path[:i]) >= 0 for i in range(1, len(path))]):
            count += 1
            actualPaths.append(path)
            
    return count, actualPaths

def bunnyHopBackTrace(n): 
    n = 2*n
    def backtrack(path, count, actualPaths, up_count, down_count):
        if len(path) == n:
            if (path[0] == UP and 
                path[-1] == DOWN and 
                up_count == down_count and 
                all([sum(path[:i]) >= 0 for i in range(1, len(path))])): # this part needs to be optimized
                
                count[0] += 1
                actualPaths.append(path.copy())
            return

        path.append(UP)
        up_count += 1
        backtrack(path, count, actualPaths, up_count, down_count)
        path.pop()
        up_count -= 1

        path.append(DOWN)
        down_count += 1
        backtrack(path, count, actualPaths, up_count, down_count)
        path.pop()
        down_count -= 1

    UP = 1
    DOWN = -1
    count = [0]
    actualPaths = []
    
    if n == 0:
        return 0, []

    backtrack([], count, actualPaths, 0, 0)
    return count[0], actualPaths

"""
    Given that there are two options that can come from a given state, and the path length is k = 2n
    The runtime complexity of this solution is O(2^k)
"""
def bunnyHopBackTraceOptimized(n):
    n = 2 * n
    """
        The idea is to ensure the balance of UP and DOWN hops
        Once we build a full path, we can then add it to the list of actual paths if the balance is 0
    """
    def validPath(path, count, actualPaths, balance):
        if len(path) == n:  # Base case: if the path is complete
            if balance == 0: 
                count[0] += 1
                actualPaths.append([path.copy(), balance])
            return
        """
            If the balance is greater than 0, we can add a DOWN hop
        """
        
        if balance > 0:
            path.append(DOWN)
            validPath(path, count, actualPaths, balance - 1)
            path.pop()

        """ 
            If we are able to add an UP hop, we can add it to the path
            and again check if its a valid path
        """
        path.append(UP)
        validPath(path, count, actualPaths, balance + 1)
        path.pop()


    UP = 1
    DOWN = -1
    count = [0]
    actualPaths = []
    if n == 0:
        return 0, []

    validPath([], count, actualPaths, 0)
    return count[0], actualPaths

"""
Prints the paths in a human readable format
"""
def printPaths(paths):
    # change 1 to U and -1 to D
    for path in paths:
        print(''.join(['U' if i == 1 else 'D' for i in path]))
        
def printPathsBalance(paths):
    # change 1 to U and -1 to D
    for path in paths:
        print(''.join(['U' if i == 1 else 'D' for i in path[0]]))
        # print(f'Balance: {path[1]}')
        
def bunnyHopv3(n): 
    if n == 1: 
        return 1 
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][1] = 1
    
    for i in range(n):
        dp[i][0] = 1
    
    for i in range(1, n):
        for j in range(1, n):
            # if the cells directly above are 0. Then we can skip 
            if not (dp[i-1][j-1] == 0 and dp[i-1][j] == 0):  
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[-1][-1]

"""
Plots the time taken for each algorithm
"""
def plotBunnyHop(times):
    for algo, time in times.items():
        if time:
            plt.plot(time, label=algo)
        
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.title('Bunny Hop')
    plt.legend()
    plt.savefig('bunnyHop.png')
    plt.close()
    
"""
Plots the growth of the number of paths as n increases
"""
def plotBunnyHopPathCount(count):
    plt.plot(count)

    plt.xlabel('n')
    plt.ylabel('Path Count')
    plt.title('Bunny Hop')
    plt.savefig('bunnyHopPathCount.png')
    plt.close()
"""
Tests the bunnyHop algorithms for n = 1 to n
"""
def testBunnyHop(n):
    times = {
        'bunnyHopBrute': [],
        'bunnyHopBackTrace': [],
        'bunnyHopBackTraceOptimized': [],
        'BunnyHopDynamic': []
    }
    
    counts = {
        'bunnyHopBrute': [],
        'bunnyHopBackTrace': [],
        'bunnyHopBackTraceOptimized': [],
        'BunnyHopDynamic': []
    }
    
    for i in range(1, n+1):
        """
            First two algorithms are my first tries and are not optimized
            The last algorithm is the optimized version
        """
        # start_time = time.time()
        # counts['bunnyHopBrute'].append(bunnyHopBrute(i)[0])
        # times['bunnyHopBrute'].append(time.time() - start_time)
        
        # start_time = time.time()
        # counts['bunnyHopBackTrace'].append(bunnyHopBackTrace(i)[0])
        # times['bunnyHopBackTrace'].append(time.time() - start_time)
        
        # start_time = time.time()
        # counts['bunnyHopBackTraceOptimized'].append(bunnyHopBackTraceOptimized(i)[0])
        # times['bunnyHopBackTraceOptimized'].append(time.time() - start_time)
        
        start_time = time.time()
        counts['BunnyHopDynamic'].append(bunnyHopv3(i))
        times['BunnyHopDynamic'].append(time.time() - start_time)
        
        print('---------------------------------------------')
        print(f'Elapsed time for n = {i}:')
        # print(f'\tbunnyHopBackTraceOptimized: {times["bunnyHopBackTraceOptimized"][-1]} seconds')
        print(f'\tBunnyHopDynamic: {times["BunnyHopDynamic"][-1]} seconds')

        print(f'Number of paths: {counts["BunnyHopDynamic"][-1]}')
        
    print('---------------------------------------------')

    plotBunnyHop(times)
    plotBunnyHopPathCount(counts['BunnyHopDynamic'])
if __name__ == '__main__':
    if sys.argv[1] == 'test':
        if not int(sys.argv[2]):
            print('Usage: python bunnyHop.py test <n>')
            sys.exit(1)
            
        if int(sys.argv[2]) <= 0:
            print('n must be greater than 0')
            sys.exit(1)            
            
        if int(sys.argv[2]) > 11:
            print('running the test for n > 11 will take a long time')
        
        testBunnyHop(int(sys.argv[2]))
    else: 
        start_time = time.time()
        count, paths = bunnyHopBackTraceOptimized(int(sys.argv[1]))
        elapsed_time = time.time() - start_time
        print(f'n = {sys.argv[1]} | Number of paths: {count}')
        print(f'Elapsed time: {elapsed_time} seconds\n')
        # printPaths(paths)
        printPathsBalance(paths)
        