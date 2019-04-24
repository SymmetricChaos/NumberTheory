from ModularArithmetic import gcd, lcm

class Rational:
    
    def __init__(self,n,d=1):
        self.n = n
        self.d = d
        self.simplify()
    
    def simplify(self):
        g = gcd(self.n,self.d)
        self.n = self.n//g
        self.d = self.d//g
    
    def __str__(self):
        return str(self.n) + "/" + str(self.d)
    
    def __mul__(self,multiplier):
        
        if type(multiplier) == int:
            multiplier = Rational(multiplier)
        
        n = self.n * multiplier.n
        d = self.d * multiplier.d
        return Rational(n,d)
        
    def __rmul__(self,multiplier):
        return self*multiplier
    
    def __add__(self,addend):
        
        if type(addend) == int:
            addend = Rational(addend)
        
        L = lcm(self.d,addend.d)
        
        n = (L//self.d)*self.n + (L//addend.d)*addend.n
        d = L
        
        return Rational(n,d)
    
    def __radd__(self,addend):
        return self+addend
        
    
q = Rational(2,10)

print(q)
q.simplify()
print(q)
print(q*q)
print(q*3)
print(3*q)
print(1+q)
print(q+1)