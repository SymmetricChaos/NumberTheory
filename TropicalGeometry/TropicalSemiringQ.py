class Tropical:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
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
        
#    def sym(self):
#        return Tropical(1/self.val)
#    
#    
#
#    def __abs__(self):
#        return Tropical(abs(self.val))
#
#
#    def __str__(self):
#        return str(self.a/self.b)
#    
#    
#
#    
#    
#    def __truediv__(self,b):
#        return self * b.sym()
#    
#
#    def __floordiv__(self,b):
#        return self * b.sym()