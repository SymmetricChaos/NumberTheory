from Combinatorics import dyck_words
import matplotlib.pyplot as plt

N = 4
D = dyck_words(N)

for d in D:
    fig = plt.figure()
    fig.set_size_inches(3,3)
    ax=fig.add_axes([0,0,1,1])
    ax.set_axis_off()
    plt.ylim(0,N+1)
    x = [i for i in range(2*N+1)]
    y = [0]*len(x)
    for ctr,i in enumerate(d,1):
        if i == "(":
            y[ctr] = y[ctr-1]+1
        if i == ")":
            y[ctr] = y[ctr-1]-1
    plt.plot(x,y)