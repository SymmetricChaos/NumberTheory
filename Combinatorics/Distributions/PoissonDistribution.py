from Combinatorics import factorial
from math import exp

def poisson_eq(l,k):
     return (l**k*exp(-l))/factorial(k)


class PoissonDist:
    
    def __init__(self,l):
        self.l = l
        self.mean = l
        self.var = l
        
        
    def  __getitem__(self,k):
        return poisson_eq(self.l,k)