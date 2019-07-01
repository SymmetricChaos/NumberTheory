class Atom:
    """An indeterminate raised to a certain power"""
    
    def __init__(s,p):
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
        
    
class Particle:
    """The product of some atoms"""
    
    def __init__()
    
class PolyMult:
    
    def __init__()