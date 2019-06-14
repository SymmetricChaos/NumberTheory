def geometric_eq(p,k):
     return (1-p)**(k-1)*p


class GeometricDist:
    
    def __init__(self,p):
        self.p = p
        self.mean = 1/p
        
        
    def  __getitem__(self,k):
        return geometric_eq(self.p,k)
    
    
    def __iter__(self):
        k = 0
        while True:
            yield geometric_eq(self.p,k)
            k += 1