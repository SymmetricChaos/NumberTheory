from Sequences.MathUtils import digits_to_int, int_to_digits
from Sequences.ModularArithmetic import weyl
from Sequences.NiceErrorChecking import require_integers

from math import gcd

# Obviously these are all VERY inefficient

def _check_LFSR_args(vector,taps):
    
    if type(vector) != list:
        raise Exception("The vector must be a list")
    if type(taps) != list:
        raise Exception("The taps must be a list")
    
    for v in vector:
        if v not in (0,1):
            raise Exception("Vector must consist only of 1s and 0s")
    for t in taps:
        if t >= len(vector):
            raise Exception("Taps must be valid positions in the vector")


def LCG(x,a,c,m):
    """Linear Congruential Generator"""
    
    require_integers(["x","a","c","m"],[x,a,c,m])
    
    while True:
        yield x
        x = ((a*x)+c)%m


def aLFG(a,b,m):
    """Additive Lagged Fibonacci Generator"""
    
    require_integers(["a","b","m"],[a,b,m])
    
    while True:
        yield a
        a,b = b,(a+b)%m


def mLFG(a,b,m):
    """Multiplicative Lagged Fibonacci Generator"""
    
    require_integers(["a","b","m"],[a,b,m])
    
    while True:
        yield a
        a,b = b,(a*b)%m


def gLFG(a,b,m,func):
    """Generalized Lagged Fibonacci Generator"""
    
    require_integers(["a","b","m"],[a,b,m])
    
    while True:
        yield a
        a,b = b,func(a,b)%m


def LFSR(vector,taps):
    """Linear Feedback Shift Register: Returns the state at each step"""
    
    _check_LFSR_args(vector,taps)
    
    while True:
        yield digits_to_int(vector,2,bigendian=True)
        vector = vector[1:] + [sum([vector[i] for i in taps])%2]


def middle_square(n):
    """Middle Square Method"""
    
    require_integers(["n"],[n])
    
    N = int_to_digits(n)
    width = len(N)+(len(N)%2)
    
    while True:
        a = n*n
        A = int_to_digits(a)
        
        if len(A) % 2 == 1:
            A = [0] + A
        
        n = digits_to_int(A[width//2:-width//2])
        
        yield n


def middle_square_weyl(n,k,m):
    """Middle Square Method Augmented with a Weyl Sequence"""
    
    # Only n has to be checked since the weyl() function will check k and m
    require_integers(["n"],[n])
    
    W = weyl(k,m)
    
    N = int_to_digits(n)
    width = len(N)+(len(N)%2)
    
    for w in W:
        a = n*n+w
        A = int_to_digits(a)
        
        if len(A) % 2 == 1:
            A = [0] + A
        
        n = digits_to_int(A[width//2:-width//2])
        
        yield n


def blum_blum_shub(x,p,q):
    """
    Blum Blum Shub PRNG
    M must be a semiprime but this is not checked
    """
    
    M = p*q
    
    if gcd(M,x) != 1:
        raise Exception("x must be coprime to M")
    if x in (0,1):
        raise Exception("x cannot be 0 or 1")
    if p%4:
        raise Exception("p must be congruent to 3 mod 4")
    if q%4:
        raise Exception("q must be congruent to 3 mod 4")
    
    while True:
        yield x
        
        x = (x*x)%M





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Linear Congruential Generator")
    simple_test(LCG(9,5,17,97),14,
                "9, 62, 36, 3, 32, 80, 29, 65, 51, 78, 19, 15, 92, 89")
    
    print("\nLagged Fibonacci Generator")
    simple_test(mLFG(9,27,97),14,
                "9, 27, 49, 62, 31, 79, 24, 53, 11, 1, 11, 11, 24, 70")
    
    print("\nLinear Feedback Shift Register")
    simple_test(LFSR([1,0,0,1,0,1,1,0],[0,3,6,7]),11,
                "105, 180, 218, 237, 118, 187, 221, 110, 55, 155, 205")
    
    print("\nMiddle-Square Method")
    simple_test(middle_square(675248),6,
                "959861, 333139, 981593, 524817, 432883, 387691")
    
    print("\nMiddle-Square Weyl")
    simple_test(middle_square_weyl(675248,5743,7899),6,
                "959861, 333145, 985594, 395534, 447152, 944916")
    
    # print("\nBlum Blum Shub")
    # simple_test(blum_blum_shub(17,101,71),10,
    #             "17, 289, 523, 1480, 175, 1422, 929, 784, 1393, 755")
    