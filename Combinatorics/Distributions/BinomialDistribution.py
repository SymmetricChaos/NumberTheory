from Combinatorics import choose

class BinomialDist:
    
    def __init__(self,n,p):
        self.n = n
        self.p = p
        pmf = []
        for k in range(n+1):
            pmf.append( choose(n,k)*p**k*(1-p)**(n-k) )
        self.pmf = pmf
        self.mean = n*p
        
        
    def  __getitem__(self,k):
        return self.pmf[k]

    def __iter__(self):
        for i in self.pmf:
            yield i
            
#D = BinomialDist(20,.7)
#
#for i in D:
#    print(i)