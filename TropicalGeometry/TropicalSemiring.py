class Tropical:
    
    def __init__(self,val):
        self.val = val
    
    def __add__(self,b):
        return min(self.val,b.val)
    
    def __mul__(self,b):
        return self.val + b.val