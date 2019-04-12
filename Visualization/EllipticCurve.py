from EllipticCurves.EllipticCurveOOP import elliptic_points
from matplotlib import pyplot as plt

a = 2
b = 3
F = 101

P = elliptic_points(a,b,F)
x = [p[0] for p in P]
y = [p[1] for p in P]

title = r"$y^2 = x^3 + {}x + {} \ \ \ \ \  GF({})$".format(a,b,F)
plt.scatter(x,y)
plt.title(title)