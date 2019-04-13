from Sequences.Utils import choose

def pascal():
    """Pascal's Triangle"""
    
    n, k = 0, 0
    while True:
        
        yield choose(n,k)
               
        if n == k:
            n += 1
            k = 0
        else:
            k += 1