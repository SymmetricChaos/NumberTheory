# Univariate polynomials with coefficients from any ring


from Polynomials.PolyUtils import poly_print, poly_add, poly_mult
from Polynomials.PolynomialIntegerTypeUtils import poly_print_simple

class RPoly:
    
    def __init__(self,coef):
        assert type(coef) == list
        self.coef = coef
        self.normalize()
        

    def __getitem__(self,n):
        """Make polynomial accessible by indexing"""
        return self.coef[n]


    def __setitem__(self,n,val):
        """Allow valid coefficients to be set"""
        assert type(val) == int, "Coefficients must be integers"
        self.coef[n] = val


    def __call__(self,x):
        """Evaluate the polynomial at a given point"""
        out = 0
        for pwr,coef in enumerate(self.coef):
            out = out + coef*(x**pwr)
        return out


    def __str__(self):
        """Print nicely in descending written form"""
        return poly_print_simple(self)


    def __repr__(self):
        """Print nicely in descending written form"""
        return poly_print(self.coef)


    def __len__(self):
        """Number of coefficients"""
        return len(self.coef)


    def __neg__(self):
        """Additive inverse of each coefficient"""
        L = [-c for c in self.coef]
        return RPoly(L)


    def __add__(self,poly):
        """Add a polynomial to a polynomial"""
        if type(poly) != RPoly:
            poly = RPoly([poly])

        L = poly_add(self.coef,poly.coef)
        return RPoly(L)


    def __radd__(self,poly):
        """Polynomial addition is commutative"""
        return self + poly


    def __sub__(self,poly):
        """Subtract a polynomial from a polynomial"""
        if type(poly) != RPoly:
            poly = RPoly([poly])

        L = poly_add(self.coef,[-c for c in poly.coef])
        return RPoly(L,self)


    def __rsub__(self,poly):
        """Subtract a polynomial from a polynomial"""
        if type(poly)  == int:
            poly = RPoly([poly])

        L = poly_add(self.coef,[-c for c in poly.coef])
        return RPoly(L)


    def __mul__(self,poly):
        """Multiply a polynomial by polynomial"""
        if type(poly)  == int:
            poly = RPoly([poly])
            
        L = poly_mult(self.coef,poly.coef)
        return RPoly(L)


    def __rmul__(self,poly):
        """Multiply a polynomial by polynomial"""
        return self*poly


    def __pow__(self,pwr):
        """Multiply a polynomial by itself"""
        if pwr == 0:
            return RPoly([1])
        if pwr == 1:
            return self
        else:
            assert type(pwr) == int, f"{pwr} is not an integer"
            assert type(pwr) > 0, f"{pwr} is negative"
            out = self.copy()
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
        """Algorithm for euclidean division of polynomials"""

        # Cast integer to poly if needed
        if type(poly) == int:
            poly = RPoly([poly])
        assert type(poly) == RPoly, f"Could not cast {poly} to integer polynomial"

        # Check for division by zero    
        if poly.coef == [0]:
            raise ZeroDivisionError

        # We can only divide a longer polynomial by a shorter one
        if len(self) < len(poly):
            return RPoly([0]), self.copy()

        # Copy inputs
        P = self.coef[:]
        Q = poly.coef[:]

        # Integer case, an RPoly could have length one on its own and
        # thus represent an integer
        if len(poly) == 1:
            c = self.content()
            if c % poly.coef[0] == 0:
                return RPoly([p//Q[0] for p in P]), RPoly([0])
            else:
                raise Exception(f"Integer division of {self} by {poly} is not defined")
        # Use euclidean division algorithm
        else:
            # Check that division is defined
            for p in P:
                if p % Q[-1] != 0:
                    raise Exception(f"Integer division of {self} by {poly} is not defined")

            dP = len(P)-1
            dQ = len(Q)-1
            if dP >= dQ:
                qt = [0] * dP
                while dP >= dQ:
                    
                    d = [0]*(dP - dQ) + Q
                    mult = qt[dP - dQ] = P[-1] // d[-1]
                    d = [coeff*mult for coeff in d]
                    P = [ coeffN - coeffd for coeffN, coeffd in zip(P, d)]
                    while P[-1] == 0 and len(P) > 1:
                        if len(P) == 1:
                            break
                        P.pop()
                    dP = len(P)-1
            
            return RPoly(qt), RPoly(P)


    def __floordiv__(self,poly):
        """Integer division of polynomials"""
        a,b = divmod(self,poly)
        return a


    def __mod__(self,poly):
        """Remainder of integer division of polynomials"""
        a,b = divmod(self,poly)
        return b


    def normalize(self):
        """Remove trailing zeroes"""
        while self.coef[-1] == 0 and len(self.coef) > 1:
            if len(self.coef) == 1:
                break
            self.coef.pop()


    def copy(self):
        """Copy the polynomial"""
        return RPoly(self.coef[:])


    def derivative(self):
        """Calculate the formal derivative of the polynomial"""
        co = self.coef.copy()
        for i in range(len(co)):
            co[i] *= i
        return RPoly(co[1:])


    def evaluate(self,X):
        """Evaluate the polynomial at a given list of points"""
        assert type(X) == list
        out = [0]*len(X)
        for pwr,coef in enumerate(self.coef):
            for pos,x in enumerate(X):
                out[pos] = (out[pos] + coef*(x**pwr))
        return out


    def degree(self):
        """Degree of the polynomial"""
        return len(self)-1

        
    def pretty_name(self):
        return poly_print_simple(self,pretty=True)



if __name__ == '__main__':
    P = RPoly([0,2,0,-6,2,0,0])
    Q = P*3
    R = RPoly([1,1])
    print(P)
    print(Q)
    print(P.is_monic())
    print(Q)
    print(f"P = {P}")
    print(f"P // {R} = {P//R}")
    print(f"P % {R} = {P%R}")
    print(P+1)
    print(1+P)
    print(f"P(2) = {P(2)}")