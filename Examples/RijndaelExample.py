from Polynomials import Polynomial

# The finite field GF(2^8) with 256 elements has various expressions

# The Rijndael polynomial 
R = Polynomial([1,1,0,1,1,0,0,0,1],2)
class Rijndael:
    
    def __init__(self,coef):
        assert len(coef) < 9
        self.poly = Polynomial(coef,modulus=2)
    
    def __add__(self,Q):
        assert type(self) == Rijndael
        assert type(Q) == Rijndael
        
        a = (self.poly+Q.poly) % R
        return Rijndael(a.coef)
    
    def __mul__(self,Q):
        assert type(self) == Rijndael
        assert type(Q) == Rijndael
        
        a = (self.poly*Q.poly) % R
        return Rijndael(a.coef)
    
    def __str__(self):
        c = [str(i) for i in reversed(self.poly.coef)]
        c = "".join(c)
        return f"{c:>8}"
    
    def __repl__(self):
        s = ""
        for i in reversed(self.poly.coef):
            s += str(i)
        return s


P = Rijndael([0,1,1,0,1,1,1,1])
Q = Rijndael([1,0,1,0,1])

print(P)
print(Q)
print(P+Q)