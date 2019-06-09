from Fourier import Fourier, evaluate_series
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-4,4,150)
pi = np.pi
S = Fourier([0],[0],[0])
for i in [1,3,5]:
    A = Fourier([4/(pi*i)],[i])
    plt.plot(x,evaluate_series(A,x),color='gray',linestyle=":")
    S += A

yS = evaluate_series(S,x)
plt.plot(x,yS,color='black')