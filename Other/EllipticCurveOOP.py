def elliptic_points(a,b,field):
    out = [(0,0)]
    for i in range(field):
        R = (i**3 + a*i + b) % field
        for j in range(field):
            L = (j**2) % field
            if R == L:
                out.append((i,j))
    return out

class elliptic:
    
    def __init__(self,a,b,field):
        if 4*a**3 + 27*b**2 == 0:
            raise Exception("Elliptic curves must be non-singular")
        self.a = a
        self.b = b
        self.field = field
        self.points = elliptic_points(a,b,field)

print(elliptic_points(1,-1,61))