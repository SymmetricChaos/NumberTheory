from PolyUtils import poly_print, poly_add, poly_repr, poly_mult, \
                      poly_norm, poly_divmod

def degree(poly):
    if poly.coef[-1] == 0:
        return -1
    else:
        return len(poly.coef)-1

class polynomial:
    
    def __init__(self,coef,modulus=0):
        self.coef = poly_norm(coef,modulus)
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
        print(self.coef)
        print(poly.coef)
        div,mod = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(div,self.modulus), polynomial(mod,self.modulus)
    
    def evaluate(self,x):
        out = 0
        for pwr,coef in enumerate(self.coef):
            out += coef*(x**pwr) % self.modulus
        return out % self.modulus
    
A = polynomial([1,2,3,4],5)
B = polynomial([4,3,4,2],5)
C = polynomial([1,2,3,4],5)
print(A)
print(B)
print(A+B)

print(A)
print(B)
print(A*B)
print(divmod(A,C))

print(dir(1))