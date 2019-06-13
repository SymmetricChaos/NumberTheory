from Combinatorics.Distributions import BinomialDist
import matplotlib.pyplot as plt


D1 = BinomialDist(20,.5)
x1 = [i for i in range(21)]
y1 = [i for i in D1]

D2 = BinomialDist(20,.7)
x2 = [i for i in range(21)]
y2 = [i for i in D2]

D3 = BinomialDist(40,.5)
x3 = [i for i in range(41)]
y3 = [i for i in D3]


plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)