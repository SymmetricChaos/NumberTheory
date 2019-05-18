from Rationals import farey_sequence
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 6)

N = 125
F = farey_sequence(N)

x = [i for i in range(len(F))]
y = [f.d for f in F]

plt.title(f"Denominators of the Farey Sequence F({N})")
plt.scatter(x,y,s=3)