from EllipticCurves import Elliptic_Curve
from matplotlib import pyplot as plt

a = 2
b = 3
F = 51

P = Elliptic_Curve(a,b,F).points()
x = [p[0] for p in P]
y = [p[1] for p in P]

title = r"$y^2 = x^3 + {}x + {}$  (mod {})".format(a,b,F)
plt.scatter(x,y)
plt.title(title)