def thue_morse():
    """
    Thue-Morse Sequence
    OEIS A010060
    """
    
    S = [0]
    
    yield 0
    
    while True:
        new = []
        
        for s in S:
            yield (s+1)%2
            new.append((s+1)%2)
            
        S += new

def co_thue_morse():
    """
    Complement of the Thue-Morse Sequence
    OEIS A010059
    """
    
    S = [1]
    
    yield 1
    
    while True:
        new = []
        
        for s in S:
            yield (s+1)%2
            new.append((s+1)%2)
            
        S += new


def fibonacci_word():
    """
    Fibonacci Word
    OEIS
    """
    
    a,b = (0,),(0,1)
    n = 0
    
    while True:
        for i in range(n,len(b)):
            yield b[i]
        
        n = len(b)
        a,b = b,b+a





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Thue-Morse Sequence")
    simple_test(thue_morse(),18,
                "0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0")
    
    print("\nComplement of the Thue-Morse Sequence")
    simple_test(co_thue_morse(),18,
                "1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1")
    
    print("\nInfinite Fibonacci Word")
    simple_test(fibonacci_word(),18,
                "0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1")