from Computation.Factorization import factorization
import matplotlib.pyplot as plt
from math import floor
from numpy import linspace
from functools import reduce
from operator import mul


N = [i for i in range(2,200)]
D = [len(factorization(n)) for n in N]
    
print(D)

D2 = [d/(n**1) for d,n in zip(D,N)]
plt.scatter(N,D)
#plt.scatter(N,D2)

def prod(L):
    return reduce(mul,L,1)

def e(x,p):
    return floor( 1 / ( p**(1/x) -1 ) )

#R = [i for i in linspace(1,20,50)]
#P = [2,3,5,7,11,13,17]

#for r in R:
#    E = [p**e(r,p) for p in P]
#    print(prod(E))
#plt.scatter(R,E)