from Polynomials.PolynomialRationalType import QPoly

## TODO: rational fractions will be ratios of QPoly
## TODO: rational expressions will be sums of rational fraction

class RationalFrac:
    
    def __init__(self,n,d):
        assert type(n) == QPoly
        assert type(d) == QPoly
        self.n = n
        self.d = d
      
    
    def __str__(self):
        return f"{str(self.n)} / {str(self.d)}"


    def evaluate():
        pass
    
    
    # Will have to return a new object because type could change
    def simplify(self):
        pass
    
    
    #LaTeX formatting
    def pretty_name(self):
        return 


class RationalExp:
    
    def __init__(self,L):
        assert type(L) == list
        for r in L:
            assert type(r) == QPoly
        self.L = L