from ModularArithmetic import gcd

class Rational:
    
    def __init__(self,n,d=1):
        assert type(n) == int, "Numerator must be int."
        assert type(d) == int, "Denominator must be int."
        assert d != 0, "Division by zero error."
        if d < 0:
            d = abs(d)
            n = -n
        self.n = n
        self.d = d
        self.simplify()


    def simplify(self):
        g = abs(gcd(self.n,self.d))
        self.n = self.n//g
        self.d = self.d//g


    def inv(self):
        return Rational(self.d,self.n)


    def __neg__(self):
        return Rational(-self.n,self.d)


    def __str__(self):
        return str(self.n) + "/" + str(self.d)


    def __repr__(self):
        return str(self.n) + "/" + str(self.d)


    def __mul__(self,multiplier):
        if type(multiplier) == int:
            multiplier = Rational(multiplier)
            
        n = self.n * multiplier.n
        d = self.d * multiplier.d
        
        return Rational(n,d)


    def __rmul__(self,multiplier):
        if type(multiplier) == int:
            multiplier = Rational(multiplier)
        return self*multiplier


    def __truediv__(self,divisor):
        if type(divisor) == int:
            divisor = Rational(divisor)
        return self*divisor.inv()


    def __add__(self,addend):
        if type(addend) == int:
            addend = Rational(addend)
        
        n = self.n*addend.d + addend.n*self.d
        d = self.d*addend.d

        return Rational(n,d)


    def __radd__(self,addend):
        if type(addend) == int:
            addend = Rational(addend)
        return self + addend


    def __sub__(self,addend):
        return self + -addend


    def __rsub__(self,addend):
        return addend + -self


    def __eq__(self,other):
        if self.n == other.n:
            if self.d == other.d:
                return True
        return False
    
    
    def __pow__(self,power):
        assert type(power) == int,"Only powers of integers are supported"
        if power == 0:
            return Rational(1)
        if power == 1:
            return self
        else:
            n = self.n**power
            d = self.d**power
            return Rational(n,d)

    def whole_part(self):
        return self.n // self.d

    def fractional_part(self):
        return Rational(self.n % self.d, self.d)
    
    
    def mixed_form(self):
        """Whole and fractional part"""
        w = self.n // self.d
        f = self.fractional_part()
        return w,f
    
    def egyptian_form(self):
        """List of unit fractions that sum to the fraction"""
        
        # If the fraction is greater than one separate out the whole part
        L = []
        if self.n >= self.d:
            w,f = self.mixed_form()
            a = f.n
            b = f.d
            L.append(w)
        else:
            a = self.n
            b = self.d

        # Test each possible unit fraction discarding it if it is too big
        # Otherwise subtract it out until a unit fraction remains
        x = 2
        while a > 0:
            F1 = Rational(a*x,b*x)
            F2 = Rational(-1,x)
            s = F1+F2
            if s.n >= 0:
                a,b = s.n,s.d
                L.append(Rational(1,x))
                if a == 1:
                    L.append(Rational(1,b))
                    return L
            x += 1
            
        return L
    
    # See the computation director for an explanation of the division algorithm
    def digits(self,n):
        N = self.n
        D = self.d
        
        if(N % D == 0):
            return(str(N//D))
        
        pos = 0
        digits = []
        m = []
        ctr = 0
        
        for ctr in range(n):
            digits.append(N//D)
            N = (N % D)*10
            m.append(N)
        
        if(pos == 0):
            x1 = str(digits[0])
            x2 = "".join(str(e) for e in digits[1:])
            out = "{}.{}".format(x1,x2)
            
        return out
    
        