from PolyUtils import poly_print, poly_add, poly_repr

class polynomial:
    
    def __init__(self,coef,modulus=0):
        self.coef = coef
        self.modulus = modulus
    
    def __str__(self):
        return poly_print(self.coef,self.modulus)
    
    def __repr__(self):
        return poly_repr(self.coef,self.modulus)
    
    def __add__(self,poly):
        L = poly_add(self.coef,poly.coef,self.modulus)
        return polynomial(L,self.modulus)
        
A = polynomial([1,2,3,4],5)
B = polynomial([4,3,4,2],5)

print(A)
print(B)
print(A+B)