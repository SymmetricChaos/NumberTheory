from Polynomials import lagrange_interpolation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])

F = lambda x: x**x
lp = lagrange_interpolation([1,2,3,4],F)

print(lp)

x0 = np.linspace(1,4,20)
y0 = F(x0)


x1 = np.linspace(1,4,20)
y1 = lp.evaluate(x1)
plt.plot(x1,y1)
plt.plot(x0,y0)
plt.scatter([1,2,3,4],[F(1),F(2),F(3),F(4)])