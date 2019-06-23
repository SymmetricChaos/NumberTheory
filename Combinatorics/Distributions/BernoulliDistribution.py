from Combinatorics.Distributions.DistributionFunctions import is_prob


def bernoulli_eq(p,k):
     if k == 0:
         return 1-p
     if k == 1:
         return p


class BernoulliDist:
    
    def __init__(self,p):
        assert is_prob(p)
        self.n = 2
        self.p = p
        self.q = 1-p
        self.mean = p
        self.var = p*(1-p)
        self.support = [0,1]
        
        
    def  __getitem__(self,k):
        return bernoulli_eq(self.p,k)