import matplotlib.pyplot as plt
import numpy as np
from Polynomials.PolynomialIntegerType import IntPolynomial

P = IntPolynomial([3,2,3,2])

x = list(np.linspace(-3,3,101))
y = P.evaluate(x)
plt.plot(x,y)
plt.title(P.pretty_name())