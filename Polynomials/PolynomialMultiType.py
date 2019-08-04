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
        return self+other


    def __sub__(self,other):
        return self+(-other)


    def __rsub__(self,other):
        return -self+other
    
    
    def __neg__(self):
        return -1*self


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
    
    
#    def __divmod__(self,other):
#        assert type(other) == Atom
#        if self.s != other.s:
#            raise Exception("Division of an atom by differnet atoms not yet supported")
#        if self.p > other.p:
#            return Atom(self.s,self.p-other.p)
#        if self.p < other.p:
#            raise Exception("Division of an atom by a larger atom not yet supported")


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
        # If they have different numbers of indeterminates sort by which has
        # more indeterminates
        if len(self.A) != len(other.A):
            return len(self.A) > len(other.A)
        # If they have the same number of indeterminates then sort by which has
        # overall greater powers
        x = sum([a.p for a in self.A])
        y = sum([a.p for a in other.A])
        if x != y:
            return x > y
        # If the powers are overall the same then sort by the leading atoms
        for i,j in zip(self.A,other.A):
            if i.s != j.s:
                return i.s > j.s
        # if that fails then sort by the powers of the atoms
        for i,j in zip(self.A,other.A):
            if i.p != j.p:
                return i.p > j.p
    

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
        """Particle addition"""
        if type(other) == Atom:
            return MVPoly([self,Particle([other])])
        if type(other) == Particle:
            if particle_id(self) == particle_id(other):
                return Particle(self.A,self.coef+other.coef)
            else:
                return MVPoly([self,other])
        if type(other) == MVPoly:
            return MVPoly([self]+other.terms)
        return MVPoly([self,Particle([],other)])


    def __radd__(self,other):
        return other+self

    
    def __sub__(self,other):
        """Particle subtraction"""
        return self+(-other)


    def __rsub__(self,other):
        return -self+other
    

    def __pow__(self,other):
        assert type(other) == int
        assert other >= 0
        if other == 0:
            return 1
        else:
            out = self
            for i in range(other-1):
                out *= self
            return out


    def __neg__(self):
        return -1*self
    
    
    def copy(self):
        return Particle(self.A[:],self.coef)


    def evaluate(self,V):
        """Evaluate some or all indeterminates of the Particle"""
        co = self.coef
        new_atoms = []
        for a in self.A:
            if a.s in V:
                co *= V[a.s]**a.p
            else:
                new_atoms.append(a)
        return Particle(new_atoms,co)


    def derivative(self,T):
        """Derivative of some of all intederminates of the Particle"""
        co = self.coef
        new_atoms = []
        for a in self.A:
            if a.s in T:
                co *= a.p
                if a.p == 1:
                    continue
                else:
                    new_atoms.append(Atom(a.s,a.p-1))
            else:
                new_atoms.append(a)
        return Particle(new_atoms,co)

class MVPoly:
    """Polynomial with various indeterminates"""
    
    def __init__(self,terms):
        self.terms = poly_merge(sorted(terms))


    def __len__(self):
        """Numbers of terms used"""
        return len(self.terms)

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
        """MVPoly addition"""
        if type(other) == MVPoly:
            return MVPoly(self.terms+other.terms)
        if type(other) == Particle:
            return MVPoly(self.terms+[other])
        if type(other) == Atom:
            return MVPoly(self.terms+[Particle([other])])
        return MVPoly(self.terms+[Particle([],other)])


    def __radd__(self,other):
        """Addition is commutative"""
        return self + other


    def __sub__(self,other):
        return self+(-other)


    def __rsub__(self,other):
        return -self+other


    def __pow__(self,other):
        assert type(other) == int
        assert other >= 0
        if other == 0:
            return 1
        if other == 1:
            return self
        else:
            out = self
            for i in range(other-1):
                out *= self
            return out


    def __neg__(self):
        a = [-i for i in self.terms]
        return MVPoly(a)
    
    
    def copy(self):
        return MVPoly([t.copy() for t in self.terms])
    
    
    def evaluate(self,V):
        """Partially or entirely evaluate all terms of the MVPoly"""
        assert type(V) == dict
        a = [t.evaluate(V) for t in self.terms]
        return MVPoly(a)


    def derivative(self,T):
        """Partial derivative"""
        assert type(T) == list
        assert all([type(t) == str for t in T])
        a = [t.derivative(T) for t in self.terms]
        return MVPoly(a)




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
        if t.coef != 0:
            terms.append(t)
    return terms


def particle_divmod(P,Q):
    co,rco = divmod(P.coef,Q.coef)
    A, rA = [],[]
    for p in P.coef:
        for q in Q.coef:
            if p.s == q.s:
                d,r = divmod(p,q)
        print(p)

#def integer_division(P,Q):
#    P = P.copy()
#    Q = Q.copy()
#    out = []
#    while True:
#        if P[0] == Q[0]:
#            P -= Q
#        else:
            