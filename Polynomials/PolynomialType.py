from Polynomials.PolyUtils import poly_print, poly_add, poly_repr, poly_mult, \
                                  poly_divmod, poly_norm, poly_derivative

class Polynomial:
    
    def __init__(self,coef,modulus=0):
        assert type(coef) == list
        self.coef = coef
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
        """Number of coefficients"""
        return len(self.coef)


    def __neg__(self):
        """Additive inverse of each coefficient"""
        L = [-c for c in self.coef]
        return Polynomial(L,self.modulus)

    def __add__(self,poly):
        """Add a polynomial to a polynomial"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")

        L = poly_add(self.coef,poly.coef,self.modulus)
        return Polynomial(L,self.modulus)


    def __radd__(self,poly):
        """Add a polynomial to a polynomial"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")

        L = poly_add(self.coef,poly.coef,self.modulus)
        return Polynomial(L,self.modulus)
        

    def __sub__(self,poly):
        """Subtract a polynomial from a polynomial"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")

        L = poly_add(self.coef,[-c for c in poly.coef],self.modulus)
        return Polynomial(L,self.modulus)

    def __rsub__(self,poly):
        """Subtract a polynomial from a polynomial"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")

        L = poly_add(self.coef,[-c for c in poly.coef],self.modulus)
        return Polynomial(L,self.modulus)


    def __mul__(self,poly):
        """Multiply a polynomial by polynomial"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
            
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")
        L = poly_mult(self.coef,poly.coef,self.modulus)
        return Polynomial(L,self.modulus)
            
        
    def __rmul__(self,poly):
        """Multiply a polynomial by polynomial"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")

        L = poly_mult(self.coef,poly.coef,self.modulus)
        return Polynomial(L,self.modulus)


    def __truediv__(self,poly):
        """Get the quotient of one polynomial by another"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")
        
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return Polynomial(a,self.modulus)


    def __rtruediv__(self,poly):
        """Get the quotient of one polynomial by another"""
        if type(poly) != Polynomial:
            poly = Polynomial([poly])
        if self.modulus != poly.modulus:
            raise Exception("Modulus does not match.")
        
        a,b = poly_divmod(poly.coef,self.coef,self.modulus)
        return Polynomial(a,self.modulus)


    def __pow__(self,pwr):
        """Multiply a polynomial by itself"""
        if pwr == 0:
            return Polynomial([1],self.modulus)
        if pwr == 1:
            return self
        else:
            out = self
            for i in range(pwr-1):
                out *= self
        return out


    def __eq__(self,poly):
        """Check if two polynomials have the same coefficient and are over the same field"""
        if len(self) == len(poly):
            if all([x == y for x,y in zip(self.coef,poly.coef)]):
                if self.modulus == poly.modulus:
                    return True
        return False

    
    def __divmod__(self,poly):
        """Get the quotient and remainder of one polynomial by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return Polynomial(a,self.modulus), Polynomial(b,self.modulus)


    def __mod__(self,poly):
        """Get the remainder of one polynomial divided by another"""
        a,b = poly_divmod(self.coef,poly.coef,self.modulus)
        return Polynomial(b,self.modulus)
    
    
    def __getitem__(self,n):
        """Make polynomial accessible by indexing"""
        return self.coef[n]
    

    def derivative(self,silent=False):
        """Calculate the derivative of the polynomial"""
        if self.modulus != 0 and silent == False:
            print("Warning! Derivative is not well defined.")
        c = poly_derivative(self.coef)
        return Polynomial(c,self.modulus)


    def evaluate(self,X):
        """Evaluate the polynomial at a given point or points"""
        if type(X) != list:
            X = [X]
        out = [0]*len(X)
        for pwr,coef in enumerate(self.coef):
            for pos,x in enumerate(X):
                if self.modulus != 0:
                    out[pos] = (out[pos] + coef*(x**pwr)) % self.modulus
                else:
                    out[pos] = (out[pos] + coef*(x**pwr))
        
        if len(out) == 1:
            return out[0]
        return out
    
    def __round__(self,digits):
        return Polynomial([round(i,digits) for i in self.coef],modulus=self.modulus)

    def degree(self):
        """Degree of the polynomial"""
        return len(self)-1