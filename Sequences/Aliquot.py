from Sequences.MathUtils import factorization
from Sequences.Simple import naturals

def _aliquot_sum(n):
    return sum(factorization(n)[:-1])

def aliquot():
    """Aliquot Numbers: Sum of proper divisors for each positive integer"""
    
    for n in naturals(1):
        yield _aliquot_sum(n)


def aliquot_recurrence(N):
    """Aliquot Sequence of N: Recurrence relation of which each term of the Aliquot sum of the previous"""
    
    while True:
        yield N
        N = _aliquot_sum(N)


def abundant():
    """Abundant Numbers: Positive integers that are less than their Aliquot sum"""
    
    for n in naturals(1):
        if _aliquot_sum(n) > n:
            yield n


def abundance():
    """Abundance: The Aliquot sum of each positive number minus that number"""
    
    for n in naturals(1):
        yield _aliquot_sum(n)-n


def deficient():
    """Deficient Numbers: Positive integers that are greater than their Aliquot sum"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) < ctr:
            yield ctr
        ctr += 1


def deficiency():
    """Deficiency: Each positive integer minus its Aliquot sum"""
    
    for n in naturals(1):
        yield n-_aliquot_sum(n)


def perfect():
    """Perfect Numbers: Positive integers that are equal to their Aliquot sum"""
    
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


if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Aliquot Sums")
    simple_test(aliquot(),10,
                "0, 1, 1, 3, 1, 6, 1, 7, 4, 8")
    
    print("\nAliquot Sequence of 276")
    simple_test(aliquot_recurrence(276),9,
                "276, 396, 696, 1104, 1872, 3770, 3790, 3050, 2716")
    
    print("\nAbundant Numbers")
    simple_test(abundant(),10,
                "12, 18, 20, 24, 30, 36, 40, 42, 48, 54")
    
    print("\nAbundance")
    simple_test(abundance(),10,
                "-1, -1, -2, -1, -4, 0, -6, -1, -5, -2")
    
    print("\nDeficient Numbers")
    simple_test(deficient(),10,
                "1, 2, 3, 4, 5, 7, 8, 9, 10, 11")
    
    print("\nDeficiency")
    simple_test(deficiency(),10,
                "1, 1, 2, 1, 4, 0, 6, 1, 5, 2")
    
    print("\nPerfect Numbers")
    simple_test(perfect(),6,
                "6, 28, 496, 8128, 33550336, 8589869056")
    