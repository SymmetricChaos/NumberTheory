class Atom:
    """An indeterminate raised to a certain power"""
    
    def __init__(self,s,p):
        assert type(s) == str
        assert s in "abcdefghijklmnopqrstuvwxyz"
        assert type(p) == int
        assert p >= 0
        
        self.s = s
        self.p = p
        self.D = {s:p}
        
    def __eq__(self,other):
        assert type(other) == Atom
        if self.s == other.s and self.p == other.p:
            return True
        return False
    
    def __lt__(self,other):
        assert type(other) == Atom
        return self.s < other.s
    
    def __str__(self):
        if self.p == 1:
            return f"{self.s}"
        return f"{self.s}^{self.p}"
    
    def __repr__(self):
        if self.p == 1:
            return f"{self.s}"
        return f"{self.s}^{self.p}"
    
    def __mul__(self,other):
        # If they are Atom with the same indeterminate sum their powers
        if other.s == self.s:
            return Atom(self.s,self.p+other.p)
        # If they have different indeterminates combine them as a particle
        else:
            return Particle([self,other])

            
    
class Particle:
    """The product of some atoms"""
    
    def __init__(self,A):
        assert type(A) == list
        assert all([type(a) == Atom for a in A])
        self.A = sorted(A)
        self.D = dict()
        for a in self.A:
            self.D[a.s] = a.p
        
    def __lt__(self,other):
        assert type(other) == Particle
        # First sort by number of indeterminates
        if len(self.A) != len(other.A):
            return True
        # If they are equal sort by the coefficients
        x = sum([a.p for a in self.A])
        y = sum([a.p for a in other.A])
        return x < y
    
    def __str__(self):
        out = ""
        for a in self.A:
            out += str(a)
        return out
    
#    def __mul__(self,other):
                
    
class PolyMult:
    """Polynomial with various indeterminates"""
    
    def __init__(self,P,C):
        pass


a = Atom("a",3)
b = Atom("b",1)
c = Atom("c",2)

print(Particle([b,a,c]))

P = Particle([b,a])

print(a*b)