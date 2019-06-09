from Computation.Collatz import collatz
import matplotlib.pyplot as plt

init = 1121
L = [c for c in collatz(init)]
N = [i for i in range(len(L))]

plt.bar(N,L)
plt.title("The Hailstone Sequence Starting at {}".format(init))