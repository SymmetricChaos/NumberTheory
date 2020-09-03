from Sequences.MathUtils import int_to_digits
from NiceErrorChecking import require_integers, require_nonnegative, require_geq
from itertools import chain
from Sequences.Simple import constant

# Would like to restrict this to streaming algorithms that can keep producing 
# digits

# This is a spigot algorithm for pi
# On my machine its almost instantaneous out to about 1500 digits
# I do not understand this algorithm right now
def pi_digits():
    """
    Decimal Digits of Pi
    OEIS A000796
    """
    
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


def sqrt_digits(n,B):
    """
    Digits of the square root of n in base B
    OEIS A002193, A002194, A002163, A010465, A010466, A010467, A010464, 
         A010472, A010468, A010490, A010469, A010470, A010471, A010477,
         A010473, A010524, A010474
    """
    
    require_integers(["n","B"],[n,B])
    require_nonnegative(["n"],[n])
    require_geq(["B"],[B],2)
    
    if n == 0:
        yield 0
    
    if n == 1:
        yield 1
    
    Bsq = B*B
    p,r = 0,0
    
    chunks = [i for i in int_to_digits(n,Bsq)]
    
    for d in chain(chunks,constant(0)):
        c = Bsq*r+d
        x = 0
        
        for i in range(B):
            x += 1
            
            if x*(x+(2*B*p)) > c:
                x -= 1
                break
        
        r = c - x*(x+2*B*p)
        p = B*p+x
        
        yield x
        
        if r == 0:
            break



# def root_digits(a,n,B):
#     """
    
#     OEIS
#     """
    
#     digits = int_to_digits(a,B)
    
#     x,y,r = 0,0,0
    
#     while True:
        



if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Decimal Digits of Pi")
    simple_test(pi_digits(),18,
                "3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3")
    
    print("\nDecimal Digits of the Square Root of 2")
    simple_test(sqrt_digits(2,10),18,
                "1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7, 3, 0, 9, 5, 0, 4")
    
    print("\nBits of the Square Root of 2")
    simple_test(sqrt_digits(2,2),18,
                "1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1")
