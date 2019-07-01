class Atom:
    """An indeterminate raised to a certain power"""
    
    def __init__(self,s,p):
        assert type(s) == str
        assert s in "abcdefghijklmnopqrstuvwxyz"
        assert type(p) == int
        assert p >= 0
        
        self.s = s
        self.p = p
        
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
    
class Particle:
    """The product of some atoms"""
    
    def __init__(self,A):
        assert type(A) == list
        assert all([type(a) == Atom for a in A])
        self.A = A
        print(sorted(A))
        
    def __lt__(self,other):
        assert type(other) == Particle
        x = sum([a.p for a in self.A])
        y = sum([a.p for a in other.A])
        return x < y
        
    
class PolyMult:
    """Polynomial with various indeterminates"""
    
    def __init__(self):
        pass


a = Atom("a",3)
b = Atom("b",1)
c = Atom("c",2)

Particle([b,c,a])