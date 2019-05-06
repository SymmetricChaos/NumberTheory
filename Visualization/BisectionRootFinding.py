from Polynomials import Polynomial
from Computation.RootFinding import bisection_method_convergents
from numpy import linspace
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(10, 6)

P = Polynomial([-2,-1,0,1])
print(P)

x = linspace(-0,2,30)
y = P.evaluate(x)[0]

def poly_eval(x):
    return P.evaluate(x)[0]

plt.plot(x,y)
plt.axhline(0)
con = bisection_method_convergents(0,2,poly_eval,6)
for ctr,pos in enumerate(con):
    plt.scatter(pos,0,zorder=3,color='black')
    plt.text(pos-.01,.15,str(ctr+1))
    print(pos)
    