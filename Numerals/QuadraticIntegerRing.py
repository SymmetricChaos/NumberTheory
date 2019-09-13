class QuadraticInt:
    def __init__(self,q,m=1,n=0):
        assert type(q) == int
        assert type(m) == int
        assert type(n) == int
        # Quadratic extension
        self.q = q
        # Multiple of the quadratic
        self.m = m
        # Integer part
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
        # If the quadratic part is negative
        elif self.m < 0:
            # Unit case
            if self.m == -1:
                if self.n == 0:
                    return f"-√{self.q}"
                else:
                    return f"{self.n} - √{self.q}"
            # General case
            if self.n == 0:
                return f"-{self.m}√{self.q}"
            else:
                return f"{self.n} - {abs(self.m)}√{self.q}"
        # Of the quadratic part is positive
        else:
            # Unit case
            if self.m == 1:
                if self.n == 0:
                    return f"√{self.q}"
                else:
                    return f"{self.n} + √{self.q}"
            # General case
            if self.n == 0:
                return f"{self.m}√{self.q}"
            else:
                return f"{self.n} + {self.m}√{self.q}"

    def __add__(self,other):
        if type(other) == int:
            return QuadraticInt(self.q,
                                self.m,
                                self.n+other)
        elif type(other) == QuadraticInt:
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

    
    def __mul__(self,other):
        if type(other) == int:
            return QuadraticInt(self.q,
                                self.m*other,
                                self.n*other)
        elif type(other) == QuadraticInt:
            if from_same_ring(self,other):
                return QuadraticInt(self.q,
                                    self.n*other.m + other.n*self.m,
                                    self.n*other.n + self.m*other.m*self.q)

    def __rmul__(self,other):
        return self*other
        
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
    print(1+0*q)
    print(0*q)
    print(1+q)
    print(1-q)
    print(1-2*q)
    
    
    
    