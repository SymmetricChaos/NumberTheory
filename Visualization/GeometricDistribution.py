from Combinatorics.Distributions import GeometricDist
import matplotlib.pyplot as plt


D1 = GeometricDist(.7)
x1 = [i for i in range(5)]
y1 = [D1[i] for i  in x1]

D2 = GeometricDist(.4)
x2 = [i for i in range(5)]
y2 = [D2[i] for i  in x2]

plt.plot(x1,y1)
plt.plot(x2,y2)