from ModularArithmetic import modinv

# Finite fields can often be represented by polynomials with the aid of modular
# arithmetic. This is most useful for GF(p^n) when n is greater than 1.

# For our purposes polynomials will be in ASCENDING order
# x^0 is at index 0
# x^1 is at index 1
# x^2 is at index 2
# etc

# Print a list with identical spacing for each element
def eq_print(P,width=0):
    S = [str(co) for co in P]
    if width == 0:
        width = max(len(s) for s in S)
    for i in S:
        print("{:>{w}} ".format(i,w=width),end="")
    print()
    

# Convert the polynomial to the normal form by removing trailing zeroes
def poly_norm(P):
    while P[-1] == 0 and len(P) > 1:
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



def poly_print(P,mod):
    """Show the polynomial in descending form as it would be written"""
    # Get the degree of the polynomial in case it is in non-normal form
    d = poly_degree(P)
    
    if d == -1:
        if mod == 0:
            return f"0"
        else:
            return f"0 (mod {mod})"

    
    out = ""
    
    # Step through the ascending list of coefficients backward
    # We do this because polynomials are usually written in descending order
    for pwr in range(d,-1,-1):
        
        # Skip the zero coefficients entirely
        if P[pwr] == 0:
            continue
        
        coe = P[pwr]
        val = abs(coe)
        sgn = "-" if coe//val == -1 else "+"
                
        # When the coefficient is 1 or -1 don't print it unless it is the
        # coefficient for x^0
        if val == 1 and pwr != 0:
            val = ""
  
        # If it is the first term include the sign of the coefficient
        if pwr == d:
            if sgn == "+":
                sgn = ""
            
            # Handle powers of 1 and zero that appear as the first term
            if pwr == 1:
                s = "{}{}x".format(sgn,val)
            elif pwr == 0:
                s = "{}{}".format(sgn,val)
            else:
                s = "{}{}x^{}".format(sgn,val,pwr)
        
        # If power is 1 just show x rather than x^1
        elif pwr == 1:
            s = " {} {}x".format(sgn,val)
        
        # If the power is 0 only show the sign and value
        elif pwr == 0:
            s = " {} {}".format(sgn,val)
        
        # Otherwise show the sign, coefficient, and power
        else:
            s = " {} {}x^{}".format(sgn,val,pwr)
        
        out += s
    
    if mod == 0:
        return out
    else:
        out += " (mod {})".format(mod)
        return out

def poly_repr(P,mod):
    """Show the list and modulus"""
    out = str(P) + " mod {}".format(mod)
    return out
    


# Add two polynomiala modulo some number
def poly_add(P, Q, m = 0):
        
    pad = max(len(P),len(Q))
    
    P = poly_pad(P,pad)
    Q = poly_pad(Q,pad)
    
    out = []
    
    if m == 0:
        for x,y in zip(P,Q):
            out.append( x+y )
    else:
        for x,y in zip(P,Q):
            out.append( (x+y) % m)

    poly_norm(out)

    return out
    


# Multiply two polynomials modulo some number
def poly_mult(P, Q, m = 0):
    
    out = [0]*(len(P)+len(Q))
    
    
    if m == 0:
        for i in range(len(P)):
            for j in range(len(Q)):
                out[i+j] += P[i]*Q[j]
                out[i+j] = out[i+j]
    else:
        for i in range(len(P)):
            for j in range(len(Q)):
                out[i+j] += P[i]*Q[j]
                out[i+j] = out[i+j] % m
    
    poly_norm(out)

    return out

# Divide two polynomials modulo some number
def poly_divmod(P, Q, m = 0):
    # Don't modify the inputs
    P = P[:]
    Q = Q[:]
    
    # Remove unnecessary zeroes
    dP = poly_degree(P)
    dQ = poly_degree(Q)
    
    #Q = [0]*(len(P)-len(Q)) + Q
    
    # Check for division by zero    
    if poly_degree(Q) == -1:
        raise ZeroDivisionError
    
    # Use euclidean division for m = 0, representing no modulus
    if m == 0:
        if dP >= dQ:
            qt = [0] * dP
            while dP >= dQ:
                d = [0]*(dP - dQ) + Q
                mult = qt[dP - dQ] = P[-1] / d[-1]
                d = [coeff*mult for coeff in d]
                P = [ coeffN - coeffd for coeffN, coeffd in zip(P, d)]
                poly_norm(P)
                dP = poly_degree(P)
        else:
            qt = [0]
        return qt, P
    

    # Otherwise use modular arithmetic
    else:
        dP = len(P)-1
        dQ = len(Q)-1
        if dP >= dQ:
            qt = [0]*dP
            while dP >= dQ:
                d = [0]*(dP - dQ) + Q
                mult = qt[dP - dQ] = P[-1] * modinv(d[-1],m)
                d = [co*mult for co in d]
                P = [ (coeffP - coeffd) % m for coeffP, coeffd in zip(P, d)]
                poly_norm(P)
                dP = len(P)-1
            rm = [i % m for i in P]
        else:
            qt = [0]
            rm = [i % m for i in P]

    #poly_norm(qt)
    #poly_norm(rm)
    #print(qt)
    return qt,rm

def poly_derivative(P):
    P = P.copy()
    for i in range(len(P)):
        P[i] *= i
    return P[1:]


def numeric_check(x):
    """Check if a variable is an integer or float"""
    if isinstance(x, (int, float)) == False:
        raise TypeError("Must be float or integer")
        
#def poly_euclid_div(P,Q):
#    
#    qt = [0]*len(P)
#    rm = P
#    d = poly_degree(Q)
#    c = Q[-1]
#    while poly_degree(rm) >= d:
#        s = rm[-1]//c
#        qt[poly_degree(rm)-d] = s
#        rm = [r-s*q for q,r in zip(Q,rm)]
#    return (qt, rm)
#
#cA = [-42,0,-12,1]
#cB = [5,-3,1]
#cC = poly_euclid_div(cA,cB)
#print(cC)
#
#print(poly_add(poly_mult(cB,cC[0]),cC[1]))