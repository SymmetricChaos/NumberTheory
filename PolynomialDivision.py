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


# Remove zeroes from the end of a polynomial
def poly_norm(P):
    while P[-1] == 0:
        if len(P) == 1:
            break
        P.pop()


# Determine the degree of a polynomial
def poly_degree(P):
    P = P.copy()
    poly_norm(P)
    
    # The zero polynomial is treated as having degree -1
    if P[-1] == 0:
        return -1
    
    return len(P)-1



# Pad a polynomial with zeroes
def poly_pad(P,n):
    out = P.copy()
    while len(out) < n:
        out.append(0)
    return out



def poly_print(P):
    
    # Get the degree of the polynomial in case it is in non-normal form
    d = poly_degree(P)
    
    # Step through the ascending list backward
    for i in range(d,-1,-1):
        
        
        coe = P[i]
        val = abs(coe)
        sgn = "-" if coe//val == -1 else "+"
        
        if val == 1:
            val = ""
        
        # Skip the zero coefficients
        if P[i] == 0:
            continue
        
        # If it is the first term include the sign of the coefficient
        elif i == d:
            s = "{}{}x^{} ".format(sgn,val,i)
        
        # If power is 1 just show x
        elif i == 1:
            s = " {} {}x".format(sgn,val)
        
        # If the power is 0 only show the sign and value
        elif i == 0:
            s = " {} {}".format(sgn,val)
        
        # Otherwise show the sign, coefficient, and power
        else:
            s = "{} {}x^{}".format(sgn,val,i)
        
        print(s,end="")
    print()


# Add two polynomiala modulo some number
def poly_add(P,Q,m=2):
    
    pad = max(len(P),len(Q))
    
    P = poly_pad(P,pad)
    Q = poly_pad(Q,pad)
    
    out = []
    for x,y in zip(P,Q):
        out.append( x+y % m)
    
    return out
    


# Multiply two polynomials modulo some number
def poly_mult(P,Q,m=2):
    
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



# Divide two polynomial modulo some number
def poly_divmod(P, Q, m=2):
    # Don't modify the inputs
    P = P[:]
    Q = Q[:]
    
    # Remove unnecessary zeroes
    poly_norm(P)
    poly_norm(Q)
    
    # Record the degree of the polynomials
    dP = len(P)-1
    dQ = len(Q)-1
    
    if poly_degree(Q) == -1:
        raise ZeroDivisionError
    
    if dP >= dQ:
        qt = [0]*dP
        while dP >= dQ:
            d = [0]*(dP - dQ) + Q
            mult = qt[dP - dQ] = P[-1] * modinv(d[-1],m) #P[-1] // d[-1]
            d = [co*mult for co in d]
            P = [ (coeffP - coeffd) % m for coeffP, coeffd in zip(P, d)]
            poly_norm(P)
            dP = len(P)-1
        rm = P
    else:
        qt = [0]
        rm = P
    
    
    poly_norm(qt)
    poly_norm(rm)
    
    #qt = [int(i) for i in qt]
    
    return qt,rm


P = [-42,1,-12,-1,0,0]
Q = [-3,1,0,0]

print(P)
poly_print(P)
print()

P = [0,1,1,1,1,1,1,0,1,1,1,1,1,1]
Q = [1,1,0,1,1,0,0,0,1]

#print(polyadd(P,Q,2))
#print(polymult([1,0,2,1,0],[1,1,2,1],3))

print(P)
print(Q)
print()
print(poly_divmod(P,Q,2))