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


class Elliptic_Curve:
    def __init__(self,a,b,f):
        self.a = a
        self.b = b
        self.f = f
    
    def points(self):
        return elliptic_points(self.a, self.b, self.f)
    
    def __eq__(self,other):
        if self.a != other.a or self.b != other.b or self.f != other.f:
            return False
        return True
        

class Elliptic_Point:
    def __init__(self,x,y,curve):
        
        if x != float('inf') and y != float('inf'):
            if (y**2) % curve.f != (x**3 + curve.a*x + curve.b) % curve.f:
                raise Exception("Points are not on specified curve")
        
        self.x = x
        self.y = y
        self.a = curve.a
        self.b = curve.b
        self.f = curve.f
        self.curve = curve
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    
    def __eq__(self,other):
        
        if self.x == other.x and self.y == other.y:
            if self.a == other.a and self.b == other.b:
                if self.f == other.f:
                    return True
        return False
    
    def inv(self):
        return Elliptic_Point(self.x, (self.f-self.y) % self.f, self.curve)
    
    def identity(self):
        return Elliptic_Point(float('inf'),float('inf'),self.curve)

    
    def __add__(self,other):
        if self.curve != other.curve:
            raise Exception("Points are from different curves")
    
        if self == other.inv():
            return self.identity()

        
        # Account for the additive identity
        if self == self.identity():
            return other
        if other == other.identity():
            return self
    
        if self == other:
            m = (3*self.x*self.x+self.a) * modinv(2*self.y, self.f)
        else:
            m = (self.y-other.y)*modinv( self.x-other.x, self.f )
    
        
        x = (m*m - self.x - other.x) % self.f
        y = -(self.y + m*(x - self.x)) % self.f
        return Elliptic_Point(x, y, self.curve)
    
    def __mul__(self,scalar):
        if scalar == 0:
            return self.identity()
        if scalar == 1:
            return self
        else:
            out = self
            for i in range(scalar-1):
                out += self
            return out
    
C = Elliptic_Curve(2,3,97)
#print(C.points())
a = Elliptic_Point(3,6,C)
b = Elliptic_Point(3,6,C)
print(a+b)
print(a*6)
