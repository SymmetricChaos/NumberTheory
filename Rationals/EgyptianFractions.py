from RationalsType import Rational
from Other import factorization, subset_sum

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
def egyptian_form_practical(rational):
    
    N = rational.n
    D = rational.d
    F = factorization(D)
    S = subset_sum(F,N)
    if S != ():
        return [Rational(s,D) for s in S]
    else:
        return []


#def egyptian_form_prime(rational):
#    if rational.n % 2 == 0:
#        #2/p = 2/(p+1) + 2/(p*(p+1))
#    else:
#        return []
    
    
    
        
def egyptian_form(rational):
    
    # If the fraction is greater than one seperate out the whole part
    L = []
    if rational.n >= rational.d:
        w,rational = rational.mixed_form()
        L.append(w)
    
    E = egyptian_form_practical(rational)
    if E != []:
        E.sort()
    else:
        E = egyptian_form_greedy(rational)
    
    return L + E
    
import random
for i in range(20):
    
    N = random.randint(2,100)
    D = random.randint(2,100)
    
    A = Rational(N,D)
    print(A)
    E = egyptian_form(A)
    print(E)
    print()