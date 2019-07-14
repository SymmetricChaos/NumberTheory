from itertools import groupby

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
    
    def __add__(self,other):
        return Particle([self]) + other
    
    def __radd__(self,other):
        return Particle([self]) + other
    
    def __sub__(self,other):
        return Particle([self]) - other
    
    def __rsub__(self,other):
        return Particle([self]) - other
    
    def __mul__(self,other):
        if type(other) == Atom:
            # If they are Atom with the same indeterminate sum their powers
            if other.s == self.s:
                return Atom(self.s,self.p+other.p)
            else:
                return Particle([self,other])
        if type(other) == Particle:
            return other*self
        
        return Particle([self],other)
                
    def __rmul__(self,other):
        return self*other
    
    def __pow__(self,other):
        assert type(other) == int
        assert other >= 0
        return Atom(self.s,self.p*other)


class Particle:
    """The product of some atoms"""
    
    def __init__(self,A,coef=1):
        assert type(A) == list
        assert all([type(a) == Atom for a in A])
        self.A = sorted(A)
        self.coef = coef

        
    def __lt__(self,other):
        assert type(other) == Particle
        # First sort by number of indeterminates
        if len(self.A) != len(other.A):
            return len(self.A) > len(other.A)
        # If they are equal sort by the coefficients
        x = sum([a.p for a in self.A])
        y = sum([a.p for a in other.A])
        return x > y
    
    def __abs__(self):
        return Particle(self.A,abs(self.coef))
    
    def __str__(self):
        if self.A == []:
            return str(self.coef)
        out = str(self.coef) if self.coef != 1 else ""
        for a in self.A:
            out += str(a)
        return out
    
    def __repr__(self):
        out = str(self.coef) if self.coef != 1 else ""
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
            return Particle(ownatoms,self.coef*other.coef)
        
        #  When multiplied by an atom merge the atom of add it then sort
        if type(other) == Atom:
            ownatoms = self.A.copy()
            atomtypes = [at.s for at in ownatoms]
            if other.s not in atomtypes:
                ownatoms.append(other)
            else:
                for i in range(len(ownatoms)):
                    if ownatoms[i].s == other.s:
                        ownatoms[i] = ownatoms[i]*other
            ownatoms = sorted(ownatoms)
            return Particle(ownatoms,self.coef)
        
        # When multiplied by an number just change the coefficient
        return Particle(self.A,self.coef*other)
    
    def __rmul__(self,other):
        return self*other

    def eval(self,V):
        """Evaluate all indeterminates of the Particle"""
        assert type(V) == dict
        out = 1
        for a in self.A:
            out *= V[a.s]**a.p
        return out*self.coef
    
    def __add__(self,other):
        if type(other) == Atom:
            return PolyMult([self,Particle([other])])
        if type(other) == Particle:
            if self.particle_id() == other.particle_id():
                return Particle(self.A,self.coef+other.coef)
            else:
                return PolyMult([self,other])
        return PolyMult([self,Particle([],other)])
        
    def __sub__(self,other):
        if type(other) == Atom:
            return PolyMult([self,Particle([other*-1])])
        if type(other) == Particle:
            return PolyMult([self,other*-1])
        return PolyMult([self,Particle([],-other)])

    def particle_id(self):
        out = ""
        for a in self.A:
            out += str(a)
        return out

#    def reduce(self,V):
#        """Evaluate some indeterminates of the Particle"""
#        assert type(V) == dict
#        out = 1
#        for v in V.items():
#            if v[0] in self.A:
#                out *= A
#        return out*self.coef

class PolyMult:
    """Polynomial with various indeterminates"""
    
    def __init__(self,terms):
        self.terms = poly_merge(sorted(terms))
    
    def __str__(self):
        out = str(self.terms[0])
        for term in self.terms[1:]:
            sgn = "-" if term.coef < 0 else "+"
            out +=  " " + sgn + " " + str(abs(term))
        return out
    
    def eval(self,V):
        """Evaluate each particle of the polynomial"""
        assert type(V) == dict
        out = 0
        for p in self.terms:
            out += p.eval(V)
        return out
    
#    def merge(self):
#        """Merge together particles of the same kind"""
#        ctr = 0
#        while True:
#            for 

    def __mul__(self,other):
        """Multiply together two polynomials"""
        if type(other) == PolyMult:
            out = []
            for p in self.terms:
                for q in other.terms:
                    out.append(p*q)
            return PolyMult(out)
        else:
            out = []
            for p in self.terms:
                out.append(p*other)
            return PolyMult(out)

    
    def __add__(self,other):
        """Add together two polynomials"""
        return PolyMult(self.terms+other.terms)
    

a = Atom("a")
b = Atom("b")
c = Atom("c")

poly = a*b**2-1
print(poly)
#print(poly.eval({"a":2,"b":3,"c":4}))
#print(poly*poly)
pp = poly*poly*poly



def particle_id(part):
    return part.particle_id()


def poly_merge(L):
    terms = []
    for k,g in groupby(L,particle_id):
        G = list(g)
        t = G[0]
        for i in G[1:]:
            t += i
        terms.append(t)
    return terms

print(pp)
print(pp*(a-1))