from PolyUtils import poly_print, poly_add, poly_repr, poly_mult, \
                      poly_norm, poly_divmod

def degree(poly):
    if poly.coef[-1] == 0:
        return -1
    else:
        return len(poly.coef)-1

class polynomial:
    
    def __init__(self,coef,modulus=0):
        self.coef = coef
        self.modulus = modulus
    
    def __str__(self):
        return poly_print(self.coef,self.modulus)
    
    def __repr__(self):
        return poly_repr(self.coef,self.modulus)
    
    def __len__(self):
        return len(self.coef)-1
    
    def __add__(self,poly):
        if type(poly) == polynomial:
            L = poly_add(self.coef,poly.coef,self.modulus)
            return polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_add(self.coef,[poly],self.modulus)
            return polynomial(L,self.modulus)    
  
    def __mul__(self,poly):
        if type(poly) == polynomial:
            L = poly_mult(self.coef,poly.coef,self.modulus)
            return polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_mult(self.coef,[poly],self.modulus)
            return polynomial(L,self.modulus)
    
    def __pow__(self,pwr):
        if pwr == 0:
            return polynomial([0],self.modulus)
        if pwr == 1:
            return self
        else:
            out = self
            for i in range(pwr-1):
                out *= self
        return out
    
    def __eq__(self,poly):
        if degree(self) == degree(poly):
            if all([x == y for x,y in zip(self.coef,poly.coef)]):
                if self.modulus == poly.modulus:
                    return True
        return False

    
    def __divmod__(self,poly):
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(a,self.modulus), polynomial(b,self.modulus)

    def __floordiv__(self,poly):
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(a,self.modulus)
    
    def __mod__(self,poly):
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(b,self.modulus)
    

    def evaluate(self,x):
        out = 0
        for pwr,coef in enumerate(self.coef):
            out += coef*(x**pwr) % self.modulus
        return out % self.modulus

A = polynomial([1,2,3,4],5)
B = polynomial([4,3,4,2],5)
C = polynomial([1,2,3,4],5)
print(A)
print(repr(A))

print(A+B)

print(A*B)

print(A.evaluate(2))

#from Polynomials.PolynomialRepresentation import poly_divmod1
#R = [9,6,7,1,3,4,5]
#S = [1,1,0,1,1,0,0,0,1]
#print(poly_divmod1(S,R,9))


R = polynomial([9,6,7,1,3,4,5],9)
S = polynomial([1,1,0,1,1,0,0,0,1],9)
print(S//R)
print(S%R)

#print(dir(1.1))