class Tropical:
    
    def __init__(self,val):
        self.val = val
    
    def __add__(self,b):
        return Tropical(min(self.val,b.val))
    
    def __mul__(self,b):
        return Tropical(self.val + b.val)
    
    def __pow__(self,b):
        return Tropical(self.val*b.val)