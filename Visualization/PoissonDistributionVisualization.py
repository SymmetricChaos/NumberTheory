from Combinatorics.Distributions import PoissonDist
import matplotlib.pyplot as plt


D1 = PoissonDist(3.2)
x1 = [i for i in range(10)]
y1 = [D1[i] for i  in x1]

plt.scatter(x1,y1)