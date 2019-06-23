def bernoulli_eq(p,k):
     if k == 0:
         return 1-p
     if k == 1:
         return p


class BernoulliDist:
    
    def __init__(self,p):
        self.n = 2
        self.p = p
        self.q = 1-p
        self.mean = p
        self.var = p*(1-p)
        
        
    def  __getitem__(self,k):
        return bernoulli_eq(self.p,k)
    
    def __iter__(self):
        for k in range(self.n+1):
            yield bernoulli_eq(self.p,k)

