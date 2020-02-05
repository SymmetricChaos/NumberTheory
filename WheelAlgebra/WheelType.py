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
    
#    def __eq__(self,other):
#        if self.a == other.a:
#            if self.b == other.b:
#                return True
#        return False


if __name__ == '__main__':
    print("A wheel is a structure in which division is always defined, even division by zero")
    print("This has some strange consequences. In a field, the usual way of doing arithmetic, zero is an absorbing element. That means anything times zero is zero. However this is no longer true in a wheel.")
    
    
    
    x = Wheel(2,3)
    y = Wheel(3,5)
    z = Wheel(5,7)
    
    add_id = Wheel(0,1)
    mul_id = Wheel(1,1)
    
    nullity = Wheel(0,0)
    
    a = Wheel(1,0)
    
    print(f"{add_id} * {nullity} = {add_id * nullity}")
    print(f"{add_id} + {nullity} = {add_id + nullity}")
    print()
    print(f"{x} + {y} = {x + y}")
    print(f"{x} * {z} = {x * z}")
    print()
    print(f"{a} + {y} = {a + y}")
    print(f"{a} * {y} = {a * y}")
    print(f"{x} + {nullity} = {x + nullity}")
    print(f"{a} * {add_id} = {x * add_id}")