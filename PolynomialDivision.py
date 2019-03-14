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


#function n / d:
#  require d ≠ 0
#  q ← 0
#  r ← n       # At each step n = d × q + r
#  while r ≠ 0 AND degree(r) ≥ degree(d):
#     t ← lead(r)/lead(d)     # Divide the leading terms
#     q ← q + t
#     r ← r − t * d
#  return (q, r)

def polydiv(N,D):
    if D == 0:
        raise Exception("D cannot be equal to zero")
    
    Q = 0
    R = N
    while R != 0 and len(N) >= len(D):
        t = R[0]/D[0]
        Q = Q + t
        R = R - t * D
    return (Q,R)

print(polymult([1,0,2,1,0],[1,1,2,1],3))

P = [1,1,1,1]
Q = [0,1,1,0,1]

print(polyadd(P,Q,2))