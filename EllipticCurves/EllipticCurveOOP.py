# For elliptic curves over finite fields.

from ModularArithmetic import modinv

def elliptic_nonsingular(a,b,field):
    if (4*a**3 + 27*b**2) % field == 0:
        return False
    return True

def elliptic_points(a,b,field):
    if elliptic_nonsingular(a,b,field) == False:
        raise Exception("Elliptic curves must be non-singular")
        
    out = [(float('inf'),float('inf'))]
    for i in range(field):
        R = (i**3 + a*i + b) % field
        for j in range(field):
            L = (j**2) % field
            if R == L:
                out.append((i,j))
    return out

def elliptic_inv(P,curve):
    return (P[0],curve.field-P[1])


class elliptic:
    
    def __init__(self,a,b,field):
        self.a = a
        self.b = b
        self.field = field
        self.points = elliptic_points(a,b,field)


def elliptic_add(P,Q,curve):
    if P not in curve.points or Q not in curve.points:
        raise Exception('Points must be elements of the curve')
    
    # If the points are inverses they add up to zero, which here is the point at infinity
    if P == elliptic_inv(Q,curve):
        return (float('inf'),float('inf'))

    # Account for the additive identity
    if P == (float('inf'),float('inf')):
        return Q
    if Q == (float('inf'),float('inf')):
        return P


    if P == Q:
        m = (3*P[0]*P[0]+curve.a) * modinv(2*P[1], curve.field)
        
    else:
        m = (P[1]-Q[1])*modinv( P[0]-Q[0], curve.field )
    
    x = (m*m - P[0] - Q[0]) % curve.field
    y = -(P[1] + m*(x - P[0])) % curve.field
    
    if (x,y) not in curve.points:
        raise Exception('Something went wrong. The point {} is not on the curve.'.format((x,y)))
    
    return (x,y)


def elliptic_mult(P,n,curve):
    if P not in curve.points:
        raise Exception('Point must be elements of the curve')
    
    if n == 0:
        return (float('inf'),float('inf'))
    
    if n == 1:
        return P
    
    else:
        out = P
        for i in range(n-1):
            out = elliptic_add(out,P,curve)

    return out
    

