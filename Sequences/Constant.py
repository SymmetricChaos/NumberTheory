from Sequences.MathUtils import int_to_digits, real_sum, real_diff, real_prod_nat, real_div_nat
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
    Decimal Digits of Pi\n
    OEIS A000796
    """
    
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


def sqrt_digits(n,B=10):
    """
    Digits of the square root of n in base B\n
    OEIS A002193, A002194, A002163, A010465, A010466, A010467, A010464, 
         A010472, A010468, A010490, A010469, A010470, A010471, A010477,
         A010473, A010524, A010474
    """
    
    require_integers(["n","B"],[n,B])
    require_nonnegative(["n"],[n])
    require_geq(["B"],[B],2)
    
    Bsq = B*B
    p,r = 0,0
    
    chunks = int_to_digits(n,Bsq)
    
    for d in chain(chunks,constant(0)):
        c = Bsq*r+d
        x = -1
        
        for i in range(B):
            x += 1
            
            if x*(x+(2*B*p)) > c:
                x -= 1
                break
        
        r = c - x*(x+2*B*p)
        p = B*p+x
        
        yield x


def root_digits(n,a,B=10):
    """
    Digits of the nth root of a in base B\n
    OEIS
    """
    
    require_integers(["a","n","B"],[a,n,B])
    require_nonnegative(["a"],[a])
    require_geq(["n","B"],[n,B],2)
    
    Bpow = B**n
    chunks = int_to_digits(a,Bpow)
    
    r,y = 0,0
    
    for d in chain(chunks,constant(0)):
        c = Bpow*r+d
        x = 0
        
        for i in range(B):
            x += 1
            
            if (B*y+x)**n - (Bpow*y**n) > c:
                x -= 1
                break
        
        y1 = B*y+x
        r1 = c - ((B*y+x)**n - (Bpow*y**n))
        
        r,y = r1,y1
        
        yield x


# Not sure why this doesn't work in other bases
def phi_digits():
    """
    Phi: Digits of the golden ratio\n
    OEIS A001622
    """
    
    # Digits of the square root of 5
    S = sqrt_digits(5,10)
    
    # Skip the first two and yield 1 then 6
    next(S)
    next(S)
    
    yield 1
    yield 6
    
    # Divide remaining part by 2
    for d in real_div_nat(S,2,10):
        yield d





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Pi, the Circle Constant")
    simple_test(pi_digits(),18,
                "3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3")
    
    print("\nTau, Twice Pi")
    simple_test(real_prod_nat(pi_digits(),2,),18,
                "6, 2, 8, 3, 1, 8, 5, 3, 0, 7, 1, 7, 9, 5, 8, 6, 4, 7")
    
    print("\nPhi, The Golden Ratio")
    simple_test(phi_digits(),18,
                "1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4")
    
    print("\nSquare Root of 2")
    simple_test(sqrt_digits(2),18,
                "1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7, 3, 0, 9, 5, 0, 4")
    
    print("\nBits of the Square Root of 2")
    simple_test(sqrt_digits(2,B=2),18,
                "1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1")
    
    print("\nCube Root of 3")
    simple_test(root_digits(3,3),18,
                "1, 4, 4, 2, 2, 4, 9, 5, 7, 0, 3, 0, 7, 4, 0, 8, 3, 8")
    
    print("\n4th Root of 2")
    simple_test(root_digits(4,2),18,
                "1, 1, 8, 9, 2, 0, 7, 1, 1, 5, 0, 0, 2, 7, 2, 1, 0, 6")
    
    print("\n2√2")
    simple_test(real_sum(sqrt_digits(2),sqrt_digits(2)),18,
                "2, 8, 2, 8, 4, 2, 7, 1, 2, 4, 7, 4, 6, 1, 9, 0, 0, 9")
    
    print("\n√(2)/2")
    simple_test(real_div_nat(sqrt_digits(2),2),18,
                "0, 7, 0, 7, 1, 0, 6, 7, 8, 1, 1, 8, 6, 5, 4, 7, 5, 2")
    
    print("\n√2 - ∛2")
    simple_test(real_diff(root_digits(2,2),root_digits(3,2)),18,
                "0, 1, 5, 4, 2, 9, 2, 5, 1, 2, 4, 7, 8, 2, 2, 1, 8, 8")
    