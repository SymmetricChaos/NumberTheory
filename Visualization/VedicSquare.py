from Computation.DigitalSum import digital_sum
import matplotlib.pyplot as plt
from matplotlib.cm import rainbow

def digital_root_alt(n,m):
    if n < m:
        return n
    while n > m:
        n = digital_sum(n)
    return n

def show_vedic_square(m):
    L = []
    for i in range(1,m):
        L.append( [digital_root_alt(i*n,m) for n in range(1,m)] )
    #equal_spacing_grid(L,len(str(m))+1,'left')
    return L

m = 25
V = show_vedic_square(m)


fig = plt.figure()
ax=fig.add_axes([0,0,2,2])
ax.set_axis_off()
ax.set_aspect('equal')

cls = rainbow([i/m for i in range(m+1)])

for x,v in enumerate(V,1):
    for y,n in enumerate(v) :
        ax.scatter(x/m,(9-y)/m, c=cls[n], s=350)