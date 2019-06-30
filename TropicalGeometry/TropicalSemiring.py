class Tropical:
    
    def __init__(self,val):
        self.val = val
    
    # Relations
    def __lt__(self,other):
        if type(other) == Tropical:
            return self.val-other.val < 0
        else:
            return self.val-other < 0
    
    def __gt__(self,other):
        if type(other) == Tropical:
            return self.val-other.val > 0
        else:
            return self.val-other > 0
    
    def __le__(self,other):
        if type(other) == Tropical:
            return self.val-other.val <= 0
        else:
            return self.val-other <= 0
    
    def __ge__(self,other):
        if type(other) == Tropical:
            return self.val-other.val >= 0
        else:
            return self.val-other >= 0
    
    def __eq__(self,other):
        if type(other) == Tropical:
            return self.val == other.val
        else:
            return self.val == other
    
    
    # Simple operations
    def __add__(self,b):
        if type(b) == Tropical:
            return Tropical(min(self.val,b.val))
        else:
            return Tropical(min(self.val,b))
        
    def __radd__(self,b):
        if type(b) == Tropical:
            return Tropical(min(self.val,b.val))
        else:
            return Tropical(min(self.val,b))
    
    def __mul__(self,b):
        if type(b) == Tropical:
            return Tropical(self.val+b.val)
        else:
            return Tropical(self.val+b)
        
    def __rmul__(self,b):
        if type(b) == Tropical:
            return Tropical(self.val+b.val)
        else:
            return Tropical(self.val+b)
        
    def __pow__(self,b):
        if type(b) == Tropical:
            return Tropical(self.val*b.val)
        else:
            return Tropical(self.val*b)
        
        

    # Otheer
    def __abs__(self):
        return Tropical(abs(self.val))


    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return str(self.val)
    
    def __float__(self):
        return float(self.val)
    
    
    def sym(self):
        return Tropical(-self.val)
    
    
    def __truediv__(self,b):
        return self * b.sym()
    

    def __floordiv__(self,b):
        return self * b.sym()