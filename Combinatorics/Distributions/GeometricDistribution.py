def geometric_eq(p,k):
     return (1-p)**k*p


class GeometricDist:
    
    def __init__(self,p):
        self.p = p
        self.mean = (1-p)/p
        self.var = (1-p)/p**2
        
        
    def  __getitem__(self,k):
        return geometric_eq(self.p,k)