from Combinatorics.Distributions import GeometricDist
import matplotlib.pyplot as plt


D1 = GeometricDist(.7)
x1 = [i for i in range(5)]
y1 = [D1[i] for i  in x1]

plt.scatter(x1,y1)