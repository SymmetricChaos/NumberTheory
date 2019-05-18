from GeneralUtils import equal_spacing


def pascals_triangle(n):
    """The first n rows of pascal's triangle"""
    out = [[1]]
    L = [1]
    for i in range(1,n):
        t = [0] + L
        for i in range(len(L)):
            t[i] += L[i]
        L = t
        out.append(L)
    return out
        

def show_pascals_triangle(n,w=5):
    triangle = pascals_triangle(n)
    
    for ctr,row in enumerate(triangle):
        equal_spacing(row,w,'left')
        
show_pascals_triangle(8)