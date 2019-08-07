from ModularArithmetic import gcd

class Wheel:
    
    def __init__(self,a,b):
        assert type(a) == int
        assert type(b) == int
        if b != 0:
            g = abs(gcd(a,b))
            self.a = a//g
            self.b = b//g
        else:
            self.a = a
            self.b = b
        
        
    def inv(self):
        return Wheel(self.b,self.a)
    
    def __str__(self):
        if self.b == 1:
            return str(self.n)
        return str(self.a) + "/" + str(self.b)
    
    def __add__(self,other):
        a = self.a*other.b + other.a*self.b
        b = self.b*other.b
        return Wheel(a,b)
    
    def __mul__(self,other):
        a = self.a*other.a 
        b = self.b*other.b
        return Wheel(a,b)
    
x = Wheel(2,3)
y = Wheel(3,5)
z = Wheel(5,7)
e = Wheel(0,1)

print(x,y,x)
print((x+y)*z+e*z)
print(x*z + y*z)

a = Wheel(0,0)
print(a*e)