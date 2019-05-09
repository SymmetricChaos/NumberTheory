from Rationals.RationalType import Rational
from Other import factorization, subset_sum
from PrimeNumbers import is_prime

# Use the greedy algorithm to find an egyption fraction representation for a
# fraction.
def egyptian_form_greedy(rational):
    
    N = rational.n
    D = rational.d
    assert N < D

    L = []
    # Test each possible unit fraction discarding it if it is too big
    # Otherwise subtract it out until a unit fraction remains
    x = 2
    while N > 0:
        F1 = Rational(N*x,D*x)
        F2 = Rational(-1,x)
        s = F1+F2
        if s.n >= 0:
            N,D = s.n,s.d
            L.append(Rational(1,x))
            if N == 1:
                L.append(Rational(1,D))
                return L
        x += 1
        
    return L

# Use sums of divisors to find egyptian fraction representations this always
# if the denominator is a practical number
def egyptian_form_factoring(rational):
    
    N = rational.n
    D = rational.d
    assert N < D
    
    F = factorization(D)
    S = subset_sum(F,N)
    if S != ():
        out = [Rational(s,D) for s in S]
        out.sort(reverse = True)
        return out
    else:
        return []


def egyptian_form_prime(rational):
    N = rational.n
    D = rational.d
    assert N < D
    
    if N == 2 and is_prime(D):
        A = Rational(2,D+1) 
        B = Rational(2,D*(D+1))
        return [A,B]
    else:
        return []
    
# Fractions of a certain form can be split into 
def egyptian_split(R):
    """Split a fraction with a numerator of 1 or 2 into an Egyptian fraction"""
    
    if R.n == 2:
        return [Rational(1,R.d), Rational(1,R.d+1), Rational(1,R.d*(R.d+1))]
    if R.n == 1:
        return [Rational(1,2*R.d), Rational(1,2*(R.d+1)), Rational(1,2*R.d*(R.d+1))]
        
def egyptian_form_splitting(rational,lim=4):
    """Create an Egyptian fraction representation using splitting"""
    
    N = rational.n
    D = rational.d
    assert N < D
    
    # The splitting method is extremely bad so don't even try if the result is
    # guaranteed to be ridiculous.
    if N > lim:
        return []
    
    a,b = divmod(N,2)
    E = egyptian_split(Rational(2,D))
    E = E*a
    
    if b == 1:
        E += [Rational(1,D)]
    
    changed = True
    while changed == True:
        changed = False
        for pos,e in enumerate(E):
            if E.count(e) > 1:
                changed = True
                del E[pos]
                E += egyptian_split(e)

                
    E.sort(reverse = True)
    
    return E
