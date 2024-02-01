import sys
import time

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

def bunnyHopBackTraceOptimized(n):
    n = 2 * n
    """
        The idea is to ensure the balance of UP and DOWN hops
        Once we build a full path, we can then add it to the list of actual paths if the balance is 0
    """
    def validPath(path, count, actualPaths, balance):
        if len(path) == n: 
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

def printPaths(paths):
    # change 1 to U and -1 to D
    for path in paths:
        print(''.join(['U' if i == 1 else 'D' for i in path]))
        
def printPathsBalance(paths):
    # change 1 to U and -1 to D
    for path in paths:
        print(''.join(['U' if i == 1 else 'D' for i in path[0]]), end = ' ')
        print(f'Balance: {path[1]}')
        
def testBunnyHop(n):
    for i in range(1, n+1):
        start_time = time.time()
        count, _ = bunnyHopBrute(i)
        brute_elapsed_time = time.time() - start_time
        
        start_time = time.time()
        count1, _ = bunnyHopBackTrace(i)
        backtrace_elapsed_time = time.time() - start_time
        
        start_time = time.time()
        count2, _ = bunnyHopBackTraceOptimized(i)
        optimized_elapsed_time = time.time() - start_time
        print('---------------------------------------------')
        
        print(f'Elapsed time for n = {i}:')
        print(f'\tbunnyHopBrute: {brute_elapsed_time} seconds')
        print(f'\tBunnyHopBackTrace: {backtrace_elapsed_time} seconds')
        print(f'\tbunnyHopBackTraceOptimized: {optimized_elapsed_time} seconds')

        print(f'brute_count = {count}, backtrace_v1 = {count1}, backtrace_v2 = {count2}')

if __name__ == '__main__':
    if sys.argv[1] == 'test':
        if not int(sys.argv[2]):
            print('n must be less than 9')
        else: 
            testBunnyHop(int(sys.argv[2]))
    else: 
        start_time = time.time()
        count, paths = bunnyHopBackTraceOptimized(int(sys.argv[1]))
        elapsed_time = time.time() - start_time
        print(f'n = {sys.argv[1]} | Number of paths: {count}')
        print(f'Elapsed time: {elapsed_time} seconds\n')
        # printPaths(paths)
        printPathsBalance(paths)