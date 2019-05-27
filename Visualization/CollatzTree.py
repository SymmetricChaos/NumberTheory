import matplotlib.pyplot as plt
from math import log, floor

def collatz_inv(n):
    if n % 6 == 4:
        return 2*n, (n-1)//3
    return [2*n]


def collatz_tree_pos(L,narrowness=2):
    N,x,y = L
    if N == 4:
        return [[8,x,y+1],[1,0,0]]
    a = collatz_inv(N)
    if len(a) == 1:
        return [[a[0],x,y+1.2],[1,0,0]]
    return [[a[0],x-1/(y**narrowness),y+1.7], [a[1],x+1/(y**narrowness),y+1]]


def collatz_tree(levels,narrowness=2,text=True):
    D = set([1])
    S = [[1,0,0]]
    for i in range(levels):
        new = []
        for pt in S:
            t = collatz_tree_pos(pt,narrowness)
            if t[0][0] not in D:
                D.add(t[0][0])
                new.append(t[0])
                plt.plot( [pt[1],t[0][1]], [pt[2],t[0][2]],color='red')
            if t[1][0] not in D:
                D.add(t[1][0])
                new.append(t[1])
                plt.plot( [pt[1],t[1][1]], [pt[2],t[1][2]],color='red')
        S += new
    if text == True:
        for i in S:
            plt.scatter(i[1],i[2],s=350,color='white',zorder=3)
            plt.text(i[1],i[2],str(i[0]),ha='center',va='center',fontsize=15-floor(log(i[0],10)))
        
        
fig = plt.figure()
fig.set_size_inches(40, 20)
ax=fig.add_axes([0,0,1,1])
ax.set_axis_off()
collatz_tree(14,2.5,True)

#for i in collatz_inv_graph(1,10):
#    print(i)
#

#
#for i in collatz_inv_graph(1,5):
#    y = log(i[0],2)
#    plt.scatter(0,y)#,str(i[0]))
##    for n in i[1:]:
##        plt.scatter()