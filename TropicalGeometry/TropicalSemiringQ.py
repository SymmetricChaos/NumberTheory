from ModularArithmetic import gcd

class Tropical:

    def __init__(self,a,b):
        if b < 0:
            b = abs(b)
            a = -a
        g = abs(gcd(a,b))
        self.a = a//g
        self.b = b//g

    # Comparisons
    def __le__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return self.a+other.b <= other.a+self.b

    def __lt__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return self.a+other.b < other.a+self.b

    def __ge__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return self.a+other.b >= other.a+self.b

    def __gt__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return self.a+other.b > other.a+self.b

    def __eq__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return self.a == other.a and self.b == other.b

    # Simple Operations
    def __add__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return min(self, other)
    
    def __radd__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return min(self, other)

    def __mul__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return Tropical(self.a**other.b * other.a**self.b, self.b**other.b)
    
    def __rmul__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return Tropical(self.a**other.b * other.a**self.b, self.b**other.b)
    
    
    def __pow__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return Tropical(self.a*other.a, self.b*other.b)

    def __truediv__(self,other):
        if type(other) == int:
            other = Tropical(other,1)
        return self * other.sym()
    
    # Other
    def __str__(self):
        if self.b == 1:
            return f"{self.a}"
        return f"{self.a}/{self.b}"
    
    def __repr__(self):
        if self.b == 1:
            return f"{self.a}"
        return f"{self.a}/{self.b}"

    def sym(self):
        return Tropical(self.b,self.a)

    def __abs__(self):
        return Tropical(abs(self.a),abs(self.b))
    
