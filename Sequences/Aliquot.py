from Other.Factors import aliquot_sum

def aliquot():
    """Aliquot Numbers"""
    ctr = 1
    while True:
        yield aliquot_sum(ctr)
        ctr += 1

def abundant():
    """Abundant Numbers"""
    ctr = 1
    while True:
        if aliquot_sum(ctr) > ctr:
            yield ctr
        ctr += 1
        
def deficient():
    """Deficient Numbers"""
    ctr = 1
    while True:
        if aliquot_sum(ctr) < ctr:
            yield ctr
        ctr += 1
        
def perfect():
    """Perfect Numbers"""
    ctr = 1
    while True:
        if aliquot_sum(ctr) == ctr:
            yield ctr
        ctr += 1