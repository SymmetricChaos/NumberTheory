from Combinatorics import choose
from Combinatorics.Distributions.DistributionFunctions import is_prob

def binomial_eq(n,p,k):
     return choose(n,k)*p**k*(1-p)**(n-k)

class BinomialDist:
    
    def __init__(self,n,p):
        assert is_prob(p)
        self.n = n
        self.p = p
        self.mean = n*p
        self.var = n*p*(1-p)
        self.support = range(n+1)
        
    def  __getitem__(self,k):
        assert k <= self.n
        return binomial_eq(self.n,self.p,k)