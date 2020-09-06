from Sequences.NiceErrorChecking import require_integers, require_positive
from Sequences.MathUtils import aliquot_parts, sum_of_divisors, powerset, aliquot_sum, prime_factorization
from Sequences.Simple import naturals, arithmetic
from collections import Counter

def aliquot():
    """
    Aliquot Numbers: Sum of proper divisors for each positive integer
    OEIS A001065
    """
    
    for n in naturals(1):
        yield aliquot_sum(n)


def untouchable():
    """
    Untouchable Numbers: Non-negative integers that cannot be an aliquot sum
    OEIS A005114
    """
    
    pass


def aliquot_recurrence(N):
    """
    Aliquot Sequence of N: Recurrence relation of which each term of the aliquot sum of the previous
    """
    
    require_integers(["N"],[N])
    require_positive(["N"],[N])
    
    while True:
        yield N
        N = aliquot_sum(N)


def abundant():
    """
    Abundant Numbers: Positive integers that are less than their aliquot sum
    OEIS A005101
    """
    
    for n in naturals(1):
        if aliquot_sum(n) > n:
            yield n


def primitive_abundant_1():
    """
    Primitive Abundant Numbers: Positive integers that are abundant but have only deficient factors
    OEIS A071395
    """
    
    P = perfect()
    next_p = next(P)
    A = set([])
    
    for n in naturals(1):
        if n >= next_p:
            A.add(next_p)
            next_p = next(P)
        
        F = aliquot_parts(n)
        
        if sum(F) > n:
            if any([f in A for f in F]):
                continue
            
            yield n
            A.add(n)


def primitive_abundant_2():
    """
    Primitive Abundant Numbers: Positive integers that are abundant but no abundant factors
    OEIS A091191
    """
    
    A = set([])
    
    for n in naturals(1):
        F = aliquot_parts(n)
        
        if sum(F) > n:
            if any([f in A for f in F]):
                continue
            
            yield n
            A.add(n)


def abundance():
    """
    Abundance: The aliquot sum of each positive number minus that number
    OEIS A033880
    """
    
    for n in naturals(1):
        yield aliquot_sum(n)-n


def highly_abundant():
    """
    Highly Abundant Numbers: Positive integers with a greater sum of divisors than every smaller positive integer
    OEIS A002093
    """
    
    M = 0
    
    for n in naturals(1):
        m = sum_of_divisors(n)
        
        if m > M:
            M = m
            yield n


def superabundant():
    """
    Super Abundant Numbers: Positive integers such that the sum of divisors divided by n is greater than for every smaller positive integer
    OEIS A004394
    """
    
    M = 0
    
    for n in naturals(1):
        m = sum_of_divisors(n)/n
        
        if m > M:
            M = m
            yield n


def deficient():
    """
    Deficient Numbers: Positive integers that are greater than their aliquot sum
    OEIS A005100
    """
    
    ctr = 1
    
    while True:
        if aliquot_sum(ctr) < ctr:
            yield ctr
        ctr += 1


def deficiency():
    """
    Deficiency: Each positive integer minus its aliquot sum
    OEIS A033879
    """
    
    for n in naturals(1):
        yield n-aliquot_sum(n)


def perfect():
    """
    Perfect Numbers: Positive integers that are equal to their aliquot sum
    OEIS A000396
    """
    
    # There are currently (2020) only 51 known perfect numbers and the first 47
    # of those are sequential so, since they're hard to find, we cheat a bit.
    # This is still pretty, slow, though.
    P = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 
         2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497,
         86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 
         2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 
         30402457, 32582657, 37156667, 42643801, 4311260]
    
    for p in P:
        yield 2**(p-1)*(2**(p)-1)


def pseudoperfect():
    """
    Pseudoperfect Numbers: Positive integers such that some subset of the proper factors sum to n\n
    OEIS A005835
    """
    
    for n in naturals(2):
        F = aliquot_parts(n)
        for s in powerset(F):
            if sum(s) == n:
                yield n
                break


