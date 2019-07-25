from itertools import groupby

class Atom:
    """An indeterminate raised to a certain power"""
    
    def __init__(self,s,p=1):
        assert type(s) == str
        assert len(s) == 1
        assert type(p) == int
        assert p >= 1
        
        self.s = s
        self.p = p


    def __eq__(self,other):
        """Check that two atoms at the same"""
        assert type(other) == Atom
        return self.s == other.s and self.p == other.p


    def __lt__(self,other):
        """For sorting atoms"""
        assert type(other) == Atom
        return self.s < other.s


    def __str__(self):
        """Print an atom"""
        if self.p == 1:
            return f"{self.s}"            
        return f"{self.s}^{self.p}"


    def __repr__(self):
        """Print an atom"""
        if self.p == 1:
            return f"{self.s}"
        return f"{self.s}^{self.p}"


    def __add__(self,other):
        """Addition of atoms with other objects"""
        return Particle([self]) + other


    def __radd__(self,other):
        """Addition of atoms with other objects"""
        return Particle([self]) + other


    def __sub__(self,other):
        """Subtraction other objects from atoms"""
        if type(other) == Atom:    
            return Particle([self]) - Particle([other])
        return Particle([self]) - other
    
    
    def __rsub__(self,other):
        """Subtraction of atoms from other objects"""
        return Particle([self],-1) + other


    def __neg__(self):
        return 0-self


    def __mul__(self,other):
        """Multiply atoms with other objects"""
        if type(other) == Atom:
            # Atoms with different indeterminate sum their powers
            if other.s == self.s:
                return Atom(self.s,self.p+other.p)
            else:
                # Atoms with different indeterminate form a particle
                return Particle([self,other])
        if type(other) == Particle:
            # When multiplied by a Particle use Particle multiplication
            return other*self
        # If it is something else make a particle with self as the '
        #indeterminate and other as the coefficient
        return Particle([self],other)


    def __rmul__(self,other):
        """Multiplication is commutative"""
        return self*other


    def __pow__(self,other):
        """Integer exponentiation"""
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


    def __eq__(self,other):
        """Check if two Particles have the same atoms"""
        assert type(other) == Particle
        return self.A == other.A
    
        
    def __lt__(self,other):
        """For sorting Particles"""
        assert type(other) == Particle
        # First sort by number of indeterminates
        if len(self.A) != len(other.A):
            return len(self.A) > len(other.A)
        # If they are equal sort by the coefficients
        x = sum([a.p for a in self.A])
        y = sum([a.p for a in other.A])
        return x > y
    

    def __abs__(self):
        """Particle with a positive coefficient"""
        return Particle(self.A,abs(self.coef))


    def __str__(self):
        """Print the Particle"""
        if self.A == []:
            return str(self.coef)
        if self.coef == 1:
            out = ""
        elif self.coef == -1:
            out = "-"
        else:
            out = str(self.coef)
        for a in self.A:
            out += str(a)
        return out


    def __repr__(self):
        return str(self)


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
        """Multiplication is commutative"""
        return self*other


    def __add__(self,other):
        if type(other) == Atom:
            return MVPoly([self,Particle([other])])
        if type(other) == Particle:
            if particle_id(self) == particle_id(other):
                return Particle(self.A,self.coef+other.coef)
            else:
                return MVPoly([self,other])
        return MVPoly([self,Particle([],other)])


    def __sub__(self,other):
        if type(other) == Atom:
            return MVPoly([self,Particle([other*-1])])
        if type(other) == Particle:
            return MVPoly([self,other*-1])
        return MVPoly([self,Particle([],-other)])


    def eval(self,V):
        """Evaluate all indeterminates of the Particle"""
        assert type(V) == dict
        out = 1
        for a in self.A:
            out *= V[a.s]**a.p
        return out*self.coef


    def reduce(self,V):
        """Evaluate some indeterminates of the Particle"""
        assert type(V) == dict
        out = 1
        temp_atoms = self.A.copy()
        for v in V.items():
            for pos,a in enumerate(self.A):
                if v[0] == a.s:
                    del temp_atoms[pos]
                    out *= v[1]**a.p
                    break
        return Particle(temp_atoms,out*self.coef)


class MVPoly:
    """Polynomial with various indeterminates"""
    
    def __init__(self,terms):
        self.terms = poly_merge(sorted(terms))


    def __str__(self):
        """Print the MVPoly"""
        out = str(self.terms[0])
        for term in self.terms[1:]:
            sgn = "-" if term.coef < 0 else "+"
            out +=  " " + sgn + " " + str(abs(term))
        return out
    
    
    def __eq__(self,other):
        """Check if two polynomials have identical Particles"""
        assert type(other) == MVPoly
        return self.terms == other.terms
    
    
    def eval(self,V):
        """Evaluate each particle of the polynomial"""
        assert type(V) == dict
        out = 0
        for p in self.terms:
            out += p.eval(V)
        return out


    def __mul__(self,other):
        """Multiply together two polynomials"""
        if type(other) == MVPoly:
            out = []
            for p in self.terms:
                for q in other.terms:
                    out.append(p*q)
            return MVPoly(out)
        else:
            out = []
            for p in self.terms:
                out.append(p*other)
            return MVPoly(out)
        
    def __rmul__(self,other):
        """Multiplication is commutative"""
        return self * other

    
    def __add__(self,other):
        """Add together two polynomials"""
        if type(other) == MVPoly:
            return MVPoly(self.terms+other.terms)
        if type(other) == Particle:
            return MVPoly(self.terms+[other])
        if type(other) == Atom:
            return self + Particle([other])
        return self + Particle([],other)
    
    def __radd__(self,other):
        """Addition is commutative"""
        return self + other

def particle_id(part):
    """Get the atoms of the particle"""
    out = ""
    for a in part.A:
        out += str(a)
    return out


def poly_merge(L):
    """Merge like terms"""
    terms = []
    for k,g in groupby(L,particle_id):
        G = list(g)
        t = G[0]
        for i in G[1:]:
            t += i
        terms.append(t)
    return poly_trim(terms)

def poly_trim(L):
    """Remove terms with coef 0"""
    terms = []
    for t in L:
        if t.coef != 0:
            terms.append(t)
    return terms