from Sequences.MathUtils import int_to_digits, real_sum, real_prod_nat, real_div_nat
from NiceErrorChecking import require_integers, require_nonnegative, require_geq
from itertools import chain, dropwhile
from Sequences.Simple import constant, naturals

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
def metallic_ratio_digits(n):
    """
    Digits of the Nth Metallic Ratio\n
    OEIS 
    """
    
    # Prepend zeroes
    N = [n]
    m = 10
    dig = 0
    while m <= n:
        m *= 10
        dig += 1
    
    N = [0]*dig + N

    # (n + √(n+4))/2
    M = real_div_nat(real_sum(N,sqrt_digits(n*n+4)),2)
    
    yield from dropwhile(lambda x: x == 0,M)


def phi_digits():
    """
    Phi: Digits of the golden ratio\n
    OEIS A001622
    """
    
    yield from metallic_ratio_digits(1)


def silver_ratio_digits():
    """
    Digits of the silver ratio\n
    OEIS A014176
    """
    
    yield from metallic_ratio_digits(2)


def champernowne_digits(B=10):
    """
    Digits of the base B version of Champernowne's constant
    OEIS A003137, A030302, A030548, A033307, A030373, A031219, A030998, 
         A031035, A031076
    """
    
    for n in naturals(1):
        yield from iter(int_to_digits(n,B))





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
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
    
    print("\nThe Silver Ratio, 1 + √2")
    simple_test(silver_ratio_digits(),18,
                "2, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7, 3, 0, 9, 5, 0, 4")
    
    print("\nThe Bronze Ratio, (3 + √13)/2")
    simple_test(metallic_ratio_digits(3),18,
                "3, 3, 0, 2, 7, 7, 5, 6, 3, 7, 7, 3, 1, 9, 9, 4, 6, 4")
    
    print("\nThe 10th Metallic Ratio, (10 + √104)/2")
    simple_test(metallic_ratio_digits(10),18,
                "1, 0, 0, 9, 9, 0, 1, 9, 5, 1, 3, 5, 9, 2, 7, 8, 4, 8")
    
    print("\nBits of the Square Root of 2")
    simple_test(sqrt_digits(2,B=2),18,
                "1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1")
    
    print("\nCube Root of 3")
    simple_test(root_digits(3,3),18,
                "1, 4, 4, 2, 2, 4, 9, 5, 7, 0, 3, 0, 7, 4, 0, 8, 3, 8")
    
    print("\n4th Root of 2")
    simple_test(root_digits(4,2),18,
                "1, 1, 8, 9, 2, 0, 7, 1, 1, 5, 0, 0, 2, 7, 2, 1, 0, 6")
    
    print("\nBase 10 Champernowne's Constant")
    simple_test(champernowne_digits(),18,
                "1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1")
    
    print("\nBase 2 Champernowne's Constant")
    simple_test(champernowne_digits(2),18,
                "1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1")