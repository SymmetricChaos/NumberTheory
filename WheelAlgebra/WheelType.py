class Wheel:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def inv(self):
        return Wheel(self.b,self.a)
    
    def __add__(self,other):
        a = self.a*other.b + other.a*self.b
        b = self.b*other.b
        return Wheel(a,b)