from Sequences.Simple import naturals, integers, arithmetic
from Sequences.MathUtils import choose
from math import floor, log2
from Sequences.Primes import primes
from Sequences.NiceErrorChecking import require_integers, require_positive, require_nonnegative


def polygonal(S=1):
    """Polygonal Numbers"""
    
    require_integers(["S"],[S])
    require_positive(["S"],[S])
    
    for n in naturals():
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def gen_polygonal(S=1):
    """Generalized Polygonal Numbers"""
    
    require_integers(["S"],[S])
    require_positive(["S"],[S])
    
    for n in integers():
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def cen_polygonal(S=1):
    """Centered Polygonal Numbers"""
    
    require_integers(["S"],[S])
    require_positive(["S"],[S])
    
    for n in naturals(1):
        yield (S*n) // 2 * (n-1)+1


def simplicial(N=1):
    """Simplicial Numbers: Generalization of triangular numbers to N dimensions"""
    
    require_integers(["N"],[N])
    require_positive(["N"],[N])
    
    yield 0
    
    for n in naturals():
        yield choose(n+N,N)


def perfect_powers():
    """Perfect Powers: Non-negative integers that can be written as a a perfect power"""
    
    yield 0
    yield 1
    
    for n in naturals(2):
        lim = floor(log2(n))+2
        
        for i in primes():
            ctr = 2
            
            while True:
                pwr = ctr**i
                
                if pwr > n:
                    break
                
                if pwr == n:
                    yield n
                    break
                
                ctr += 1
            
            if i > lim:
                break


def doubly_polygonal(S=1):
    """Doubly Polygonal Numbers"""
    
    require_integers(["S"],[S])
    require_positive(["S"],[S])
    
    cur = 0
    P = polygonal(S)
    
    for s in polygonal(S):
        skip = s-cur-1
        
        for n in range(skip):
            next(P)
        
        yield next(P)
        
        cur = s


def hypercube(e=0):
    """Hypercube Numbers: Each non-negative integer raised to the power of e"""
    
    require_integers(["e"],[e])
    require_nonnegative(["e"],[e])
    
    for n in naturals():
        yield n**e


def gen_hypercube(e=0):
    """Generalized Hypercube Numbers: Each integer raised to the power of e"""
    
    require_integers(["e"],[e])
    require_nonnegative(["e"],[e])
    
    for i in integers():
        yield i**e


### More efficient calculation for common polygonal numbers ###
def triangular():
    """Triangular Numbers"""
    
    S = 0
    
    for a in naturals():
        S += a
        yield S


def square():
    """Square Numbers"""
    
    S = 0
    
    for a in arithmetic(1,2):
        yield S
        S += a


def pentagonal():
    """Pentagonal Numbers"""
    
    for n in naturals():
        yield (3*n*n-n)//2


def gen_pentagonal():
    """Generalized Pentagonal Numbers"""
    
    for i in integers():
        yield (3*i*i-i)//2





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Triangular Numbers")
    simple_test(triangular(),10,
                "0, 1, 3, 6, 10, 15, 21, 28, 36, 45")
    
    print("\nSquare Numbers")
    simple_test(square(),10,
                "0, 1, 4, 9, 16, 25, 36, 49, 64, 81")
    
    print("\nPentagonal Numbers")
    simple_test(pentagonal(),10,
                "0, 1, 5, 12, 22, 35, 51, 70, 92, 117")
    
    print("\nGeneralized Pentagonal Numbers")
    simple_test(gen_pentagonal(),10,
                "0, 1, 2, 5, 7, 12, 15, 22, 26, 35")
    
    print("\nHexagonal Numbers")
    simple_test(polygonal(6),10,
                "0, 1, 6, 15, 28, 45, 66, 91, 120, 153")
    
    print("\nGeneralized Ocatagonal Numbers")
    simple_test(gen_polygonal(8),10,
                "0, 1, 5, 8, 16, 21, 33, 40, 56, 65")
    
    print("\nCentered Square Numbers")
    simple_test(cen_polygonal(4),10,
                "1, 5, 13, 25, 41, 61, 85, 113, 145, 181")
    
    print("\nTetrahedral Numbers")
    simple_test(simplicial(3),10,
                "0, 1, 4, 10, 20, 35, 56, 84, 120, 165")
    
    # Differs from the OEIS definition by inclusion of 0
    print("\nPerfect Powers")
    simple_test(perfect_powers(),10,
                "0, 1, 4, 8, 9, 16, 25, 27, 32, 36")
    
    print("\nDoubly Pentagonal Numbers")
    simple_test(doubly_polygonal(5),8,
                "0, 1, 35, 210, 715, 1820, 3876, 7315")
    
    print("\nCubic Numbers")
    simple_test(hypercube(3),9,
                "0, 1, 8, 27, 64, 125, 216, 343, 512")
    
    print("\nGeneralized Cubic Numbers")
    simple_test(gen_hypercube(3),9,
                "0, 1, -1, 8, -8, 27, -27, 64, -64")