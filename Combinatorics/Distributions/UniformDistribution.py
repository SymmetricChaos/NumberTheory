def uniform_eq(a,b,k,v):
    if k >= a and k <= b:
        if type(k) == int:
            return v
    return 0


class UniformDist:
    
    def __init__(self,a,b):
        assert a < b
        assert type(a) == int
        assert type(b) == int
        self.a = a
        self.b = b
        self.n = b-a+1
        self.mean = (a+b)/2
        self.var = ((b-a+1)**2 - 1)/12
        self.support = range(a,b+1)
        
        
    def  __getitem__(self,k):
        assert k in self.support
        return uniform_eq(self.a,self.b,k,1/self.n)
