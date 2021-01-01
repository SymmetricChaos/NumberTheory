from Sequences.NiceErrorChecking import require_integers, require_geq, require_rationals
from Sequences.Simple import evens, naturals
from Sequences.Manipulations import offset

from fractions import Fraction
from math import floor, ceil, gcd
from collections import Counter

def fibonacci():
    """
    Fibonacci Sequence: Sum of successive terms, special case of a Lucas Sequence of the 1st kind\n
    OEIS A000045
    """
    
    a,b = 0,1
    
    while True:
        yield a
        a, b = b, a+b


def lucas():
    """
    Lucas Numbers: Sum of successive terms, special case of a Lucas Sequence of the 2nd kind\n
    OEIS A000032
    """
    
    a,b = 2,1
    
    while True:
        yield a
        a, b = b, a+b


def lucas_U(P=1,Q=-1):
    """
    Lucas Sequence of the first kind sometimes abbreviated U
    
    Args:
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["P","Q"],[P,Q])
    
    a,b = 0,1
    
    while True:
        yield a
        a, b = b, P*b-Q*a


def lucas_V(P=1,Q=-1):
    """
    Lucas Sequence of the second kind sometimes abbreviated V
    
    Args:
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["P","Q"],[P,Q])
    
    a, b = 2, P
    
    while True:
        yield a
        a, b = b, P*b-Q*a


def signature_function(signature):
    """
    Recursive Signature Function: Generalization of the PQ-Lucas Sequences
    
    Args:
        signature -- tuple used to multiply terms of the recurrence
    """
    
    L = [0]*(len(signature)-1)
    L += [1]
    C = [i for i in reversed(signature)]
    
    while True:
        yield L[-1]
        L.append(sum([a*b for a,b in zip(L,C)]))
        L.pop(0)


def pell():
    """
    Pell Numbers: Denominators of the continued fraction converts of the square root of two\n
    OEIS A000129
    """
    
    a,b = 0,1
    
    while True:
        yield a
        a, b = b, a+2*b


def companion_pell():
    """
    Companion Pell Numbers: Numerators of the continued fraction converts of the square root of two\n
    OEIS A002203
    """
    
    a,b = 2,2
    
    while True:
        yield a
        a, b = b, a+2*b


def jacobsthal():
    """
    Jacobsthal Numbers\n
    OEIS A001045
    """
    
    a,b = 0,1
    
    while True:
        yield a
        a,b = b,2*a+b


def simple_recurrence(a,b,operation="+"):
    """
    Recurrence on successive values of a sequence using an arithmetic operation
    
    Args:
        a -- integer, first term
        b -- integer, second term
        operation -- string, operation to be used chosen from: +,-,*,/,**
    """
    
    require_integers(["a","b"],[a,b])
    
    O = {"+": lambda x,y: x+y,
         "-": lambda x,y: x-y,
         "*": lambda x,y: x*y,
         "**": lambda x,y: x**y}
    
    func = O[operation]
    
    while True:
        yield a
        a, b = b, func(a,b)


def leonardo():
    """
    Leonardo Numbers\n
    OEIS A001595
    """
    
    a,b = 1,1
    
    while True:
        yield a
        a,b = b,a+b+1


def tribonacci():
    """
    Tribonacci Sequence\n
    OEIS A000073
    """
    
    a,b,c = 0,0,1
    
    while True:
        yield a
        a, b, c = b, c, a+b+c


def tribonnaci_words(index=0):
    """
    Finite the Tribonnaci Words
    
    Args:
        index -- 0 or 1, value to start counting from
    
    OEIS
    """
    
    if index not in (0,1):
        raise ValueError("Index must be zero or one")
    
    if index == 0:
        a = (0,)
        b = (0,1)
        c = (0,1,0,2)
    else:
        a = (1,)
        b = (1,2)
        c = (1,2,1,3)
    
    while True:
        yield a
        a,b,c = b,c,c+b+a


def tribonnaci_word(index=0):
    """
    Infinite Tribonnaci Word
    
    Args:
        index -- 0 or 1, value to start counting from
    
    OEIS A080843, A092782
    """
    
    if index not in (0,1):
        raise ValueError("Index must be zero or one")
    
    n = 0
    for T in tribonnaci_words(index):
        yield from T[n:]
        n = len(T)


