from Combinatorics import choose

def multinomial_eq(n,p,k):
     return choose(n,k)*p**k*(1-p)**(n-k)


class MultinomialDist:
    
    def __init__(self,n,p):
        self.n = n
        self.p = p
        self.mean = None
        
        
    def  __getitem__(self,k):
        return multinomial_eq(self.n,self.p,k)
    
    def __iter__(self):
        for k in range(self.n+1):
            yield multinomial_eq(self.n,self.p,k)

