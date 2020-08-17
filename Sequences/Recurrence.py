from NiceErrorChecking import require_integers, require_geq

def fibonacci():
    """Fibonacci Sequence"""
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+b


def lucas():
    """Lucas Sequence"""
    
    a = 2
    b = 1
    
    while True:
        yield a
        a, b = b, a+b


def PQ_fibonacci(P=1,Q=1):
    """
    P,Q-Fibonacci Sequence
    
    Args:
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["P","Q"],[P,Q])
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, Q*a+P*b


def PQ_lucas(P=1,Q=1):
    """
    P,Q-Lucas Sequence

    Args:
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["P","Q"],[P,Q])
    
    a = 2
    b = P
    
    while True:
        yield a
        a, b = b, Q*a+P*b


def pell():
    """Pell Numbers"""
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+2*b


def companion_pell():
    """Companion Pell Numbers"""
    
    a = 2
    b = 2
    
    while True:
        yield a
        a, b = b, a+2*b


def simple_recurrence(a,b):
    """
    Additive recurrence based relation on two terms
    
    Args:
        a -- first term
        b -- second term
    """
    
    require_integers(["a","b"],[a,b])
    
    while True:
        yield a
        a, b = b, a+b


def PQ_simple_recurrence(a,b,P,Q):
    """
    Additive recurrence based relation on two terms
    
    Args:
        a -- first term
        b -- second term
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["a","b","P","Q"],[a,b,P,Q])
    
    while True:
        yield a
        a, b = b, Q*a+P*b


def leonardo():
    """Leonardo Numbers"""
    
    a,b = 1,1
    
    while True:
        yield a
        a,b = b,a+b+1


def tribonacci():
    """Tribonacci Sequence"""
    
    a = 0
    b = 0
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b+c


def multi_fibonacci(n):
    """Higher Order Fibonacci Sequence"""
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],2)
    
    S = [0]*(n-1)+[1]
    
    while True:
        yield S[0]
        S = S[1:] + [sum(S)]


def padovan():
    """Padovan Sequence"""
    
    a = 1
    b = 0
    c = 0
    
    while True:
        yield a
        a, b, c = b, c, a+b


def narayana():
    """Narayana Sequence"""
    
    a = 1
    b = 1
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+c



def padovan_spiral():
    """Padovan's Spiral Sequence"""
    
    a = 1
    b = 1
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b


def arbitrary_recurrence(S,func):
    """
    Recurrence based sequence given a starting list and a function
    
    Args:
        S -- Starting list
        func -- A function that that will take in S and return the next value of S
    """
    
    if type(S) != list:
        raise Exception(f"S must be of type list not {type(S)}")
    
    for i in S:
        if type(i) != int:
            raise Exception(f"All elements of S must be of type int not {type(i)}")
    
    
    while True:
        yield S[0]
        S = S[1:] + [func(S)]


def sylvesters_sequence():
    """Sylvester's Sequence: Product of previous terms plus 1"""
    
    v = 2
    
    while True:
        yield v
        
        v = v*v-v+1





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Fibonacci Sequence")
    simple_test(fibonacci(),10,
                "0, 1, 1, 2, 3, 5, 8, 13, 21, 34")
    
    print("\nLucas Sequence")
    simple_test(lucas(),10,
                "2, 1, 3, 4, 7, 11, 18, 29, 47, 76")
    
    print("\n(2,3)-Fibonacci Sequence")
    simple_test(PQ_fibonacci(2,3),10,
                "0, 1, 2, 7, 20, 61, 182, 547, 1640, 4921")
    
    print("\n(2,3)-Lucas Sequence")
    simple_test(PQ_lucas(2,3),10,
                "2, 2, 10, 26, 82, 242, 730, 2186, 6562, 19682")
    
    print("\nPell Numbers")
    simple_test(pell(),10,
                "0, 1, 2, 5, 12, 29, 70, 169, 408, 985")
    
    print("\nCompanion Pell Numbers")
    simple_test(companion_pell(),10,
                "2, 2, 6, 14, 34, 82, 198, 478, 1154, 2786")
    
    print("\nSimple Recurrence for a = 7, b = 9")
    simple_test(simple_recurrence(7,9),10,
                "7, 9, 16, 25, 41, 66, 107, 173, 280, 453")
    
    print("\nTribonacci")
    simple_test(tribonacci(),10,
                "0, 0, 1, 1, 2, 4, 7, 13, 24, 44")
    
    print("\nTetranacci")
    simple_test(multi_fibonacci(4),10,
                "0, 0, 0, 1, 1, 2, 4, 8, 15, 29")
    
    print("\nPadovan")
    simple_test(padovan(),10,
                "1, 0, 0, 1, 0, 1, 1, 1, 2, 2")
    
    print("\nPadovan's Spiral")
    simple_test(padovan_spiral(),10,
                "1, 1, 1, 2, 2, 3, 4, 5, 7, 9")
    
    print("\nSylvester's Sequence")
    simple_test(sylvesters_sequence(),6,
                "2, 3, 7, 43, 1807, 3263443")
    
    print("\nNarayana's Sequence")
    simple_test(narayana(),10,
                "1, 1, 1, 2, 3, 4, 6, 9, 13, 19")
    
    from math import floor, sqrt
    print("\nArbitrary Reccurence with f(a,b,c) = ⌊2√(a+b+c)⌋+a\nand initial state 1, 1, 1")
    simple_test(arbitrary_recurrence([1,1,1],lambda x: floor(2*sqrt(x[0]+x[1]+x[2]))+x[0]),10,
                "1, 1, 1, 4, 5, 7, 12, 14, 18, 25")
    
    