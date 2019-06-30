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
        return self.a+other.b <= other.a+self.b
    
    def __lt__(self,other):
        return self.a+other.b < other.a+self.b

    def __ge__(self,other):
        return self.a+other.b >= other.a+self.b

    def __gt__(self,other):
        return self.a+other.b > other.a+self.b

    def __eq__(self,other):
        return self.a == other.a and self.b == other.b

    # Simple Operations
    def __add__(self,other):
        return min(self, other)   

    def __mul__(self,other):
        return Tropical(self.a+other.a, self.b+other.b)
        
    def __pow__(self,other):
        return Tropical(self.a*other.a, self.b*other.b)
        
    def __truediv__(self,other):
        return self * other.sym()
    
    # Other
    def __str__(self):
        return f"{self.a}/{self.b}"
    
    def sym(self):
        return Tropical(self.b,self.a)
    
    def __abs__(self):
        return Tropical(abs(self.a),abs(self.b))
    
