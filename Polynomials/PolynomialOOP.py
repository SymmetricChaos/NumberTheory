from PolyUtils import poly_print, poly_add, poly_repr, poly_mult, \
                      poly_divmod, poly_norm


runtime_constants = {"modulus" : 0,
                     "show_mod" : True}

def degree(poly):
    if poly.coef[-1] == 0:
        return -1
    else:
        return len(poly.coef)-1

def set_modulus(n):
    runtime_constants["modulus"] == n


class polynomial:
    
    
    def __init__(self,coef,modulus=None):
        self.coef = coef
        if modulus == None:
            self.modulus = runtime_constants["modulus"]
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
        """Degree for nonzero polynomials"""
        return len(self.coef)-1


    def __add__(self,poly):
        """Add an integer or polynomial to a polynomial using the modulus of the first argument"""
        if type(poly) == polynomial:
            L = poly_add(self.coef,poly.coef,self.modulus)
            return polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_add(self.coef,[poly],self.modulus)
            return polynomial(L,self.modulus)    


    def __mul__(self,poly):
        """Multiply a polynomial by an integer or polynomial using the modulus of the first argument"""
        if type(poly) == polynomial:
            L = poly_mult(self.coef,poly.coef,self.modulus)
            return polynomial(L,self.modulus)
        
        if type(poly) == int:
            L = poly_mult(self.coef,[poly],self.modulus)
            return polynomial(L,self.modulus)


    def __pow__(self,pwr):
        """Multiply a polynomial by itself"""
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
        """Check if two polynomial have the same coefficient and are over the same field"""
        if degree(self) == degree(poly):
            if all([x == y for x,y in zip(self.coef,poly.coef)]):
                if self.modulus == poly.modulus:
                    return True
        return False

    
    def __divmod__(self,poly):
        """Get the quotient and modulus of one polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(a,self.modulus), polynomial(b,self.modulus)


    def __floordiv__(self,poly):
        """Get the quotient of one polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(a,self.modulus)
    

    def __mod__(self,poly):
        """Get the modulus of one polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return polynomial(b,self.modulus)
    

    def evaluate(self,X):
        """Evaluate the polynomial at a given point or points"""
        if type(X) != list:
            X = [X]
        out = [0]*len(X)
        for pwr,coef in enumerate(self.coef):
            for pos,x in enumerate(X):
                out[pos] = (out[pos] + coef*(x**pwr)) % self.modulus
        return out
