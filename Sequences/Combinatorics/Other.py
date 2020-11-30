from Sequences.MathUtils import nontrivial_factors, all_subsets, poly_eval
from Sequences.Combinatorics.PermutationUtils import int_to_comb
from Sequences.Simple import naturals
from Sequences.Manipulations import make_triangle
from Sequences.NiceErrorChecking import require_geq, require_integers

from math import comb


def catalan():
    """
    Catalan Numbers: Fundamental sequence in combinatorics\n
    OEIS A000108
    """
    
    C = 1
    
    for n in naturals():
        yield C
        C = C*(4*n+2)//(n+2)


def co_catalan():
    """
    Co-Catalan Numbers: Number of illegal options in many counting problems address by Catalan numbers\n
    OEIS A001791
    """
    
    yield 0
    for n in naturals(1):
        yield comb(2*n,n-1)


# Building the triangle using only addition and index look ups is about 100 
# times faster than calculating the binomial coefficients directly on my
# machine
# There is probably a way to do this is place
def pascal():
    """
    Pascal's Triangle: Number triangle with binomial coefficients\n
    OEIS A007318
    """
    
    L = [1,0]
    
    while True:
        T = [0]
        
        for i in range(len(L)-1):
            x = L[i]+L[i+1]
            T.append(x)
            yield x
        
        T.append(0)
        L = T


def pascal_triangle():
    """
    Pascal's Triangle by Rows\n
    OEIS A007318
    """
    
    yield from make_triangle(pascal())


# Find a more efficient way to do this
def central_binomial():
    """
    Central Binomial Coefficients: Middle term of the odd rows of Pascal's Triangle
    OEIS A000984
    """
    
    for n in naturals():
        yield comb(2*n,n)


def gould():
    """
    Gould's Sequence: Number of odd values on the nth row of Pascal's Triangle\n
    OEIS A001316
    """
    
    P = pascal()
    
    for n in naturals(1):
        val = 0
        
        for i in range(n):
            if next(P) % 2 == 1:
                val += 1
        
        yield val


# As with Pascal's triangle I found this memoized version to be vastly faster
# than directly calculating the values, which involved both binomial
# coefficients and exponentiation
def eulerian():
    """
    Eulerian Triangle: Triangle with number of permutations of a set with n elements where there are m increases\n
    OEIS A008292
    """
    
    L = [1,0]
    
    for a in naturals(1):
        T = []
        
        for b in range(a):
            x = (a-b)*L[b-1] + (b+1)*L[b]
            T.append(x)
            yield x
        
        T.append(0)
        L = T


def eulerian_triangle():
    """
    Eulerian Triangle by Rows\n
    OEIS A007318
    """
    
    yield from make_triangle(eulerian())


def bell():
    """
    Bell Numbers: Number of equivalence classes on a set with n elements\n
    OEIS A000110
    """
    
    R0 = [1]
    R1 = [1,2]
    
    while True:
        yield R0[0]
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2


def fubini():
    """
    Fubini Numbers (aka Ordered Bell Numbers): Number of weak orderings on a set with n elements\n
    OEIS A000670
    """
    
    yield 1
    
    for P in eulerian_triangle():
        yield poly_eval(P,2)


def lazy_caterer():
    """
    Lazy Caterer Numbers: Maximum number of pieces produced when cutting a circle with exactly n lines\n
    OEIS A000124
    """
    
    for n in naturals():
        yield (n*(n+1))//2+1


# Generalized cake numbers?
def cake():
    """
    Cake Numbers: Maximum number of pieces produced when cutting a sphere with exactly n planes\n
    OEIS A000125
    """
    
    for n in naturals():
        yield (n*n*n+5*n+6)//6


