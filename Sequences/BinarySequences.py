from itertools import cycle

def thue_morse(invert=False):
    """
    Thue-Morse Sequence
    
    Args:
        invert -- bool, give the complement of the Thue Morse sequence
    
    
    OEIS A010060
    """
    
    if invert:
        S = [1]
        yield 1
    else:
        S = [0]
        yield 0
    
    while True:
        new = []
        
        for s in S:
            yield (s+1)%2
            new.append((s+1)%2)
            
        S += new


def fibonacci_word(invert=False):
    """
    Fibonacci Word
    
    Args:
        invert -- bool, give the complement of the Fibonacci word
    
    OEIS
    """
    
    if invert:
        a,b = (1,),(1,0)
    else:
        a,b = (0,),(0,1)
    n = 0
    
    while True:
        for i in range(n,len(b)):
            yield b[i]
        
        n = len(b)
        a,b = b,b+a




def gray_codes():
    """
    Ordering of binary codes such that there is exactly one change between successive codes
    """
    
    yield (0,)
    
    cycles = [cycle([1,1,0,0])]
    cycle_len = 2
    ctr = 0
    
    while True:
        ctr += 1
        
        if ctr == cycle_len:
            cycle_len *= 2
            
            L = [1]*cycle_len + [0]*cycle_len
            cycles.append(cycle(L))
        
        N = []
        for n in reversed(cycles):
            N.append(next(n))
        
        yield tuple(N)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Thue-Morse Sequence")
    simple_test(thue_morse(),18,
                "0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0")
    
    print("\nInfinite Fibonacci Word")
    simple_test(fibonacci_word(),18,
                "0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1")
    
    print("\nGray Codes")
    simple_test(gray_codes(),6,
                "(0,), (1,), (1, 1), (1, 0), (1, 1, 0), (1, 1, 1)")
    