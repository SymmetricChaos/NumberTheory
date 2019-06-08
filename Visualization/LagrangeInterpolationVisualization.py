from Polynomials import lagrange_interpolation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])

F = lambda x: x**3
lp = lagrange_interpolation([1,2,3],F)

print(lp)

x0 = np.linspace(1,3,20)
y0 = F(x0)


x1 = np.linspace(1,3,20)
y1 = lp.evaluate(x1)
plt.plot(x1,y1)
plt.plot(x0,y0)