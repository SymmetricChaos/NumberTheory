from ModularArithmetic import gcd

class Rational:
    
    def __init__(self,n,d=1):
        assert type(n) == int
        assert type(d) == int
        if d < 0:
            d = abs(d)
            n = -n
        self.n = n
        self.d = d
        self.simplify()


    def simplify(self):
        g = abs(gcd(self.n,self.d))
        self.n = self.n//g
        self.d = self.d//g


    def inv(self):
        return Rational(self.d,self.n)


    def __neg__(self):
        return Rational(-self.n,self.d)


    def __str__(self):
        return str(self.n) + "/" + str(self.d)


    def __mul__(self,multiplier):
        
        n = self.n * multiplier.n
        d = self.d * multiplier.d
        
        return Rational(n,d)


    def __rmul__(self,multiplier):
        return self*multiplier


    def __truediv__(self,divisor):
        return self*divisor.inv()


    def __add__(self,addend):
        
        n = self.n*addend.d + addend.n*self.d
        d = self.d*addend.d

        return Rational(n,d)


    def __radd__(self,addend):
        return self + addend


    def __sub__(self,addend):
        return self + -addend


    def __rsub__(self,addend):
        return addend + -self


    def __eq__(self,other):
        if self.n == other.n:
            if self.d == other.d:
                return True
        return False
    
A = Rational(4,-10)
B = Rational(7,16)
print(A)
print(B)
print(A+B)
print(A-A)
print(A*B)
print(-A)
print(A-B)
print(A==A)
print(A==B)
print(A.inv()+A)
print(A/B)