def multi_fibonacci(n):
    """
    Higher Order Fibonacci Sequences\n
    OEIS A000073, A000078, A001591, A001592
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],2)
    
    S = [0]*(n-1)+[1]
    
    while True:
        yield S[0]
        S = S[1:] + [sum(S)]


def padovan():
    """
    Padovan Sequence\n
    OEIS A000931
    """
    
    a,b,c = 1,0,0
    
    while True:
        yield a
        a, b, c = b, c, a+b


def padovan_spiral():
    """
    Padovan's Spiral Sequence\n
    OEIS A134816
    """
    
    a,b,c = 1,1,1
    
    while True:
        yield a
        a, b, c = b, c, a+b


def narayana_cows():
    """
    Narayana's Cows Sequence\n
    OEIS A000930
    """
    
    a,b,c = 1,1,1
    
    while True:
        yield a
        a, b, c = b, c, a+c


def sylvester():
    """
    Sylvester's Sequence: Product of previous terms plus one\n
    OEIS A000058
    """
    
    v = 2
    
    while True:
        yield v
        
        v = v*v-v+1


def pisot_E(a,b):
    """
    Pisot E-Sequence
    
    Args:
        a -- first term
        b -- second term
    
    OEIS A008776, A020701, A020720, A020707, A020706, A020695, A020729,
         A010904, A010916, A007699, A010900, A010903, A010912, A010914,
         A020711, A020717, A010901, A010902, A010905, A010907, A010911,
         A010913, A020708, A020721, A048575, A010908, A010909, A010910,
         A010915, A010917, A010924, A014001, A014002, A014003, A014004,
         A014005, A014006, A014007, A014008, A020704, A020709, A020712,
         A020713, A020716, A020718, A274951, A275628, A276396
    """
    
    require_integers(["a","b"],[a,b])
    require_geq(["a"],[a],1)
    
    if a >= b:
        raise ValueError("The first two terms of a Pisot sequence must be increasing")
    
    while True:
        yield a
        a,b = b,floor((b*b)/a + .5)


def pisot_L(a,b):
    """
    Pisot L-Sequence
    
    Args:
        a -- first term
        b -- second term
    
    OEIS A008776, A018910, A020737, A020707, A020706, A020729, A048577,
         A048578, A048580, A020717, A020743, A048583, A048584, A048585,
         A048586, A020730, A020734, A020736, A048575, A048582, A048587,
         A048588, A048590, A277084, A048576, A048579, A048589, A048591,
         A048592, A121605, A277088, A277089
    """
    
    require_integers(["a","b"],[a,b])
    require_geq(["a"],[a],1)
    
    if a >= b:
        raise ValueError("The first two terms of a Pisot sequence must be increasing")
    
    while True:
        yield a
        a,b = b,ceil((b*b)/a)


def pisot_P(a,b):
    """
    Pisot P-Sequence
    
    Args:
        a -- first term
        b -- second term
    
    OEIS A008776, A020701, A021006, A020720, A020707, A020727, A020729,
         A021001, A010912, A020711, A048625, A010901, A020708, A020721,
         A021008, A021013, A048626, A020704, A020712, A020713, A020716,
         A020718, A020744, A021004, A021011
    """
    
    require_integers(["a","b"],[a,b])
    require_geq(["a"],[a],1)
    
    if a >= b:
        raise ValueError("The first two terms of a Pisot sequence must be increasing")
    
    while True:
        yield a
        a,b = b,ceil((b*b)/a - .5)


def pisot_T(a,b):
    """
    Pisot T-Sequence
    
    Args:
        a -- first term
        b -- second term
    
    OEIS A008776, A010925, A020707, A010919, A018919, A020729, A010920,
         A018921, A020742, A020745, A018914, A020746, A010922, A018915,
         A018917, A018918, A018920, A018922, A019492, A020747, A020748,
         A020749, A020750, A018923, A020728, A020732, A020741, A020744,
         A020751, A020752, A022034, A022039, A275904, A278681, A278692,
         A278764
    """
    
    require_integers(["a","b"],[a,b])
    require_geq(["a"],[a],1)
    
    if a >= b:
        raise ValueError("The first two terms of a Pisot sequence must be increasing")
    
    while True:
        yield a
        a,b = b,(b*b)//a


def ulam(u=1,v=2):
    """
    Ulam Sequence
    
    Args:
        u -- first term
        v -- second term
    
    OEIS A002858
    """
    
    T = [u,v]
    S = Counter({u+v:1})
    
    yield u
    yield v
    
    while True:
        new = min([v for v,c in S.items() if c == 1])
        yield new
        T.append(new)
        
        for term in T[:-1]:
            S[new+term] += 1
        
        del S[new]


def semifibonacci():
    """
    The Semi-Fibonacci Sequence\n
    OEIS A030067
    """
    
    L = [1]
    
    for e in offset(evens(),1):
        yield L[-1]
        L.append(L[e//2-1])
        
        yield L[-1]
        L.append(L[e-1] + L[e-2])


def perrin():
    """
    The Perrin Numbers\n
    OEIS A001608
    """
    
    a,b,c = 3,0,2
    
    while True:
        yield a
        a, b, c = b, c, a+b


def rowland():
    """
    Rowland's Sequence consisting of only 1s and odd primes\n
    OEIS A132199
    """
    
    a = 7
    
    for n in naturals(2):
        b = a+gcd(n,a)
        
        yield b-a
        
        a = b


def rowland_primes():
    """
    Prime values of Rowland's Sequence\n
    OEIS 
    """
    
    a = 7
    
    for n in naturals(2):
        b = a+gcd(n,a)
        
        if b-a != 1:
            yield b-a
        
        a = b


def logistic_map(x,r):
    """
    Logistic Map for some rational n/d and integer r\n
    """
    
    require_rationals(["x","r"],[x,r])
    
    while True:
        yield x
        
        x = r*x*(1-x)


def sorting():
    """
    The Sorting Numbers: Greatest number of comparisons needed for merge sort\n
    OEIS A001855
    """
    
    def half_ceil(n):
        if n % 2 == 1:
            return n//2+1
        return n//2
    
    def half_floor(n):
        return n//2
    
    A = [0]
    
    yield 0
    
    for n in naturals(2):
        t = A[half_floor(n)-1] + A[half_ceil(n)-1] + n - 1
        
        yield t
        
        A.append(t)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Fibonacci Sequence")
    simple_test(fibonacci(),15,
                "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377")
    
    print("\nLucas Numbers")
    simple_test(lucas(),14,
                "2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521")
    
    print("\nLucas Sequence U(-1,3)")
    simple_test(lucas_U(-1,3),13,
                "0, 1, -1, -2, 5, 1, -16, 13, 35, -74, -31, 253, -160")
    
    print("\nLucas Sequence V(3,-5)")
    simple_test(lucas_V(3,-5),10,
                "2, 3, 19, 72, 311, 1293, 5434, 22767, 95471, 400248")
    
    print("\nSignature Sequence {3,1,1}")
    simple_test(signature_function([3,1,1]),10,
                "1, 3, 10, 34, 115, 389, 1316, 4452, 15061, 50951")
    
    print("\nPell Numbers")
    simple_test(pell(),12,
                "0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741")
    
    print("\nCompanion Pell Numbers")
    simple_test(companion_pell(),11,
                "2, 2, 6, 14, 34, 82, 198, 478, 1154, 2786, 6726")
    
    print("\nJacobsthal Numbers")
    simple_test(jacobsthal(),13,
                "0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365")
    
    print("\nLeonardo Numbers")
    simple_test(leonardo(),13,
                "1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465")
    
    print("\nSimple Additive Recurrence for a = 7, b = 9")
    simple_test(simple_recurrence(7,9),12,
                "7, 9, 16, 25, 41, 66, 107, 173, 280, 453, 733, 1186")
    
    print("\nTribonacci")
    simple_test(tribonacci(),14,
                "0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504")
    
    print("\nTetranacci")
    simple_test(multi_fibonacci(4),14,
                "0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401")
    
    print("\nPadovan")
    simple_test(padovan(),17,
                "1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16")
    
    print("\nPadovan's Spiral")
    simple_test(padovan_spiral(),16,
                "1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49")
    
    print("\nSylvester's Sequence")
    simple_test(sylvester(),7,
                "2, 3, 7, 43, 1807, 3263443, 10650056950807")
    
    print("\nNarayana's Cows Sequence")
    simple_test(narayana_cows(),15,
                "1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129")
    
    print("\nPisot E-Sequence(8,21)")
    simple_test(pisot_E(8,21),10,
                "8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368")
    
    print("\nPisot L-Sequence(8,21)")
    simple_test(pisot_L(8,21),10,
                "8, 21, 56, 150, 402, 1078, 2891, 7754, 20798, 55785")
    
    print("\nPisot P-Sequence(8,21)")
    simple_test(pisot_P(8,21),10,
                "8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368")
    
    print("\nPisot T-Sequence(8,21)")
    simple_test(pisot_P(8,21),10,
                "8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368")
    
    print("\nUlam Sequence")
    simple_test(ulam(),15,
                "1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47")
    
    print("\n(1,3)-Ulam Sequence")
    simple_test(ulam(1,3),15,
                "1, 3, 4, 5, 6, 8, 10, 12, 17, 21, 23, 28, 32, 34, 39")
    
    print("\nThe Semifibonacci Sequence")
    simple_test(semifibonacci(),17,
                "1, 1, 2, 1, 3, 2, 5, 1, 6, 3, 9, 2, 11, 5, 16, 1, 17")
    
    print("\nPerrin Sequence")
    simple_test(perrin(),15,
                "3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51")
    
    print("\nRowland's Sequence")
    simple_test(rowland(),17,
                "1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1")
    
    print("\nPrimes in Rowland's Sequence")
    simple_test(rowland_primes(),16,
                "5, 3, 11, 3, 23, 3, 47, 3, 5, 3, 101, 3, 7, 11, 3, 13")
    
    print("\nInfinite Tribonnaci Word")
    simple_test(tribonnaci_word(),18,
                "0, 1, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 1, 0, 1, 0, 2, 0")
    
    print("\nTribonnaci Words")
    simple_test(tribonnaci_words(),4,
                "(0,), (0, 1), (0, 1, 0, 2), (0, 1, 0, 2, 0, 1, 0)")
    
    print("\nLogistic Map with x=1/3 and r=1/2")
    simple_test(logistic_map(Fraction(1,3),Fraction(1,2)),5,
                "1/3, 1/9, 4/81, 154/6561, 493339/43046721")
    
    print("\nThe Sorting Numbers")
    simple_test(sorting(),15,
                "0, 1, 3, 5, 8, 11, 14, 17, 21, 25, 29, 33, 37, 41, 45")
    