from Polynomials import Polynomial
from matplotlib import pyplot as plt

coef = [7,2,12,9,3,31]
F = 101

P = Polynomial(coef,F)

x = [i for i in range(101)]
y = P.evaluate(x)

s = str(P)

title = r"${}$ {}".format(s[:-9],s[-9:])
plt.scatter(x,y)
plt.title(title)