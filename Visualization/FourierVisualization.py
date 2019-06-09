from Fourier import Fourier, evaluate_series
import numpy as np

A = Fourier([2],[1],[1])
B = Fourier([1.5],[3],[2])
C = Fourier([1],[.5],[1.2])
S = A+B+C
x = np.linspace(-8,8,150)

yA = evaluate_series(A,x)
yB = evaluate_series(B,x)
yC = evaluate_series(C,x)
yS = evaluate_series(S,x)

import matplotlib.pyplot as plt

plt.plot(x,yA,color='grey',linestyle=":")
plt.plot(x,yB,color='grey',linestyle=":")
plt.plot(x,yC,color='grey',linestyle=":")
plt.plot(x,yS,color='black')

print(D)