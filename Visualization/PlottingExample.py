import matplotlib.pyplot as plt

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_axis_off()


im = ax.imshow([[2,3,4,1], [2,4,4,2]], origin="lower", extent=[1,4,2,8])
ax.plot([1,2,3,4], [2,3,4,8], lw=5)

ax.scatter([2,3,4,1], [2,3,4,8], c="r", s=2500)

ax.set_aspect('auto')
plt.show()