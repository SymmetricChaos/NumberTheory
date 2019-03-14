# Finite fields can often be represented by polynomials with the aid of modular
# arithmetic. This is most useful for GF(p^n) when n is greater than 1.

# For our purposes polynomials will be in ASCENDING order
# x^0 is at index 0
# x^1 is at index 1
# x^2 is at index 2
# etc

# Extended Euclidean algorithm
# g   : Greatest common denominator
# x,y : integers such that g = ax + by
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Use egcd to calculate the modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Pad a polynomial with zeroes
def polypad(P,n):
    out = P.copy()
    while len(out) < n:
        out.append(0)
    return out

# Remove zeroes from the end
def polynorm(P):
    while P[-1] == 0:
        if len(P) == 1:
            break
        P.pop()

# Add two polynomiala modulo some number
def polyadd(P,Q,m):
    
    pad = max(len(P),len(Q))
    
    P = polypad(P,pad)
    Q = polypad(Q,pad)
    
    out = []
    for x,y in zip(P,Q):
        out.append( x+y % m)
    
    return out
    
# Multiply two polynomials modulo some number
def polymult(P,Q,m):
    
    L = [0]*(len(P)+len(Q))
    
    for i in range(len(P)):
        for j in range(len(Q)):
            L[i+j] += P[i]*Q[j]
            L[i+j] = L[i+j] % m
    
    for x in L[::-1]:
        if x == 0:
            L.pop()
        else:
            break
    return L

def poly_divmod(P, Q):
    # Don't modify the inputs
    P = P[:]
    Q = Q[:]
    
    # Remove unnecessary zeroes
    polynorm(P)
    polynorm(Q)
    
    # Record the degree of the polynomials
    dP = len(P)-1
    dQ = len(Q)-1
    
    if Q == 0:
        raise ZeroDivisionError
    
    if dP >= dQ:
        qt = [0]*dP
        while dP >= dQ:
            d = [0]*(dP - dQ) + Q
            mult = qt[dP - dQ] = P[-1] / float(d[-1])
            d = [co*mult for co in d]
            P = [float(abs ( coeffP - coeffd )) for coeffP, coeffd in zip(P, d)]
            polynorm(P)
            dP = len(P)-1
            #print(P)
        rm = P
    else:
        qt = [0]
        rm = P
    
    
    polynorm(qt)
    polynorm(rm)
    
    return qt,rm


P = [-42,0,-12,1]
Q = [-3,1,0,0]

#print(polyadd(P,Q,2))
#print(polymult([1,0,2,1,0],[1,1,2,1],3))

print(P)
print(Q)
print(poly_divmod(P,Q))