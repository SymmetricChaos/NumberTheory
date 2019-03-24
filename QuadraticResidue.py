
def quad_residue(q,m):
    for i in range(m):
        if i**2 % m == q:
            return True

def find_quad_residue(m):
    L = []
    for i in range(m):
        q = i**2 % m
        if q not in L:
            L.append(q)
    L.sort()
    return L


for i in range(2,20):
    qr = find_quad_residue(i)
    
    print(qr)