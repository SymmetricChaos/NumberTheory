from Combinatorics.Distributions import BinomialDist
import matplotlib.pyplot as plt


D1 = BinomialDist(20,.7)
x1 = [i for i in range(21)]
y1 = [i for i in D1]

D2 = BinomialDist(14,.4)
x2 = [i for i in range(15)]
y2 = [i for i in D2]

plt.scatter(x1,y1)
plt.scatter(x2,y2)