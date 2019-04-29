# Rectangular grid

from GraphType import Graph

def man_dist(a,b):
    """Manhattan Distance"""
    return abs(a[0]+b[0]) + abs(a[1]+b[1])

def graph_grid(N):

    G = Graph(N**2)
    for j in range(N):
        for i in range(N-1):
            G.add_edge(i+N*j,i+N*j+1)
    
    
    for j in range(N-1):
        for i in range(N):
            G.add_edge(i+N*j,i+N*j+N)
            
    return G
    
G = graph_grid(6)
print(G)