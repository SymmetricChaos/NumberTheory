class Tropical:
    
    def __init__(self,val):
        self.val = val
    
    def __add__(self,b):
        if type(b) == Tropical:
            return Tropical(min(self.val,b.val))
        else:
            return Tropical(min(self.val,b))
    
    
    def __mul__(self,b):
        if type(b) == Tropical:
            return Tropical(self.val+b.val)
        else:
            return Tropical(self.val+b)
        
    
    def __pow__(self,b):
        if type(b) == Tropical:
            return Tropical(self.val*b.val)
        else:
            return Tropical(self.val*b)


    def __abs__(self):
        return Tropical(abs(self.val))


    def __str__(self):
        return str(self.val)