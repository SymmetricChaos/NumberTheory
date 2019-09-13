class QuadraticInt:
    def __init__(self,q,m=1):
        assert type(q) == int
        assert type(m) == int
        self.q = q
        self.m = m

        
    def __str__(self):
        if self.m == 0:
            return "0"
        elif self.m == 1:
            return f"√{self.q}"
        else:
            return f"{self.m}√{self.q}"

    
    def same_ring(self,other):
        assert type(other) == QuadraticInt
        assert other.q == self.q

#    def __add__
#    def __sub__
#    def __mul__
#    Its a ring so no division needed
#    Maybe factoring