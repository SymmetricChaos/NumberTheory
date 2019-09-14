# Polynomials over the ordinary ring of integers.

from Polynomials.PolyUtils import poly_print, poly_add, poly_repr, poly_mult, \
                                  poly_divmod, poly_norm, poly_derivative

class IntPolynomial:
    
    def __init__(self,coef):
        assert type(coef) == list
        
        self.coef = coef
        self.normalize()
        
        
    def normalize(self):
        """Normalize the representation"""
        poly_norm(self.coef)


    def __str__(self):
        """Print nicely in descending written form"""
        return poly_print(self.coef)


    def __repr__(self):
        """Show literal contents in acending form"""
        return poly_repr(self.coef)


    def __len__(self):
        """Number of coefficients"""
        return len(self.coef)


    def __neg__(self):
        """Additive inverse of each coefficient"""
        L = [-c for c in self.coef]
        return IntPolynomial(L)


    def __add__(self,poly):
        """Add a polynomial to a polynomial"""
        if type(poly) != IntPolynomial:
            poly = IntPolynomial([poly])

        L = poly_add(self.coef,poly.coef)
        return IntPolynomial(L)


    def __radd__(self,poly):
        """Add a polynomial to a polynomial"""
        if type(poly) != IntPolynomial:
            poly = IntPolynomial([poly])

        L = poly_add(self.coef,poly.coef)
        return IntPolynomial(L)
        

    def __sub__(self,poly):
        """Subtract a polynomial from a polynomial"""
        if type(poly) != IntPolynomial:
            poly = IntPolynomial([poly])

        L = poly_add(self.coef,[-c for c in poly.coef])
        return IntPolynomial(L,self)


    def __rsub__(self,poly):
        """Subtract a polynomial from a polynomial"""
        if type(poly)  == int:
            poly = IntPolynomial([poly])

        L = poly_add(self.coef,[-c for c in poly.coef])
        return IntPolynomial(L)


    def __mul__(self,poly):
        """Multiply a polynomial by polynomial"""
        if type(poly)  == int:
            poly = IntPolynomial([poly])
            
        L = poly_mult(self.coef,poly.coef)
        return IntPolynomial(L)
            
        
    def __rmul__(self,poly):
        """Multiply a polynomial by polynomial"""
        if type(poly) == int:
            poly = IntPolynomial([poly])

        L = poly_mult(self.coef,poly.coef)
        return IntPolynomial(L)


    def __truediv__(self,poly):
        """Get the quotient of one polynomial by another"""
        if type(poly) == int:
            poly = IntPolynomial([poly])
        
        a,b = poly_divmod(self.coef,poly.coef)
        return IntPolynomial(a)


    def __rtruediv__(self,poly):
        """Get the quotient of one polynomial by another"""
        if type(poly) == int:
            poly = IntPolynomial([poly])
        
        a,b = poly_divmod(poly.coef,self.coef)
        return IntPolynomial(a)


    def __pow__(self,pwr):
        """Multiply a polynomial by itself"""
        if pwr == 0:
            return IntPolynomial([1])
        if pwr == 1:
            return self
        else:
            out = self
            for i in range(pwr-1):
                out *= self
        return out


    def __eq__(self,poly):
        """Check if two polynomials have the same coefficients"""
        if len(self) == len(poly):
            if all([x == y for x,y in zip(self.coef,poly.coef)]):
                return True
        return False

    
    def __divmod__(self,poly):
        """Get the quotient and remainder of one polynomial by another"""
        
        # Check for division by zero    
        if poly.coef == [0]
            raise ZeroDivisionError
        
        # Copy inputs
        P = self.coef[:]
        Q = poly.coef[:]
        
        # Integer cases 
        # THESE SEEM WRONG
        if len(Q) == 1:
            return [p/Q[0] for p in P], [0]

        if len(P) == 1:
            return [P[0]/q for q in Q], [0]
            
        # Use euclidean division
        dP = poly_degree(P)
        dQ = poly_degree(Q)
        if dP >= dQ:
            qt = [0] * dP
            while dP >= dQ:
                d = [0]*(dP - dQ) + Q
                mult = qt[dP - dQ] = P[-1] / d[-1]
                d = [coeff*mult for coeff in d]
                P = [ coeffN - coeffd for coeffN, coeffd in zip(P, d)]
                poly_norm(P)
                dP = poly_degree(P)
        else:
            qt = [0]
        return qt, P
    
#        return IntPolynomial(a), IntPolynomial(b)


    def __mod__(self,poly):
        """Get the remainder of one polynomial divided by another"""
        a,b = poly_divmod(self.coef,poly.coef)
        return IntPolynomial(b)
    
    
    def __getitem__(self,n):
        """Make polynomial accessible by indexing"""
        return self.coef[n]
    

    def derivative(self,silent=False):
        """Calculate the derivative of the polynomial"""
        c = poly_derivative(self.coef)
        return IntPolynomial(c)


    def evaluate(self,X):
        """Evaluate the polynomial at a given point or points"""
        if type(X) != list:
            X = [X]
        out = [0]*len(X)
        for pwr,coef in enumerate(self.coef):
            for pos,x in enumerate(X):
                out[pos] = (out[pos] + coef*(x**pwr))
        
        if len(out) == 1:
            return out[0]
        return out
    

    def __round__(self,digits):
        return IntPolynomial([round(i,digits) for i in self.coef])


    def degree(self):
        """Degree of the polynomial"""
        return len(self)-1