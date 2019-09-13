class QuadraticInt:
    def __init__(self,q,m=1,n=0):
        assert type(q) == int
        assert type(m) == int
        assert type(n) == int
        self.q = q
        self.m = m
        self.n = n


    # Deal with negatives
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
        # Qadratic part
        elif self.m != 1 and self.n == 0:
            return f"{self.m}√{self.q}"
        elif self.m == 1 and self.n != 0:
            return f"{self.n} + √{self.q}"
        # Full number
        else:
            return f"{self.n} + {self.m}√{self.q}"


    def __add__(self,other):
        if type(other) == int:
            return QuadraticInt(self.q,self.m,self.n+other)
        if type(other) == QuadraticInt:
            if from_same_ring(self,other):
                return QuadraticInt(self.q,
                                    self.m+other.m,
                                    self.n+other.n)
            

    def __radd__(self,other):
        return self + other
    
    
    def __sub__(self,other):
        return self + -other

   
    def __rsub__(self,other):
        return -self + other

    
    # Multiplication by other QuadInts doesn't work
    def __mul__(self,other):
        if type(other) == int:
            return QuadraticInt(self.q,
                                self.m*other,
                                self.n*other)
        if type(other) == QuadraticInt:
            if from_same_ring(self,other):
                return QuadraticInt(self.q,
                                    self.n*other.m+self.n*other.n,
                                    self.n*other.m+self.n*other.m*self.q)
            
    def __neg__(self):
        return self*-1
#    Its a ring so no division needed
#    Maybe factoring


def from_same_ring(A,B):
    if type(A) == QuadraticInt:
        if type(B) == QuadraticInt:
            return A.q == B.q
    return False

if __name__ == '__main__':
    q = QuadraticInt(5)
    print(q)
    print(3+q)
    print(q-1)
    r = 1-q*2
    print(r)
    print(r*q)