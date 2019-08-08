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
            return str(self.a)
        return str(self.a) + "/" + str(self.b)
    
    def __add__(self,other):
        a = self.a*other.b + other.a*self.b
        b = self.b*other.b
        return Wheel(a,b)
    
    def __neg__(self):
        return Wheel(-self.a,self.b)
    
    def __mul__(self,other):
        a = self.a*other.a 
        b = self.b*other.b
        return Wheel(a,b)
    
    def __truediv__(self,other):
        return Wheel(self*other.inv)
    
x = Wheel(2,3)
y = Wheel(3,5)
z = Wheel(5,7)

add_id = Wheel(0,1)
mul_id = Wheel(1,1)

ab = Wheel(0,0)

a = Wheel(1,0)

print(f"{add_id} * {ab} = {add_id * ab}")
print(f"{add_id} + {ab} = {add_id + ab}")
print()
print(f"{x} + {y} = {x + y}")
print(f"{x} * {z} = {x * z}")
print()
print(f"{a} + {y} = {a + y}")
print(f"{a} * {y} = {a * y}")