from TropicalSemiring import Tropical
from TropicalPolynomial import TropicalPoly
import numpy as np
import matplotlib.pyplot as plt

a = Tropical(5)
b = Tropical(8)

print(a)
print(b)
print(a+b)
print(a*b)
print(a**b)



a = Tropical(3)
b = Tropical(1)
c = Tropical(1)
P = TropicalPoly([a,b,c])
print(P)

x = list(np.linspace(-2,6,51))
y = P.evaluate(x)



plt.plot(x,y)