# Must be a more efficient way to generate these
def weird():
    """
    Weird Numbers: Positive integers that are abundant but not pseudoperfect\n
    OEIS 
    """
    
    def _is_pseudoperfect(n):
        F = aliquot_parts(n)
        for s in powerset(F):
            if sum(s) == n:
                return True
        return False
    
    for a in abundant():
        if not _is_pseudoperfect(a):
            yield a


def amicable_pairs():
    """
    Amicable Pairs:\n
    OEIS
    """
    
    lower = set([])
    
    for n in naturals(220):
        b = aliquot_sum(n)
        
        if b <= n or b in lower:
            continue
        
        if aliquot_sum(b) == n:
            lower.add(n)
            yield n
            yield b


def practical():
    """
    Practical Numbers: Positive integers with factors that can be summed to any smaller positive integer\n
    OEIS
    """
    
    def srinivasan_ineq(a):
        F = prime_factorization(a)
        C = Counter(F)
        P = 2**(C[2]+1)-1
        del C[2]
        for p,n in C.items():
            if p > P+1:
                return False
            P *= (p**(n+1)-1)//(p-1)
        return True
    
    yield 1
    
    for a in arithmetic(2,2):
        if srinivasan_ineq(a):
            yield a





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Aliquot Sums")
    simple_test(aliquot(),17,
                "0, 1, 1, 3, 1, 6, 1, 7, 4, 8, 1, 16, 1, 10, 9, 15, 1")

    print("\nAliquot Sequence of 276")
    simple_test(aliquot_recurrence(276),9,
                "276, 396, 696, 1104, 1872, 3770, 3790, 3050, 2716")
    
    print("\nAbundant Numbers")
    simple_test(abundant(),14,
                "12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70")
    
    print("\nPrimitive Abundant Numbers (Type 1, all deficient factors)")
    simple_test(primitive_abundant_1(),12,
                "20, 70, 88, 104, 272, 304, 368, 464, 550, 572, 650, 748")
    
    print("\nPrimitive Abundant Numbers (Type 2, no abundant factors)")
    simple_test(primitive_abundant_2(),13,
                "12, 18, 20, 30, 42, 56, 66, 70, 78, 88, 102, 104, 114")
    
    print("\nHighly Abdundant Numbers")
    simple_test(highly_abundant(),15,
                "1, 2, 3, 4, 6, 8, 10, 12, 16, 18, 20, 24, 30, 36, 42")
    
    print("\nSuperabdundant Numbers")
    simple_test(superabundant(),13,
                "1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360")
    
    print("\nAbundance")
    simple_test(abundance(),14,
                "-1, -1, -2, -1, -4, 0, -6, -1, -5, -2, -10, 4, -12, -4")
    
    print("\nDeficient Numbers")
    simple_test(deficient(),16,
                "1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19")
    
    print("\nDeficiency")
    simple_test(deficiency(),17,
                "1, 1, 2, 1, 4, 0, 6, 1, 5, 2, 10, -4, 12, 4, 6, 1, 16")
    
    print("\nPerfect Numbers")
    simple_test(perfect(),7,
                "6, 28, 496, 8128, 33550336, 8589869056, 137438691328")
    
    print("\nPseudoperfect Numbers")
    simple_test(pseudoperfect(),14,
                "6, 12, 18, 20, 24, 28, 30, 36, 40, 42, 48, 54, 56, 60")
    
    print("\nWeird Numbers (infinite but very laborious to compute)")
    simple_test(weird(),2,
                "70, 836")
    
    print("\nAmicable Pairs")
    simple_test(amicable_pairs(),9,
                "220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232")
    
    print("\nPractical Numbers")
    simple_test(practical(),15,
                "1, 2, 4, 6, 8, 12, 16, 18, 20, 24, 28, 30, 32, 36, 40")
    