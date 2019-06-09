from Fourier import Fourier, evaluate_series
import numpy as np

A = Fourier([1],[1],[1])
B = Fourier([1.5],[3],[2])
C = A+B
x = np.linspace(-5,5,150)

yA = evaluate_series(A,x)
yB = evaluate_series(B,x)
yC = evaluate_series(C,x)

import matplotlib.pyplot as plt

plt.plot(x,yA,color='grey',linestyle=":")
plt.plot(x,yB,color='grey',linestyle=":")
plt.plot(x,yC,color='black')
print(A)
print(B)