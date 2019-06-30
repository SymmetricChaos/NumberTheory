from TropicalSemiring import Tropical
from TropicalPolynomial import TropicalPoly
import numpy as np

a = Tropical(5)
b = Tropical(8)

print(a)
print(b)
print(a+b)
print(a*b)
print(a**b)


P = TropicalPoly([b,a])
print(P)

x = list(np.linspace(-2,6,51))
y = P.evaluate(x)


import matplotlib.pyplot as plt

plt.plot(x,y)

print(a**0)