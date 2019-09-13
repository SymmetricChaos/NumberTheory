class QuadraticInt:
    def __init__(self,q,m=1,n=0):
        assert type(q) == int
        assert type(m) == int
        assert type(n) == int
        self.q = q
        self.m = m
        self.n = n

        
    def __str__(self):
        # Zero
        if self.m == 0 and self.n == 0:
            return "0"
        # One
        elif self.m == 0 and self.n == 1:
            return f"1"
        # Just the quadratic
        elif self.m == 1 and self.n == 0:
            return f"√{self.q}"
        # Integer part
        elif self.m == 0 and self.n != 1:
            return f"{self.n}"
        # Quadratuc part
        elif self.m != 1 and self.n == 0:
            return f"{self.m}√{self.q}"
        # Full number
        else:
            return f"{self.n} + {self.m}√{self.q}"

    
    def from_same_ring(self,other):
        assert type(other) == QuadraticInt
        assert other.q == self.q

#    def __add__
#    def __sub__
#    def __mul__
#    Its a ring so no division needed
#    Maybe factoring