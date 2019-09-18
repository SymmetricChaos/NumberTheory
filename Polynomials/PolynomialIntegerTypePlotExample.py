import matplotlib.pyplot as plt
import numpy as np
from Polynomials.PolynomialIntegerType import ZPoly

P = ZPoly([0,2,3,0,-116,20,-18,-6,1,0,1])

x = list(np.linspace(-2.5,2.5,101))
y = P.evaluate(x)
plt.plot(x,y)
print(P.coef)
print(str(P))
plt.title(P.pretty_name())
