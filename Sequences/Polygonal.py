from Sequences.Simple import naturals, integers, arithmetic, sign_sequence
from math import floor, log2, comb
from Sequences.Primes import primes
from Sequences.NiceErrorChecking import require_integers, require_positive, \
                                        require_nonnegative, require_geq
from Sequences.SequenceManipulation import offset, sequence_apply

def polygonal(S=2):
    """
    Polygonal Numbers: Numbers that form a polygon with S sides in the usual way
    
    Args:
        S -- Number of sides
    
    OEIS A000217, A000290, A000326
    """
    
    require_integers(["S"],[S])
    require_geq(["S"],[S],2)
    
    for n in naturals():
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def gen_polygonal(S=2):
    """
    Generalized Polygonal Numbers: Generalization of polygonal number formula to integers
    
    Args:
        S -- Number of sides
    
    OEIS A001318
    """
    
    require_integers(["S"],[S])
    require_geq(["S"],[S],2)
    
    for n in integers():
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def cen_polygonal(S=2):
    """
    Centered Polygonal Numbers: Numbers that form a polygon with S sides that is centered on an object
    
    Args:
        S -- Number of sides
    
    OEIS A005448, A001844, A005891, A003215, A069099, A016754, A060544, A062786, A069125, A003154
    """
    
    require_integers(["S"],[S])
    require_geq(["S"],[S],2)
    
    for n in naturals(1):
        yield (S*(n*n-n)) // 2 +1


# Should find a mroe efficient way avoiding the choose function
def simplicial(N=1):
    """
    Simplicial Numbers: Generalization of triangular numbers to N dimensions
    
    Args:
        N -- Dimension of the simplex
    
    OEIS A000292, A000332
    """
    
    require_integers(["N"],[N])
    require_positive(["N"],[N])
    
    yield 0
    
    for n in naturals():
        yield comb(n+N,N)


def perfect_powers():
    """
    Perfect Powers: Non-negative integers that can be written as a perfect power\n
    OEIS A001597 (when offset by 1)
    """
    
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


def doubly_polygonal(S=2):
    """
    Doubly Polygonal Numbers: Polygonal numbers that 
    
    Args:
        S -- Number of sides
    
    OEIS A000583, A002817, A063249, A232713
    """
    
    require_integers(["S"],[S])
    require_geq(["S"],[S],2)
    
    cur = 0
    P = polygonal(S)
    
    for s in polygonal(S):
        skip = s-cur-1
        
        for n in range(skip):
            next(P)
        
        yield next(P)
        
        cur = s


def hypercube(e=0):
    """
    Hypercube Numbers: Each non-negative integer raised to the power of e
    
    Args:
        e -- exponent to raise each non-negative integer to
    
    OEIS A000290, A000578, A000583, A000584, A001014, A001015
    """
    
    require_integers(["e"],[e])
    require_nonnegative(["e"],[e])
    
    for n in naturals():
        yield n**e


def gen_hypercube(e=0):
    """
    Generalized Hypercube Numbers: Each integer raised to the power of e
    
    Args:
        e -- exponent to raise each integer to
    
    OEIS
    """
    
    require_integers(["e"],[e])
    require_nonnegative(["e"],[e])
    
    for i in integers():
        yield i**e


def oblong():
    """
    Pronic Numbers: Sums of consecutive non-negative integers\n
    OEIS A002378
    """
    
    S = 0
    
    for a in arithmetic(2,2):
        yield S
        
        S += a


def rectangular(d):
    """
    Rectangular Numbers: Generalization of Pronic Numbers\n
    OEIS A005563, A028552, A028347, A028557, A028560, A028563, A028566,
         A028569, A098603, A119412, A132759, A098847-A098850, A120071,
         A132760-A132773
    """
    
    S = 0
    
    require_integers(["d"],[d])
    require_positive(["d"],[d])
    
    for a in arithmetic(d+1,2):
        yield S
        
        S += a


def square_triangular():
    """
    Square-Triangular Numbers: Positive integers that are both square and triangular\n
    OEIS A001110
    """
    
    a,b = 0,1
    
    while True:
        yield b
        
        a,b = b,34*b-a+2


