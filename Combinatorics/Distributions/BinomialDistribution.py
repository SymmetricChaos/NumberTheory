from Combinatorics import choose

def binomial_eq(n,p,k):
     return choose(n,k)*p**k*(1-p)**(n-k)


class BinomialDist:
    
    def __init__(self,n,p):
        self.n = n
        self.p = p
        self.mean = n*p
        self.var = n*p*(1-p)
        
        
    def  __getitem__(self,k):
        return binomial_eq(self.n,self.p,k)
    
    def __iter__(self):
        for k in range(self.n+1):
            yield binomial_eq(self.n,self.p,k)

