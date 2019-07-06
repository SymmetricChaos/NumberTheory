class Atom:
    """An indeterminate raised to a certain power"""
    
    def __init__(self,s,p=1):
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
    
    def __mul__(self,other):
        # If they are Atom with the same indeterminate sum their powers
        if other.s == self.s:
            return Atom(self.s,self.p+other.p)
        else:
            return Particle([self,other])
            
    def __pow__(self,other):
        assert type(other) == int
        assert other >= 0
        return Atom(self.s,self.p*other)



class Particle:
    """The product of some atoms"""
    
    def __init__(self,A,C=1):
        assert type(A) == list
        assert all([type(a) == Atom for a in A])
        self.A = sorted(A)
        self.C = C

        
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
        out = str(self.C) if self.C != 1 else ""
        for a in self.A:
            out += str(a)
        return out
    
    def __mul__(self,other):
        # When multiplied by another particle merge their atoms then sort
        if type(other) == Particle:
            ownatoms = self.A.copy()
            atomtypes = [c.s for c in ownatoms]
            for a in other.A:
                if a.s not in atomtypes:
                    ownatoms.append(a)
                else:
                    for i in range(len(ownatoms)):
                        if ownatoms[i].s == a.s:
                            ownatoms[i] = ownatoms[i]*a
            ownatoms = sorted(ownatoms)
            return Particle(ownatoms)
        
        #  When multiplied by an atom merge the atom of add it then sort
        if type(other) == Atom:
            ownatoms = self.A.copy()
            atomtypes = [at.s for at in ownatoms]
            if other.s not in atomtypes:
                ownatoms.append(a)
            else:
                for i in range(len(ownatoms)):
                    if ownatoms[i].s == other.s:
                        ownatoms[i] = ownatoms[i]*other
            ownatoms = sorted(ownatoms)
            return Particle(ownatoms)
        
        # When multiplied by an number just change the coefficient
        return Particle(self.A,self.C*other)
        

    def eval(self,V):
        """Evaluate all indeterminates of the Particle"""
        assert type(V) == dict
        out = 0
        for a in self.A:
            out += V[a.s]**a.p
        return out*self.C

#    def reduce:
#        """Evaluate some indeterminates of the Particle"""
    
class PolyMult:
    """Polynomial with various indeterminates"""
    
    def __init__(self,P):
        self.P = sorted(P)
    
    def __str__(self):
        out = ""
        for i in self.P:
            out += str(i) + " + "
        return out
    
    def eval(self,V):
        """Evaluate each particle"""
        assert type(V) == dict
        out = 0
        for p in self.P:
            out += p.eval(V)
        return out


a = Atom("a")**3
b = Atom("b")
c = Atom("c")**2


P = Particle([b,a])
Q = Particle([b,a,c],2)
print(P)
print(Q)
print(P*Q)
print(P*Q*a*3)

print(Q.eval({"a":2,"b":3,"c":4}))


Pol = PolyMult([P,Q,Particle([a])])
print(Pol)
print(Pol.eval({"a":2,"b":3,"c":4}))