def square_pyramidal():
    """
    Square Pyramidal Numbers: Positive integers that take the shape of a square based pyramid\n
    OEIS A000330
    """
    
    S = 1
    
    for s in offset(square(),2):
        yield S
        S += s


def squared_triangular():
    """
    Squared Triangular Numbers: Square of each triangular number\n
    OEIS A000537
    """
    
    return sequence_apply(triangular(),lambda x: x*x)


def triangles_in_triangle():
    """
    Number of triangles described by the internal and external edges of a triangle made of identical triangles\n
    OEIS A002717
    """
    
    for n,s in enumerate(sign_sequence(1),0):
        n2 = n*n
        n3 = n2*n
        
        yield (4*n3 + 10*n2 + 4*n + -1 + s)//16





### More efficient calculation for common polygonal numbers ###
def triangular():
    """
    Triangular Numbers\n
    OEIS: A000217
    """
    
    S = 0
    
    for a in naturals():
        S += a
        yield S


def square():
    """
    Square Numbers\n
    OEIS A000290
    """
    
    S = 0
    
    for a in arithmetic(1,2):
        yield S
        S += a


def cubic():
    """
    Cubic Numbers\n
    OEIS A000578
    """
    
    for n in naturals():
        yield n*n*n


def pentagonal():
    """
    Pentagonal Numbers\n
    OEIS A000326
    """
    
    for n in naturals():
        yield (3*n*n-n)//2


def gen_pentagonal():
    """
    Generalized Pentagonal Numbers\n
    OEIS A001318
    """
    
    for i in integers():
        yield (3*i*i-i)//2





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Triangular Numbers")
    simple_test(triangular(),14,
                "0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91")
    
    print("\nSquare Numbers")
    simple_test(square(),13,
                "0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144")
    
    print("\nPentagonal Numbers")
    simple_test(pentagonal(),13,
                "0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210")
    
    print("\nGeneralized Pentagonal Numbers")
    simple_test(gen_pentagonal(),14,
                "0, 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70")
    
    print("\nHexagonal Numbers")
    simple_test(polygonal(6),13,
                "0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276")
    
    print("\nGeneralized Ocatagonal Numbers")
    simple_test(gen_polygonal(8),14,
                "0, 1, 5, 8, 16, 21, 33, 40, 56, 65, 85, 96, 120, 133")
    
    print("\nCentered Triangular Numbers")
    simple_test(cen_polygonal(3),12,
                "1, 4, 10, 19, 31, 46, 64, 85, 109, 136, 166, 199")
    
    print("\nTetrahedral Numbers")
    simple_test(simplicial(3),13,
                "0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364")
    
    print("\nPerfect Powers")
    simple_test(perfect_powers(),14,
                "0, 1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 64, 81")
    
    print("\nDoubly Pentagonal Numbers")
    simple_test(doubly_polygonal(5),10,
                "0, 1, 35, 210, 715, 1820, 3876, 7315, 12650, 20475")
    
    print("\nCubic Numbers")
    simple_test(cubic(),12,
                "0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331")
    
    print("\n4th Powers")
    simple_test(hypercube(4),10,
                "0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561")
    
    print("\nPronic Numbers")
    simple_test(oblong(),13,
                "0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156")
    
    print("\nRectangular Numbers d=2")
    simple_test(rectangular(2),13,
                "0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168")
    
    print("\nSquare-Triangular Numbers")
    simple_test(square_triangular(),7,
                "1, 36, 1225, 41616, 1413721, 48024900, 1631432881")
    
    print("\nSquare Pyramidal Numbers")
    simple_test(square_pyramidal(),12,
                "1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506, 650")
    
    print("\nSquared Triangular Numbers")
    simple_test(squared_triangular(),11,
                "0, 1, 9, 36, 100, 225, 441, 784, 1296, 2025, 3025")
    
    print("\nSolutions to the Matchstick Triangle Puzzle")
    simple_test(triangles_in_triangle(),13,
                "0, 1, 5, 13, 27, 48, 78, 118, 170, 235, 315, 411, 525")
    