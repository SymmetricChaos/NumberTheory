from Polynomials import Polynomial
from Computation.RootFinding import bisection_method_convergents
from numpy import linspace
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 6)

P = Polynomial([-2,-1,0,1])
print(P)

x = linspace(0,2,30)
y = P.evaluate(x)[0]

def poly_eval(x):
    return P.evaluate(x)[0]

plt.plot(x,y)
plt.axhline(0)
con = bisection_method_convergents(0,2,poly_eval,10)
prev = 0
for ctr,pos in enumerate(con):
    plt.scatter(pos,poly_eval(pos),zorder=3,color='black')
    plt.plot([prev,pos],[4-ctr*.2,4-ctr*.2],color='black')
    print(pos)
    
    prev = pos