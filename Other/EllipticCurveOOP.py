# For elliptic curves over finite fields.

from ModularArithmetic import modinv

def elliptic_nonsingular(a,b,field):
    if (4*a**3 + 27*b**2) % field == 0:
        return False
    return True

def elliptic_points(a,b,field):
    if elliptic_nonsingular(a,b) == False:
        raise Exception("Elliptic curves must be non-singular")
        
    out = [(0,0),(float('inf'),float('inf'))]
    for i in range(field):
        R = (i**3 + a*i + b) % field
        for j in range(field):
            L = (j**2) % field
            if R == L:
                out.append((i,j))
    return out

class elliptic:
    
    def __init__(self,a,b,field):
        self.a = a
        self.b = b
        self.field = field
        self.points = elliptic_points(a,b,field)

def elliptic_add(P,Q,curve):
    if P not in curve.points or Q not in curve.points:
        raise Exception('Points must be elements of the curve')
    