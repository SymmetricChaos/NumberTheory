from TropicalSemiring import Tropical
import matplotlib.pyplot as plt
import numpy as np

# Equivalent to the tropical polynomial 3x+4
#def func(x):
#    return min(x+3,4)

# Equivalent to the tropical polynomial ax^2 + bx + c
def func(x,a,b,c):
    return min(a+2*x,b+x,c)

x = np.linspace(-1,3)
y = [func(i,1,1,3) for i in x]

plt.plot(x,y)