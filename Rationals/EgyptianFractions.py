from RationalsType import Rational

def egyptian_form(rational):
    """List of unit fractions that sum to the fraction"""
    
    # If the fraction is greater than one separate out the whole part
    L = []
    if rational.n >= rational.d:
        w,f = rational.mixed_form()
        a = f.n
        b = f.d
        L.append(w)
    else:
        a = rational.n
        b = rational.d

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

A = Rational(15,23)
print(egyptian_form(A))