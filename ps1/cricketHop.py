def cricketHop(n): 
    if n == 0: 
        return 1
    elif n == 1: 
        return 0
    return (1/3) + (2/3) * cricketHop(n-1)

def testHopProb():
    for i in range(100):
        print('n =', i, 'prob =', cricketHop(i))
        print('')
        
testHopProb()