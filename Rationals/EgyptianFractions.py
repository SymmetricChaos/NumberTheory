from RationalsType import Rational
from Other import factorization, subset_sum
from PrimeNumbers import is_prime

# Use the greedy algorithm to find an egyption fraction representation for a
# fraction.
def egyptian_form_greedy(rational):

    a = rational.n
    b = rational.d

    L = []
    # Test each possible unit fraction discarding it if it is too big
    # Otherwise subtract it out until a unit fraction remains
    x = 2
    while a > 0:
        F1 = Rational(a*x,b*x)
        F2 = Rational(-1,x)
        s = F1+F2
        if s.n >= 0:
            a,b = s.n,s.d
            L.append(Rational(1,x))
            if a == 1:
                L.append(Rational(1,b))
                return L
        x += 1
        
    return L

# Use sums of divisors to find egyptian fraction representations this always
# if the denominator is a practical number
def egyptian_form_factoring(rational):
    
    N = rational.n
    D = rational.d
    F = factorization(D)
    S = subset_sum(F,N)
    if S != ():
        return [Rational(s,D) for s in S]
    else:
        return []


def egyptian_form_prime(rational):
    n = rational.n
    d = rational.d
    if n == 2:
        A = Rational(2,d+1) 
        B = Rational(2,d*(d+1))
        return [A,B]
    else:
        return []
    
    
def egyptian_split(d):
    """Egyptian representation for a fraction with a numerator of 2 and a denominator of d"""
    return [Rational(1,d), Rational(1,d+1), Rational(1,d*(d+1))]
        
def egyptian_form(rational):
    
    # If the fraction is greater than one seperate out the whole part
    L = []
    if rational.n >= rational.d:
        w,rational = rational.mixed_form()
        L.append(w)
    if rational == 0:
        return L
        
    if is_prime(rational.d) and rational.n == 2:
        E = egyptian_form_prime(rational)
        print("prime")
        return L + E

    E = egyptian_form_factoring(rational)
    if E != []:
        E.sort(reverse = True)
        print("practical")
        return L + E
    
    print("greedy")
    return L + egyptian_form_greedy(rational)

    
