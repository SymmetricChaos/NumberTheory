from Rationals import farey_sequence
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 6)

F = farey_sequence(100)

x = [i for i in range(len(F))]
y = [f.d for f in F]

plt.scatter(x,y,s=1)