from Sequences.MathUtils import factorization



def aliquot():
    """Aliquot Numbers: Sum of divisors for each positive integer"""
    ctr = 1
    while True:
        yield sum(factorization(ctr)[:-1])
        ctr += 1


def abundant():
    """Abundant Numbers: Positive integers that are less than their sum of divisors"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) > ctr:
            yield ctr
        ctr += 1


def deficient():
    """Deficient Numbers: Positive integers that are greater than their sum of divisors"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) < ctr:
            yield ctr
        ctr += 1


def perfect():
    """Perfect Numbers: Positive integer that are equal to their sum of divisors"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) == ctr:
            yield ctr
        ctr += 1