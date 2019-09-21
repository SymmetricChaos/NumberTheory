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


    # Will have to return a new object because type could change
    def simplify(self):
        pass


    def evaluate(self,X):
        assert type(X) == list
        N = self.n.evaluate(X)
        D = self.d.evaluate(X)
        return [float(a)/float(b) for a,b in zip(N,D)]


    def pretty_name(self):
        return f"$\dfrac{{{str(self.n)}}}{{{str(self.d)}}}$"


class RationalExp:
    
    def __init__(self,L):
        assert type(L) == list
        for r in L:
            assert type(r) == QPoly
        self.L = L
        
        
if __name__ == '__main__':
    P = QPoly([0,2,0,-6])
    Q = QPoly([1,3])
    R = RationalFrac(P,Q)
    print(R)
    
    
    import matplotlib.pyplot as plt
    import numpy as np

    x = list(np.linspace(-2.5,2.5,101))
    y = R.evaluate(x)
#    plt.plot(x,y)
    plt.title(R.pretty_name())
