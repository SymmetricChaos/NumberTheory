from ModularArithmetic import gcd, lcm

class Rational:
    
    def __init__(self,n,d):
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
            n = self.n * multiplier
            d = self.d
            return Rational(n,d)
        elif type(multiplier) == Rational:
            n = self.n * multiplier.n
            d = self.d * multiplier.d
            return Rational(n,d)
        
    def __rmul__(self,multiplier):
        return self*multiplier
    
    def __add__(self,addend):
        
        if type(addend) == int:
            addend = Rational(addend,1)
        
        L = lcm(self.d,addend.d)
        
        n = (L//self.d)*self.n + (L//addend.d)*addend.n
        d = L
        
        return Rational(n,d)
        
    
q = Rational(2,10)

print(q)
q.simplify()
print(q)
print(q*q)
print(q*3)
print(3*q)
print(q+q*q+1)