# Potentially memoizeable
def multiplicative_partition():
    """
    Multiplicative Partition Numbers: Sets of integers, not including one, that have a product of n\n
    OEIS A001055
    """
    
    def all_factorizations_inner(n,m=1):
        F = [f for f in nontrivial_factors(n) if f >= m]
        
        if len(F) == 0:
            yield [n]
        
        else:
            for f in F:
                for a in all_factorizations_inner(n//f,f):
                    yield [f] + a
    
    def num_factorizations(n):
        S = set([(n,)])
        
        for i in all_factorizations_inner(n):
            S.add(tuple(sorted(i)))
        
        return len(S)
    
    for n in naturals(1):
        yield num_factorizations(n)


def natural_subsets(index=0):
    """
    All subsets of the natural numbers in colexicographic order (aka prefix order)
    
    Args:
        index -- 0 or 1, least element
    
    OEIS
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    yield ()
    yield from all_subsets(naturals(index))


def combinadic(k):
    """
    k-Combinadic Numbers: Natural numbers represented as descending combinations of k elements\n
    OEIS
    """
    
    for n in naturals():
        yield int_to_comb(n,k)


def dyck_words(n):
    """
    The Dyck words of order n with 'up' as +1 and 'down' as -1
    """
    
    def dyck_recur(S):
        a = S.count(1)
        b = S.count(-1)
        if len(S) > 2*n or b > a:
            return None
        elif a == b == n:
            yield S
        else:
            yield from dyck_recur(S+(1,))
            yield from dyck_recur(S+(-1,))
    
    yield from dyck_recur(())


def dyck_language():
    """
    All the Dyck words with 'up' as +1 and 'down' as -1
    """
    
    for n in naturals(1):
        yield from dyck_words(n)


def dyck_words_str(n):
    """
    All words consisting of n pairs of correctly matched parentheses
    """
    
    def dyck_recur(S):
        a = S.count("(")
        b = S.count(")")
        if len(S) > 2*n or b > a:
            return None
        elif a == b == n:
            yield S
        else:
            yield from dyck_recur(S+"(")
            yield from dyck_recur(S+")")
    
    yield from dyck_recur("")


def dyck_language_str():
    """
    All words consisting of correctly matched pairs of parentheses
    """
    
    for n in naturals(1):
        yield from dyck_words_str(n)


def naranya():
    """
    Triangle of Naranya Numbers: Number of Dyck words of order n with k peaks\n
    OEIS A001263
    """
    
    for n in naturals(1):
        for k in range(1,n+1):
            yield (comb(n,k)*comb(n,k-1))//n


def naranya_triangle():
    """
    Naranya's Triangle by Rows, sums are the Catalan numbers\n
    OEIS A001263
    """
    
    yield from make_triangle(naranya())


def schroder():
    """
    Schröder Numbers: The big Schröder numbers\n
    OEIS A006318
    """
    
    yield 1
    
    S = [1,2]
    
    for n in naturals(1):
        yield S[n]
        
        t = 3*S[-1]
        for k in range(1,n):
            t += S[k]*S[n-k]
        
        S.append(t)


def schroder_hipparchus():
    """
    Schröder-Hipparchus Numbers: The little Schröder numbers\n
    OEIS A001003
    """
    
    yield 1
    
    a,b = 1,1
    
    for n in naturals(2):
        t = ((6*n-9)*b-(n-3)*a)//n
        a,b = b,t
        
        yield b//2


def motzkin():
    """
    Motzkin Numbers: The number of ways to draw non-intersecting chords through n points on a circle
    OEIS 1006
    """
    
    yield 1
    
    for n in naturals(1):
        
        t = 0
        for k,c in zip(range(n//2+1),catalan()):
            t += comb(n,2*k)*c
        
        yield t


def motzkin_paths(n):
    """
    Every 'mountain' made of n line segments going NE (+1) and SW (-1), and E (0)\n
    """
    
    def horizon_recur(S):
        if len(S) > n or sum(S) < 0:
            return None
        elif sum(S) == 0 and len(S) == n:
            yield S
        else:
            yield from horizon_recur(S+(1,))
            yield from horizon_recur(S+(0,))
            yield from horizon_recur(S+(-1,))
    
    yield from horizon_recur(())


def delannoy():
    """
    Triangle of Delannoy Numbers\n
    A008288
    """
    
    yield 1
    
    R1 = [0,0]
    R2 = [0,1,0]
    
    while True:
        T = [0]
        
        for i in range(len(R2)-1):
            x = R2[i]+R2[i+1]+R1[i]
            T.append(x)
            yield x
        
        T.append(0)
        R1, R2 = R2, T


def delannoy_triangle():
    """
    Delannoy Triangle By Rows\n
    A008288
    """
    
    yield from make_triangle(delannoy())


def central_delannoy():
    """
    Central Delannoy Numbers\n
    OEIS A001850
    """
    
    for n in naturals(0):
        t = 0
        for k in range(n+1):
            t += comb(n,k)*comb(n+k,k)
        yield t


def wedderburn_etherington():
    """
    Wedderburn-Etherington Numbers\n
    OEIS A001190
    """
    
    S = [0,1,1]
    
    yield from S
    
    for n in naturals(2):
        # Odd step
        t = 0
        for i in range(1,n):
            t += S[i]*S[2*n-i-1]
        
        yield t
        S.append(t)
        
        # Even step
        t = (S[n]*(S[n]+1))//2
        for i in range(1,n):
            t += S[i]*S[2*n-i]
        
        yield t
        S.append(t)


def lobb():
    """
    Lobb Numbers: Valid prefixes for matched parentheses with m+n left brackets and m-n right brackets\n
    OEIS A039599
    """
    
    for m in naturals():
        for n in range(m+1):
            yield (2*n+1)*comb(2*m,m+n)//(m+n+1)


def lobb_triangle():
    """
    Lobb Triangle by Rows\n
    OEIS A039599
    """
    
    yield from make_triangle(lobb())


def lobb_words(m,n):
    """
    All words consisting of m+n left brackets and n-m right brackets that can be the prefix of a Dyck word
    """
    
    require_integers(["m","n"],[m,n])
    require_geq(["m","n"],[m,n],0)
    
    if n < m:
        raise ValueError("n cannot be less than m")
    
    def lobb_recur(S):
        a = S.count(1)
        b = S.count(-1)
        if len(S) > 2*n or b > a:
            return None
        elif a == (m+n) and b == (n-m):
            yield S
        else:
            yield from lobb_recur(S+(1,))
            yield from lobb_recur(S+(-1,))
    
    yield from lobb_recur(())


def lobb_words_str(m,n):
    """
    All words consisting of m+n left brackets and n-m right brackets that can be the prefix of a Dyck word
    """
    
    require_integers(["m","n"],[m,n])
    require_geq(["m","n"],[m,n],0)
    
    if n < m:
        raise ValueError("n cannot be less than m")
    
    def lobb_recur(S):
        a = S.count("(")
        b = S.count(")")
        if len(S) > 2*n or b > a:
            return None
        elif a == (m+n) and b == (n-m):
            yield S
        else:
            yield from lobb_recur(S+"(")
            yield from lobb_recur(S+")")
    
    yield from lobb_recur("")


def fuss_catalan(p,r):
    """
    Fuss-Catalan Numbers
    OEIS A000108, A000245, A002057, A001764, A006013, A006629, A002293, 
         A069271, A006632
    """
    
    require_integers(["p","r"],[p,r])
    require_geq(["p","r"],[p,r],0)
    
    for n in naturals():
        yield r*comb(n*p+r,n)//(n*p+r)


# def permutohedron():
#     """
    
#     """



def set_partitions(n,index=0):
    """
    The partitions of a set with n elements
    """
    
    def part(depth):
        if depth == index:
            yield ((index,),)
        else:
            for t in part(depth-1):
                for n,sub in enumerate(t):
                    if type(sub) == tuple:
                        yield t[:n] + (sub + (depth,),) + t[n+1:]
                yield t + ((depth,),)
    
    if index == 1:
        yield from part(n)
    else:
        yield from part(n-1)


# def ordered_partitions(n):
#     """
#     The ordered partitions of a set with n elements
#     """
    
#     S = [i for i in range(n)]
    
#     def 



if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nCatalan Numbers")
    simple_test(catalan(),11,
                "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796")
    
    print("\nCo-Catalan Numbers")
    simple_test(co_catalan(),11,
                "0, 1, 4, 15, 56, 210, 792, 3003, 11440, 43758, 167960")
    
    print("\nPascal's Triangle")
    simple_test(pascal(),18,
                "1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal_triangle(),4,
                "(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1)")
    
    print("\nCentral Binomial Coefficients")
    simple_test(central_binomial(),11,
                "1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756")
    
    print("\nGould's Sequence")
    simple_test(gould(),18,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4")
    
    print("\nEulerian Triangle")
    simple_test(eulerian(),16,
                "1, 1, 1, 1, 4, 1, 1, 11, 11, 1, 1, 26, 66, 26, 1, 1")
    
    print("\nEulerian Triangle by Rows")
    simple_test(eulerian_triangle(),4,
                "(1,), (1, 1), (1, 4, 1), (1, 11, 11, 1)")
    
    print("\nBell Numbers")
    simple_test(bell(),11,
                "1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975")
    
    print("\nFubini Numbers")
    simple_test(fubini(),10,
                "1, 1, 3, 13, 75, 541, 4683, 47293, 545835, 7087261")
    
    print("\nLazy Caterer's Numbers")
    simple_test(lazy_caterer(),14,
                "1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92")
    
    print("\nCake Numbers")
    simple_test(cake(),13,
                "1, 2, 4, 8, 15, 26, 42, 64, 93, 130, 176, 232, 299")
    
    print("\nMultiplicative Partitions")
    simple_test(multiplicative_partition(),18,
                "1, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4, 1, 2, 2, 5, 1, 4")
    
    print("\nAll Subsets of Natural Numbers")
    simple_test(natural_subsets(),7,
                "(), (0,), (1,), (0, 1), (2,), (0, 2), (1, 2)")
    
    print("\n2-Combinadic Numbers")
    simple_test(combinadic(2),7,
                "(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0)")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal_triangle(),5,
                "(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 6, 4, 1)")
    
    print("\nDyck Words of Order 4")
    simple_test(dyck_words_str(4),5,
                "(((()))), ((()())), ((())()), ((()))(), (()(()))")
    
    print("\nDyck Language")
    simple_test(dyck_language_str(),7,
                "(), (()), ()(), ((())), (()()), (())(), ()(())")
    
    print("\nDyck Words of Order 3 (numeric)")
    simple_test(dyck_words(3),2,
                "(1, 1, 1, -1, -1, -1), (1, 1, -1, 1, -1, -1)")
    
    print("\nDyck Language (numeric)")
    simple_test(dyck_language(),3,
                "(1, -1), (1, 1, -1, -1), (1, -1, 1, -1)")
    
    print("\nNaranya's Triangle")
    simple_test(naranya(),16,
                "1, 1, 1, 1, 3, 1, 1, 6, 6, 1, 1, 10, 20, 10, 1, 1")
    
    print("\nNaranya's Triangle By Rows")
    simple_test(naranya_triangle(),4,
                "(1,), (1, 1), (1, 3, 1), (1, 6, 6, 1)")
    
    print("\nSchröder Numbers")
    simple_test(schroder(),10,
                "1, 2, 6, 22, 90, 394, 1806, 8558, 41586, 206098")
    
    print("\nSchröder-Hipparchus Numbers")
    simple_test(schroder_hipparchus(),10,
                "1, 1, 3, 11, 45, 197, 903, 4279, 20793, 103049")
    
    print("\nMotizkin Numbers")
    simple_test(motzkin(),12,
                "1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798")
    
    print("\nMotzkin Paths of Length 3 (numeric)")
    simple_test(motzkin_paths(3),10,
                "(1, 0, -1), (1, -1, 0), (0, 1, -1), (0, 0, 0)")
    
    print("\nDelannoy")
    simple_test(delannoy(),18,
                "1, 1, 1, 1, 3, 1, 1, 5, 5, 1, 1, 7, 13, 7, 1, 1, 9, 25")
    
    print("\nDelannoy Triangle")
    simple_test(delannoy_triangle(),4,
                "(1,), (1, 1), (1, 3, 1), (1, 5, 5, 1)")
    
    print("\nCentral Delannoy")
    simple_test(central_delannoy(),9,
                "1, 3, 13, 63, 321, 1683, 8989, 48639, 265729")
    
    print("\nWedderburn-Etherington Numbers")
    simple_test(wedderburn_etherington(),13,
                "0, 1, 1, 1, 2, 3, 6, 11, 23, 46, 98, 207, 451")
    
    print("\nLobb Numbers")
    simple_test(lobb(),17,
                "1, 1, 1, 2, 3, 1, 5, 9, 5, 1, 14, 28, 20, 7, 1, 42, 90")
    
    print("\nLobb Triangle")
    simple_test(lobb_triangle(),4,
                "(1,), (1, 1), (2, 3, 1), (5, 9, 5, 1)")
    
    print("\nLobb Words with m = 1 and n = 3")
    simple_test(lobb_words_str(1,3),7,
                "(((()), ((()(), ((())(, (()((), (()()(, (())((, ()((()")
    
    print("\nLobb Words with m = 1 and n = 2 (numeric)")
    simple_test(lobb_words(1,2),3,
                "(1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1)")
    
    print("\nFuss-Catalan Numbers with p = 2, r = 3")
    simple_test(fuss_catalan(2,3),11,
                "1, 3, 9, 28, 90, 297, 1001, 3432, 11934, 41990, 149226")
    
    print("\nSet Partitions")
    simple_test(set_partitions(3),11,
                "((0, 1, 2),), ((0, 1), (2,)), ((0, 2), (1,)), ((0,), (1, 2)), ((0,), (1,), (2,))")
    