from Sequences.Utils import factorization



def aliquot():
    """Aliquot Numbers"""
    ctr = 1
    while True:
        yield sum(factorization(ctr)[:-1])
        ctr += 1

def abundant():
    """Abundant Numbers"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) > ctr:
            yield ctr
        ctr += 1
        
def deficient():
    """Deficient Numbers"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) < ctr:
            yield ctr
        ctr += 1
        
def perfect():
    """Perfect Numbers"""
    ctr = 1
    while True:
        if sum(factorization(ctr)[:-1]) == ctr:
            yield ctr
        ctr += 1