from Sequences import kempner_function
import matplotlib.pyplot as plt

x = []
y = []
for n,i in enumerate(kempner_function()):
    x.append(n)
    y.append(i)
    if n > 50:
        break

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
#ax.set_axis_off()
ax.set_aspect('equal')
plt.bar(x,y)