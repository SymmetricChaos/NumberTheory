def discrete_eq(a,b,k,v):
    if k >= a and k <= b:
        if type(k) == int:
            return v
    return 0


class DiscreteDist:
    
    def __init__(self,a,b):
        assert a < b
        self.a = a
        self.b = b
        self.n = b-a+1
        self.mean = (a+b)/2
        
        
    def  __getitem__(self,k):
        return discrete_eq(self.a,self.b,k,1/self.n)
    
    def __iter__(self):
        for k in range(self.a,self.b+1):
            yield discrete_eq(self.a,self.b,k,1/self.n)
