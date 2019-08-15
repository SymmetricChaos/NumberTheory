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
        if type(other) != Atom:
            return False
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
        if self == other:
            return MVPoly([])
        return self+(-other)


    def __rsub__(self,other):
        if self == other:
            return MVPoly([])
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
        self.vars = set([a.s for a in self.A])


    def __eq__(self,other):
        """Check if two Particles have the same atoms"""
        if type(other) != Particle:
            return False
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
    
    def __len__(self):
        """Number of indeterminates"""
        return len(self.A)
    

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
        if self == other:
            return MVPoly([])
        return self+(-other)


    def __rsub__(self,other):
        if self == other:
            return MVPoly([])
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
        self.vars = set()
        for t in self.terms:
            self.vars.update(t.vars)

    def __len__(self):
        """Numbers of terms used"""
        return len(self.terms)

    def __str__(self):
        """Print the MVPoly"""
        if len(self) == 0:
            return "0"
        out = str(self.terms[0])
        for term in self.terms[1:]:
            sgn = "-" if term.coef < 0 else "+"
            out +=  " " + sgn + " " + str(abs(term))
        return out
    

    def __eq__(self,other):
        """Check if two polynomials have identical Particles"""
        if type(other) != MVPoly:
            return False
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




def particle_div(P,Q):
    co = P.coef//Q.coef
    out = Particle([],co)
    for p in P.A:
        if p.s not in Q.vars:
            out *= p 
    
    for q in Q.A:
        if q.s not in P.vars:
            raise Exception(f"division of particle by indeterminates it does not contain is not yet supported")
    
    for p in P.A:
        for q in Q.A:
            if p.s == q.s:
                if p.p > q.p:
                    out *= Atom(p.s,p.p-q.p)
                    break
                elif p.p == q.p:
                    break
                else:
                    raise Exception(f"division of atoms by an atom with a greater power is not yet supported")

    return out

def poly_div(P,Q):
    P = P.copy()
    Q = Q.copy()
    if len(Q) == 0:
        raise ZeroDivisionError
#    print()
    out = MVPoly([])
    while len(P) >= len(Q):
#        print(P)
        try:
            div = particle_div(P.terms[0],Q.terms[0])
        except Exception as e:
#            print("HERE")
            print(e)
            break
        

        out += div
        P = P-(Q*div)

    return out,P

#a = Atom("a")

#P = 2*a**2 - 5*a - 1
#Q = a - 3
#print(P)
#print(Q)
#q,r = poly_div(P,Q)
#print("Quotient: ",q)
#print("Remainder:",r)
#
#print()

#P = a**2 - 3*a - 10
#Q = a + 2
#print(P)
#print(Q)
#q,r = poly_div(P,Q)
#print("Quotient: ",q)
#print("Remainder:",r)
#
#print()
#
#P = a**6 + 2*a**4 + 8*a - 10
#Q = a**3 + 3
#print(P)
#print(Q)
#q,r = poly_div(P,Q)
#print("Quotient: ",q)
#print("Remainder:",r)
