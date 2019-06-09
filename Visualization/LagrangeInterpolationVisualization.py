from Polynomials import lagrange_interpolation
import matplotlib.pyplot as plt
import numpy as np

points = np.array([1,3,5,7])
function = lambda x: np.sin(x)



print("""Lagrange interpolation takes a set of n points and finds the "best" polynomial that describes them. Given n points on a plane there is a polynomial of degree n-1 that passes through all of them.""")
print(f"In this example we use {len(points)} points taken from the sine function.")


fig = plt.figure()
ax=fig.add_axes([0,0,1,1])

lp = lagrange_interpolation(points,function)

print(lp)

x = np.linspace(min(points),max(points),50)

y0 = function(x)
y1 = lp.evaluate(x)

plt.plot(x,y0)
plt.plot(x,y1)
plt.scatter(points,function(points))