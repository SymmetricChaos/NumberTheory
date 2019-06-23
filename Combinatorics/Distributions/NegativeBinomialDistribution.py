from Combinatorics import choose

def neg_binomial_eq(r,p,k):
     return choose(k+r-1,k)*(1-p)**r*p**k


class NegativeBinomialDist:
    
    def __init__(self,r,p):
        assert r > 0
        assert p > 0 and p < 1
        self.p = p
        self.r = r
        self.mean = p*r/(1-p)
        self.var = (p*r)/(1-p)**2
        
        
    def  __getitem__(self,k):
        return neg_binomial_eq(self.r,self.p,k)