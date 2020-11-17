from Sequences.Simple import naturals
from Sequences.MathUtils import factor_out_twos
from Sequences.Recurrence import tribonacci
from Sequences.Manipulations import offset

from itertools import cycle

def thue_morse(invert=False):
    """
    Thue-Morse Sequence
    
    Args:
        invert -- bool, give the complement
    
    OEIS A010060
    """
    
    if invert:
        S = [1]
        yield 1
    else:
        S = [0]
        yield 0
    
    D = {0:1, 1:0}
    
    while True:
        for s in S[:]:
            yield D[s]
            S.append(D[s])


def thue_morse_words(invert=False):
    """
    Generations of the Thue-Morse Sequence
    
    Args:
        invert -- bool, give the complement
    
    OEIS
    """
    
    if invert:
        S = [1]
    else:
        S = [0]
    
    D = {0:1, 1:0}
    
    while True:
        yield tuple(S)
        
        for s in S[:]:
            S.append(D[s])


def fibonacci_word(invert=False):
    """
    The Infinite Fibonacci Word
    
    Args:
        invert -- bool, give the complement
    
    OEIS A003849
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


def fibonacci_words(invert=False):
    """
    Each Finite Fibonacci Word
    
    Args:
        invert -- bool, give the complement
    
    OEIS
    """
    
    if invert:
        a,b = (1,),(1,0)
    else:
        a,b = (0,),(0,1)
    
    while True:
        yield a
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


def cantor_set(invert=False):
    """
    The Cantor Ternary Set
    
    Args:
        invert -- bool, give the complement
    
    OEIS
    """
    
    if invert:
        yield 1
        S = (1,)
    else:
        yield 0
        S = (0,)
    
    if invert:
        while True:
            for i in range(len(S)):
                yield 0
            
            yield from S
            
            S = S + (0,)*len(S) + S
    
    else:
        while True:
            for i in range(len(S)):
                yield 1
            
            yield from S
            
            S = S + (1,)*len(S) + S


def cantor_sets(invert=False):
    """
    Generations of the Cantor Ternary Set
    
    Args:
        invert -- bool, give the complement
    
    OEIS
    """
    
    if invert:
        D = {1:(1,0,1), 0:(0,0,0)}
        S = (1,)
    else:
        D = {0:(0,1,0), 1:(1,1,1)}
        S = (0,)
    
    while True:
        yield S
        
        new = ()
        for s in S:
            new += D[s]
        
        S = new


def paperfolding_word(invert=False):
    """
    Infinite Regular Paperfolding Word
    
    Args:
        invert -- bool, give the complement
    
    OEIS A014577
    """
    
    for n in naturals(1):
        d,s = factor_out_twos(n)
        
        if invert:
            if d % 4 == 1:
                yield 0
            else:
                yield 1
        else:
            if d % 4 == 1:
                yield 1
            else:
                yield 0


def paperfolding_words(invert=False):
    """
    Generations of the Regular Paperfolding Word by Interpolation
    
    Args:
        invert -- bool, give the complement
    
    OEIS
    """
    
    if invert:
        S = (0,)
        
        while True:
            yield S
            
            new = [0]
            C = cycle([1,0])
            
            for s,c in zip(S,C):
                new += [s,c]
            
            S = tuple(new)
        
    else:
        S = (1,)
        
        while True:
            yield S
            
            new = [1]
            C = cycle([0,1])
            
            for s,c in zip(S,C):
                new += [s,c]
            
            S = tuple(new)


def tribonnaci_vectors():
    """
    Unique representation of each natural in the tribonacci base\n
    OEIS A278038
    """
    
    trib = offset(tribonacci(),4)
    T = [1]
    
    yield (0,)
    
    for n in naturals(1):
        if T[-1] < n:
            T.append(next(trib))
        
        out = []
        
        for t in reversed(T):
            if n >= t:
                out.append(1)
                n -= t
            
            else:
                if 1 in out:
                    out.append(0)
        
        yield tuple(out)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Thue-Morse Sequence")
    simple_test(thue_morse(),18,
                "0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0")
    
    print("\nThue-Morse Words")
    simple_test(thue_morse_words(),4,
                "(0,), (0, 1), (0, 1, 1, 0), (0, 1, 1, 0, 1, 0, 0, 1)")
    
    print("\nInfinite Fibonacci Word")
    simple_test(fibonacci_word(),18,
                "0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1")
    
    print("\nFinite Fibonacci Words")
    simple_test(fibonacci_words(),4,
                "(0,), (0, 1), (0, 1, 0), (0, 1, 0, 0, 1)")
    
    print("\nGray Codes")
    simple_test(gray_codes(),6,
                "(0,), (1,), (1, 1), (1, 0), (1, 1, 0), (1, 1, 1)")
    
    print("\nInfinite Cantor Set")
    simple_test(cantor_set(),18,
                "0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1")
    
    print("\nGenerations of the Cantor Sets")
    simple_test(cantor_sets(),3,
                "(0,), (0, 1, 0), (0, 1, 0, 1, 1, 1, 0, 1, 0)")
    
    print("\nInfinite Paperfolding Word")
    simple_test(paperfolding_word(),18,
                "1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1")
    
    print("\nGenerations of the Paperfolding Word")
    simple_test(paperfolding_words(),3,
                "(1,), (1, 1, 0), (1, 1, 0, 1, 1, 0, 0)")
    
    print("\nTribonacci Vector Representation of Each Natural")
    simple_test(tribonnaci_vectors(),6,
                "(0,), (1,), (1, 0), (1, 1), (1, 0, 0), (1, 0, 1)")
    