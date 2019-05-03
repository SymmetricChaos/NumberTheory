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
        out = [Rational(s,D) for s in S]
        out.sort(reverse = True)
        return out
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
    
    
def egyptian_split(R):
    """Split a fraction with a numerator of 1 or 2 into an Egyptian fraction"""
    
    if R.n == 2:
        return [Rational(1,R.d), Rational(1,R.d+1), Rational(1,R.d*(R.d+1))]
    if R.n == 1:
        return [Rational(1,2*R.d), Rational(1,2*(R.d+1)), Rational(1,2*R.d*(R.d+1))]
        
def egyptian_form_splitting(R):
    """Create an Egyptian fraction representation using splitting"""
    
    a,b = divmod(R.n,2)
    E = egyptian_split(Rational(2,R.d))
    E = E*a
    
    if b == 1:
        E += [Rational(1,R.d)]
    
    changed = True
    while changed == True:
        changed = False
        for pos,e in enumerate(E):
            if E.count(e) > 1:
                changed = True
                del E[pos]
                E += egyptian_split(e)
        if len(E) > 20:
            break
                
                

    E.sort(reverse = True)
    
    return E
           
    
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
        print("factoring")
        return L + E
    
    print("greedy")
    return L + egyptian_form_greedy(rational)

    
