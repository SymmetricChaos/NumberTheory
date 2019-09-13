class QuadraticInt:
    def __init__(self,q,m=1):
        self.q = q
        self.m = m
        
    def __str__(self):
        if self.m == 0:
            return "0"
        elif self.m == 1:
            return f"√{self.q}"
        else:
            return f"{self.m}√{self.q}"
        