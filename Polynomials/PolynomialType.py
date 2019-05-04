from Polynomials.PolyUtils import poly_print, poly_add, poly_repr, poly_mult, \
                      poly_divmod, poly_norm, poly_derivative


class Polynomial:
    
    def __init__(self,coef,modulus=None):
        self.coef = coef
        if modulus == None:
            self.modulus = 0
        else:
            self.modulus = modulus
        self.norm()
        
        
    def norm(self):
        """Normalize the representation"""
        poly_norm(self.coef)
        if self.modulus != 0:
            for i in range(len(self.coef)):
                self.coef[i] = self.coef[i] % self.modulus


    def __str__(self):
        """Print nicely in descending written form"""
        return poly_print(self.coef,self.modulus)


    def __repr__(self):
        """Show literal contents in acending form"""
        return poly_repr(self.coef,self.modulus)


    def __len__(self):
        """Degree for nonzero Polynomials"""
        return len(self.coef)-1


    def __add__(self,poly):
        """Add an integer or Polynomial to a Polynomial using the modulus of the first argument"""
        if type(poly) == Polynomial:
            L = poly_add(self.coef,poly.coef,self.modulus)
            return Polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_add(self.coef,[poly],self.modulus)
            return Polynomial(L,self.modulus)    

    def __sub__(self,poly):
        """Add an integer or Polynomial to a Polynomial using the modulus of the first argument"""
        if type(poly) == Polynomial:
            L = poly_add(self.coef,[-c for c in poly.coef],self.modulus)
            return Polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_add(self.coef,[-poly],self.modulus)
            return Polynomial(L,self.modulus)    

    def __neg__(self):
        """Additive inverse of each coefficient"""
        L = [-c for c in self.coef]
        return Polynomial(L,self.modulus)

    def __mul__(self,poly):
        """Multiply a Polynomial by an integer or Polynomial using the modulus of the first argument"""
        if type(poly) == Polynomial:
            L = poly_mult(self.coef,poly.coef,self.modulus)
            return Polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_mult(self.coef,[poly],self.modulus)
            return Polynomial(L,self.modulus)


    def __pow__(self,pwr):
        """Multiply a Polynomial by itself"""
        if pwr == 0:
            return Polynomial([0],self.modulus)
        if pwr == 1:
            return self
        else:
            out = self
            for i in range(pwr-1):
                out *= self
        return out


    def __eq__(self,poly):
        """Check if two Polynomial have the same coefficient and are over the same field"""
        if len(self) == len(poly):
            if all([x == y for x,y in zip(self.coef,poly.coef)]):
                if self.modulus == poly.modulus:
                    return True
        return False

    
    def __divmod__(self,poly):
        """Get the quotient and modulus of one Polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return Polynomial(a,self.modulus), Polynomial(b,self.modulus)


    def __truediv__(self,poly):
        """Get the quotient of one Polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return Polynomial(a,self.modulus)
    

    def __mod__(self,poly):
        """Get the modulus of one Polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return Polynomial(b,self.modulus)
    

    def derivative(self):
        """Calculate the derivative of the Polynomial"""
        c = poly_derivative(self.coef)
        return Polynomial(c,self.modulus)


    def evaluate(self,X):
        """Evaluate the Polynomial at a given point or points"""
        if type(X) != list:
            X = [X]
        out = [0]*len(X)
        for pwr,coef in enumerate(self.coef):
            for pos,x in enumerate(X):
                if self.modulus != 0:
                    out[pos] = (out[pos] + coef*(x**pwr)) % self.modulus
                else:
                    out[pos] = (out[pos] + coef*(x**pwr))
        return out
